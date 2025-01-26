from  databaseconnection import DatabaseConnector
from createTables import create_table
columns = {
    "id": "SERIAL PRIMARY KEY",
    "name": "VARCHAR(100)",
    "age": "INTEGER"
}
ins=DatabaseConnector(username="postgres",password="password",host="localhost",port="5432",database="database_name")
cur=ins.connect()
create_table(cur,"person", columns)