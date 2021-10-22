import pandas as pd
import random
import datetime
import sqlalchemy

class ETL:

    @staticmethod
    def read_csv_into_sqlite(input_file):

        #Rrad csv file
        data = pd.read_csv(input_file, chunksize=100000, iterator=True, dtype = {"phone_number": str})

        #Create Sqlite database
        csv_database = sqlalchemy.create_engine(f'sqlite:///{input_file.split(".")[0]}.db')

        #Insert data in sqlite database
        for df in data:
            df.to_sql('my_data', csv_database, if_exists='append', index = False)



    @staticmethod
    def create_random_csv(file_name, N):
        df = pd.DataFrame()

        # Generate random names column
        first_names = ('Mostafa', 'Mahmoud', 'Ibrahim', 'Hager', 'Abir', 'Ahmed', 'Ali', 'Fady', 'Menna', 'Kawther', 'Abdo', 'Khaled', 'Mohammed', 'Mona', 'Manar', 'Fatma', 'Mark', 'Abdallah', 'Nour')
        last_names = ('Mosa','Amin','Abbas', 'Ahmed', 'Saad', 'Mansour', 'Mahrous', 'Saeed', 'Shahin', 'Shazly', 'Nabil', 'Ibrahim', 'Walid', 'Mohamed', 'Gaber', 'Adel', 'Youssef', 'Emad', 'Ramadan', 'Mohsen')
        df['name'] = list(random.choice(first_names) + " " + random.choice(last_names) for _ in range(N))

        # Generate random date of birth column
        random_dates = []
        start_date = datetime.date(1999, 1, 1)
        end_date = datetime.date(2000, 12, 30)
        for _ in range(N):
            random_number_of_days = random.randrange((end_date - start_date).days)
            random_date = start_date + datetime.timedelta(days=random_number_of_days)
            random_dates.append(random_date)
        df['date_of_birth'] = random_dates

        # Generate random role column
        roles = ('Student', 'Professor', 'Clerk')
        df['role'] = random.choices(roles, weights=[8, 1, 2], k=N)
        
        # Geneare random phone numbers column
        phn_start = ('010', '012', '011', '015')
        df['phone_number'] = [(random.choice(phn_start) + str(random.randint(pow(10, 7), pow(10, 8)))) for _ in range(N)]

        # Generate random city column
        cities = ('Suez', 'Ismailia', 'Cairo', 'Sadr', 'Alex', 'Giza')
        df['city'] = random.choices(cities, weights=[10, 2, 2, 1, 1, 1], k=N)
        
        df.to_csv(file_name + ".csv.zip", index_label='id', compression='zip')
        
