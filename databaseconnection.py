import psycopg2


class DatabaseConnector:
    def __init__(self, db_url=None, username=None, password=None, host=None, port=None, database=None):
        self.db_url = db_url
        self.username = username
        self.password = password
        self.host = host
        self.port = port
        self.database = database
        self.connection = None

    def connect(self):
        if self.db_url:
            self.connection = psycopg2.connect(self.db_url)
        else:
            self.connection = psycopg2.connect(
                user=self.username,
                password=self.password,
                host=self.host,
                port=self.port,
                database=self.database,
            )
        return self.connection

    def close(self):
        if self.connection:
            self.connection.close()

# ins=DatabaseConnector(username="postgres",password="password",host="localhost",port="5432",database="database_name")
# cur=ins.connect().cursor()
# cur.execute("CREATE TABLE movie (title VARCHAR(255), year INT,score FLOAT);")

