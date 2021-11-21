import pandas as pd
import random
import datetime
import sqlalchemy

class ETL:

    @staticmethod
    def csv_to_sqlite(csv_file_path, columns_data_types={}, sqlite_db_file_path=None, table_name="csv_data"):
        """A function that opens and reads a csv file and copies its data into an sqlite database (given or created)."""

        if sqlite_db_file_path == None:
            db_file_path = csv_file_path + ".db"

        try:
            # Read csv file into a TextFileReader
            csv_data = pd.read_csv(csv_file_path, chunksize=100000, iterator=True, dtype=columns_data_types)

            sqlite_engine = sqlalchemy.create_engine(f'sqlite:///{db_file_path}')

            # Insert a csv data into the sqlite database
            for df in csv_data:
                df.to_sql(table_name, sqlite_engine, if_exists='append', index=False)

        except Exception as e:
            print(e)
            return False
        
        else:
            return True


    @staticmethod
    def mssql_to_sqlite(server_name="MOSA", mssql_db_name="Users", table_name="mssql_data", sqlite_db_file_path=None):
        """A function that opens and reads an mssql database and copies its data into an sqlite database (given or created)."""

        if sqlite_db_file_path == None:
            sqlite_db_file_path =  mssql_db_name + ".db"

        try:
            mssql_engine = sqlalchemy.create_engine(f'mssql+pyodbc://{server_name}/{mssql_db_name}?trusted_connection=yes&driver=SQL+Server+Native+Client+11.0')
            sqlite_engine = sqlalchemy.create_engine(f'sqlite:///{sqlite_db_file_path}')

            # Getting the table data we need
            table = mssql_engine.execute(f"SELECT * FROM {table_name};")

            # Turn the data into a pandas DataFrame
            df = pd.DataFrame(table, columns=table.keys())

            # Insert the data into the sqlite database
            df.to_sql(table_name, sqlite_engine, if_exists='append', index=False)

        except Exception as e:
            print(e)
            return False
        
        else:
            return True


    @staticmethod
    def make_query(sqlite_db_path,query):
        """A function that execute a series of queries given by the user."""

        sqlite_engine = sqlalchemy.create_engine(f'sqlite:///{sqlite_db_path}')

        try:
            result = sqlite_engine.execute(query)
            print(",".join(result.keys()))
            for row in result.fetchall():
                row = [str(i) for i in list(row)]
                print(",".join(row))

        except Exception as e:
            print(e)
            print("Couldn't execute query.")


    @staticmethod
    def csv_to_mssql(csv_file_path,server_name="MOSA", mssql_db_name="Users", table_name="csv_data", colums_data_types={}):
        """A function that opens and reads a csv file and copies its data into an mssql database."""

        try:
            csv_data = pd.read_csv(csv_file_path, chunksize=100000, iterator=True, dtype=colums_data_types)
            mssql_engine = sqlalchemy.create_engine(f'mssql+pyodbc://{server_name}/{mssql_db_name}?trusted_connection=yes&driver=SQL+Server+Native+Client+11.0')

            # Insert a csv data into the mssql database
            for df in csv_data:
                df.to_sql(table_name, mssql_engine, if_exists='append', index=False)

        except Exception as e:
            print(e)
            return False
        
        else:
            return True


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
        
