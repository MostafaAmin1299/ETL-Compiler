import pandas as pd
import sqlalchemy

def __load_to_csv(data, csv_file_path):
    data.to_csv(csv_file_path + ".csv", header=None, mode='a')


def __load_to_sqlite(data, db_file_path, table_name):
    sqlite_engine = sqlalchemy.create_engine(f'sqlite:///{db_file_path}')
    data.to_sql(table_name, sqlite_engine, if_exists='append', index=False)


# Not Finished
def __load_to_mssql(data, connection_string):
    mssql_engine = sqlalchemy.create_engine(f'mssql+pyodbc://{"server_name"}/{"mssql_db_name"}?trusted_connection=yes&driver=SQL+Server+Native+Client+11.0')
    data.to_sql("table_name", mssql_engine, if_exists='append', index=False)

def __load_to_json(data, connection_string):
    data.to_json(connection_string)

def __load_to_html(data, connection_string):
    data.to_html(connection_string)

def __load_to_xml(data, connection_string):
    data.to_xml(connection_string)