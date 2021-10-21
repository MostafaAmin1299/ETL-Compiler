from numpy.core.numeric import ones
import pandas as pd
import random
import datetime
import numpy as np
from sqlalchemy import create_engine

class ETL:

    @staticmethod
    def read_csv():
        pass

    @staticmethod
    def create_random_csv():
        N = 400
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
        df['city'] = random.choices(cities, weights=[10].append(ones(5, dtype=int)), k=N)
        
        df.to_csv('random_data.csv', index_label='id')
        

ETL.create_random_csv()
