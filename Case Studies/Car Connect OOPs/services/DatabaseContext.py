import mysql.connector
import configparser
import time

from exceptions.DatabaseConnectionException import DatabaseConnectionException
from interfaces.IDatabaseContext import IDatabaseContext


class DatabaseContext(IDatabaseContext):
    def __init__(self, database='CarConnect'):
        # Reading database config from '../config.ini'
        config = configparser.ConfigParser()
        config.read('../config.ini')
        database_config = config['Database']

        self.host=database_config['host']
        self.user=database_config['user']
        self.password=database_config['password']
        self.database = database
        self.connection = None
        self.cursor = None

    def connect(self, max_retries=3, retry_delay=2):
        for attempt in range(1, max_retries + 1):
            try:
                self.connection = mysql.connector.connect(
                    host=self.host,
                    user=self.user,
                    password=self.password,
                    database=self.database
                )
                self.cursor = self.connection.cursor()
                print(f"Connected to the database: {self.database}")
                return self.connection
            except mysql.connector.Error as err:
                if attempt < max_retries:
                    print(f"Retrying connection (Attempt {attempt}/{max_retries})...")
                    time.sleep(retry_delay)
                else:
                    print(f"Max retries reached. Unable to establish a connection.")
                    raise DatabaseConnectionException(f"Error connecting to the database: {err}")

    def disconnect(self):
        try:
            if self.connection:
                self.connection.close()
                print("\nDisconnected from the database.")
        except mysql.connector.Error as e:
            raise DatabaseConnectionException(f"Error disconnecting from the database: {e}")

    def execute_query(self, query, values=None):
        try:
            if values:
                self.cursor.execute(query, values)
            else:
                self.cursor.execute(query)
            return self.cursor, self.connection
        except mysql.connector.Error as e:
            self.connection.rollback()
            raise DatabaseConnectionException(f"Error executing query: {e}")
