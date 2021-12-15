import pandas as pd
import random
import datetime
import sqlalchemy
import re

class ETL():
    data:pd.DataFrame = None

    def extract(self, data_source:str):
        source_type = self.__get_source_type(data_source)
        if source_type == 'CSV':
            self.__extract_from_csv(data_source)
        elif source_type == 'SQLITE':
            self.__extract_from_sqlite(data_source)
        elif source_type == 'MSSQL':
            self.__extract_from_mssql(data_source)
        else:
            return 'Data source name is wrong'


    def transform(self, criteria:dict):
        transformed_data = pd.DataFrame()
        for column in criteria['COLUMNS']:
            if column == '__all__':
                transformed_data = transformed_data.append(self.data)
            else:
                transformed_data = transformed_data.append({column: self.data[column]})

        return transformed_data



    def load(self, data_destination:str):
        source_type = self.__get_source_type(data_destination)
        if source_type == 'CSV':
            self.__load_to_csv(data_destination)
        elif source_type == 'SQLITE':
            self.__load_to_sqlite(data_destination)
        elif source_type == 'MSSQL':
            self.__load_to_mssql(data_destination)
        elif source_type == 'CONSOL':
            print(self.data)
        else:
            raise Exception(f'Couldn\'t connect with {data_destination}')



    def __get_source_type(self, data_source:str):
        if data_source == None:
            return 'CONSOL'
        elif re.search(r'.*\.csv(\.zip)?', data_source):   
            return 'CSV'
        elif re.search(r'.*\.db', data_source):
            return 'SQLITE'
        elif re.search(r'Data Source.*', data_source):
            return 'MSSQL'


    def __extract_from_csv(self, data_source):
        self.data = pd.read_csv(data_source, chunksize=100000, iterator=True)

        
    def __extract_from_sqlite(self, data_source):
        data_source = data_source.split(';')
        sqlite_engine = sqlalchemy.create_engine(f'sqlite:///{data_source[0]}')
        self.data = pd.read_sql(f'select * from {data_source[1]}', sqlite_engine)


    # Not Finished
    def __extract_from_mssql(self, data_source):
        mssql_engine = sqlalchemy.create_engine(f'mssql+pyodbc://{"server_name"}/{"mssql_db_name"}?trusted_connection=yes&driver=SQL+Server+Native+Client+11.0')
        table = mssql_engine.execute(f"SELECT * FROM {'table_name'};")
        self.data = pd.DataFrame(table, columns=table.keys())


    def __load_to_csv(self, data_destination):
        self.data.to_csv(data_destination + ".csv", header=None, mode='a')


    def __load_to_sqlite(self, data_destination):
        data_destination = data_destination.split(';')
        sqlite_engine = sqlalchemy.create_engine(f'sqlite:///{data_destination[0]}')

        for df in self.data:
            df.to_sql(data_destination[1], sqlite_engine, if_exists='append', index=False)

    # Not Finished
    def __load_to_mssql(self, connection_string):
        mssql_engine = sqlalchemy.create_engine(f'mssql+pyodbc://{"server_name"}/{"mssql_db_name"}?trusted_connection=yes&driver=SQL+Server+Native+Client+11.0')
        self.data.to_sql("table_name", mssql_engine, if_exists='append', index=False)


    @staticmethod
    def create_random_csv(csv_file_path, num_rows):
        """A function that create a csv file with random data (Name, Date_of_birth, Role, Phone_number, City)."""

        df = pd.DataFrame()

        # Generate random names column
        first_names = (
            'Mostafa', 'Mahmoud', 'Ibrahim', 'Hager', 'Abir', 'Ahmed', 'Ali', 'Fady', 'Menna', 'Kawther',
            'Abdo', 'Khaled', 'Mohammed', 'Mona', 'Manar', 'Fatma', 'Mark', 'Abdallah', 'Nour'
        )
        last_names = (
            'Mosa','Amin','Abbas', 'Ahmed', 'Saad', 'Mansour', 'Mahrous', 'Saeed', 'Shahin', 'Shazly', 
            'Nabil', 'Ibrahim', 'Walid', 'Mohamed', 'Gaber', 'Adel', 'Youssef', 'Emad', 'Ramadan', 'Mohsen'
        )
        df['name'] = list(random.choice(first_names) + " " + random.choice(last_names) for _ in range(num_rows))

        # Generate random date of birth column
        random_dates = []
        start_date = datetime.date(1999, 1, 1)
        end_date = datetime.date(2000, 12, 30)

        for _ in range(num_rows):
            random_number_of_days = random.randrange((end_date - start_date).days)
            random_date = start_date + datetime.timedelta(days=random_number_of_days)

            random_dates.append(random_date)

        df['date_of_birth'] = random_dates

        # Generate random role column with more Students
        roles = ('Student', 'Professor', 'Clerk')
        df['role'] = random.choices(roles, weights=[8, 1, 2], k=num_rows)
        
        # Geneare random phone numbers column
        phone_number_beginnings = ('010', '012', '011', '015')
        df['phone_number'] = [
            (random.choice(phone_number_beginnings) 
            + str(random.randint(pow(10, 7), pow(10, 8)))) 
            for _ in range (num_rows)
        ]

        # Generate random city column with more Suez
        cities = ('Suez', 'Ismailia', 'Cairo', 'Sadr', 'Alex', 'Giza')
        df['city'] = random.choices(cities, weights=[10, 2, 2, 1, 1, 1], k=num_rows)
        
        # Save the data into a zipped csv file
        df.to_csv(csv_file_path + ".csv.zip", index_label='id', compression='zip')

