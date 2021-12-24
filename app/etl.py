from typing import Union
import pandas as pd
import sqlalchemy
import re

class ETL():
    @staticmethod
    def extract(data_source:str) -> pd.DataFrame:
        source_type = ETL.__get_source_type(data_source)
        if source_type == 'CSV':
            data = ETL.__extract_from_csv(data_source)
        elif source_type == 'SQLITE':
            db = data_source.split('/')[0]
            table_name = data_source.split('/')[1]
            data = ETL.__extract_from_sqlite(db, table_name)
        elif source_type == 'MSSQL':
            data = ETL.__extract_from_mssql(data_source)
        elif source_type == 'HTML':
            data = ETL.__extract_from_html(data_source)
        elif source_type == 'JSON':
            data = ETL.__extract_from_json(data_source)
        elif source_type == 'XML':
            data = ETL.__extract_from_xml(data_source)

        else:
            raise Exception(f'Unsupported data source')
        
        return data


    @staticmethod
    def transform(data:pd.DataFrame, criteria:dict) -> pd.DataFrame:
        # filtering
        if criteria['FILTER']:
            data = ETL.__filter(data, criteria['FILTER'])

        # columns
        if criteria['COLUMNS'] != '__all__':
            data = data.filter(items=criteria['COLUMNS'])

        # distinct
        if criteria['DISTINCT']:
            data = data.drop_duplicates()

        # ordering
        if criteria['ORDER']:
            column = criteria['ORDER'][0]
            data = data.sort_values(column, ascending=criteria['ORDER'][1] == 'ASC')

        # limit
        if criteria['LIMIT']:
            data = data[:criteria['LIMIT']]

        return data


    @staticmethod
    def load(data:pd.DataFrame, data_destination:str):
        source_type = ETL.__get_source_type(data_destination)
        if source_type == 'CSV':
            ETL.__load_to_csv(data, data_destination)
        elif source_type == 'SQLITE':
            db_destination = data_destination.split('/')[0]
            table_name = data_destination.split('/')[1]
            ETL.__load_to_sqlite(data, db_destination, table_name)
        elif source_type == 'MSSQL':
            ETL.__load_to_mssql(data, data_destination)
        elif source_type == 'HTML':
            ETL.__load_to_html(data, data_destination)
        elif source_type == 'JSON':
            ETL.__load_to_json(data, data_destination)
        elif source_type == 'XML':
            ETL.__load_to_xml(data, data_destination)
        elif source_type == 'CONSOL':
            print(data)
        else:
            raise Exception(f'Unsupported data destination')

    
    # Not finished
    @staticmethod
    def insert_into(data_destination:str, column_list:Union(list, None), values:list):
        pass


    # Not finished
    @staticmethod
    def update(data_destination:str, set:list, where:dict):
        pass


    # Not finished
    @staticmethod
    def delete_from(data_destination:str, where:dict):
        pass


    def __get_source_type(data_source:str) -> str:
        if data_source == None:
            return 'CONSOL'
        elif re.search(r'.*\.csv(\.zip)?', data_source):   
            return 'CSV'
        elif re.search(r'.*\.db/\w+', data_source):
            return 'SQLITE'
        elif re.search(r'Data Source.*', data_source):
            return 'MSSQL'
        elif re.search(r'.*\.html', data_source):   
            return 'HTML'
        elif re.search(r'.*\.json', data_source):   
            return 'JSON'
        elif re.search(r'.*\.xml', data_source):   
            return 'XML'


    def __extract_from_csv(data_source) -> pd.DataFrame:
        data = pd.read_csv(data_source)
        return data

        
    def __extract_from_sqlite(ETL, db_file_path, table_name) -> pd.DataFrame:
        sqlite_engine = sqlalchemy.create_engine(f'sqlite:///{db_file_path}')
        data = pd.read_sql(f'select * from {table_name}', sqlite_engine)
        return data


    # Not Finished
    def __extract_from_mssql(connection_string) -> pd.DataFrame:
        mssql_engine = sqlalchemy.create_engine(f'mssql+pyodbc://{"server_name"}/{"mssql_db_name"}?trusted_connection=yes&driver=SQL+Server+Native+Client+11.0')
        table = mssql_engine.execute(f"SELECT * FROM {'table_name'};")
        data = pd.DataFrame(table, columns=table.keys())
        return data

    def __extract_from_html(self, connection_string) -> pd.DataFrame:
        data = pd.read_html(connection_string)
        return data[0]

    def __extract_from_json(self, connection_string) -> pd.DataFrame:
        data = pd.read_json(connection_string, orient='records')
        return data

    def __extract_from_xml(self, connection_string) -> pd.DataFrame:
        data = pd.read_xml(connection_string)
        return data




    def __filter(data:pd.DataFrame, filters:dict) -> pd.DataFrame:
        left = filters['left']
        right = filters['right'] 

        if filters["type"] == 'or' or filters["type"] == 'and':
            left = ETL.__filter(data, left)
            right = ETL.__filter(data, right)

            if filters["type"] == 'or':
                data = pd.concat([left, right])
            elif filters["type"] == 'and':
                data = pd.merge(left, right)
            data = data[~data.index.duplicated(keep='first')]

        elif filters["type"] == 'like':
            data = data[[True if re.match(right, str(x)) else False for x in data[left]]]
        elif filters["type"] == '>':
            data = data[data[left] > right]
        elif filters["type"] == '>=':
            data = data[data[left] >= right]
        elif filters["type"] == '<':
            data = data[data[left] < right]
        elif filters["type"] == '<=':
            data = data[data[left] <= right]
        elif filters["type"] == '==':
            data = data[data[left] == str(right).lower()]
        elif filters["type"] == '!=':
            data = data[data[left] != right]

        return data


    def __load_to_csv(data, csv_file_path):
        data.to_csv(csv_file_path + ".csv", header=None, mode='a')


    def __load_to_sqlite(data, db_file_path, table_name):
        sqlite_engine = sqlalchemy.create_engine(f'sqlite:///{db_file_path}')
        data.to_sql(table_name, sqlite_engine, if_exists='append', index=False)


    # Not Finished
    def __load_to_mssql(self, data, connection_string):
        mssql_engine = sqlalchemy.create_engine(f'mssql+pyodbc://{"server_name"}/{"mssql_db_name"}?trusted_connection=yes&driver=SQL+Server+Native+Client+11.0')
        data.to_sql("table_name", mssql_engine, if_exists='append', index=False)

    def __load_to_json(self, data, connection_string):
        data.to_json(connection_string)

    def __load_to_html(self, data, connection_string):
        data.to_html(connection_string)

    def __load_to_xml(self, data, connection_string):
        data.to_xml(connection_string)


