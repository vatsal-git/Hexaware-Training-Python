import mysql.connector

from exceptions.DatabaseConnectionException import DatabaseConnectionException


class DatabaseContext:
    def __init__(self, host='localhost', user='root', password='root', database='mydatabase'):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.connection.cursor()
            print(f"Connected to the database: {self.database}")
        except mysql.connector.Error as e:
            raise DatabaseConnectionException(f"Error connecting to the database: {e}")

    def disconnect(self):
        try:
            if self.connection:
                self.connection.close()
                print("Disconnected from the database.")
        except mysql.connector.Error as e:
            raise DatabaseConnectionException(f"Error disconnecting from the database: {e}")

    def execute_query(self, query, values=None):
        try:
            if values:
                self.cursor.execute(query, values)
            else:
                self.cursor.execute(query)
            results = self.cursor.fetchall()
            self.connection.commit()
            print("\n=> results =>", results)
            print("=> Query executed successfully.")
            return results
        except mysql.connector.Error as e:
            raise DatabaseConnectionException(f"Error executing query: {e}")

    def fetch_data(self, query, values=None):
        try:
            if values:
                self.cursor.execute(query, values)
            else:
                self.cursor.execute(query)
            data = self.cursor.fetchall()
            return data
        except mysql.connector.Error as e:
            raise DatabaseConnectionException(f"Error fetching data: {e}")

    def get_current_cursor(self):
        return self.cursor
