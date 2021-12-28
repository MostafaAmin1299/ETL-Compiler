import pandas as pd
import sqlalchemy

def __extract_from_csv(data_source) -> pd.DataFrame:
    data = pd.read_csv(data_source)
    return data

    
def __extract_from_sqlite(db_file_path, table_name) -> pd.DataFrame:
    sqlite_engine = sqlalchemy.create_engine(f'sqlite:///{db_file_path}')
    data = pd.read_sql(f'select * from {table_name}', sqlite_engine)
    return data


def __extract_from_mssql(connection_string:str) -> pd.DataFrame:
    connection_string = connection_string.split("/")
    server_name = connection_string[0]
    mssql_db_name = connection_string[1]
    table_name = connection_string[2]
    mssql_engine = sqlalchemy.create_engine(f'mssql+pyodbc://{server_name}/{mssql_db_name}?trusted_connection=yes&driver=SQL+Server+Native+Client+11.0')
    table = mssql_engine.execute(f"SELECT * FROM {table_name};")
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