import mysql.connector
import time
from utils.exceptions import SqlException


class DatabaseServices:
    def __init__(self, host, user, password, database_name):
        self.host = host
        self.user = user
        self.password = password
        self.database_name = database_name
        self.connection = None
        self.cursor = None

    def connect(self, max_retries=3, retry_delay=5):
        print("\nConnecting to database...")
        retries = 0
        while retries < max_retries:
            try:
                self.connection = mysql.connector.connect(
                    host=self.host,
                    user=self.user,
                    password=self.password,
                    database=self.database_name
                )
                self.cursor = self.connection.cursor()
                print(f"Connected to database: {self.database_name}")
                return  # Connection successful, exit the loop
            except mysql.connector.Error as ex:
                print(f"Error connecting to the database: {ex}")
                retries += 1
                print(f"Retrying connection ({retries}/{max_retries})...")
                time.sleep(retry_delay)

        raise SqlException("Max retries reached. Unable to connect to the database.")

    def disconnect(self):
        try:
            if self.cursor:
                self.cursor.close()
            if self.connection:
                self.connection.close()
            print("Disconnected from the database")
        except mysql.connector.Error as ex:
            raise SqlException(f"Error disconnecting from the database: {ex}")

    def execute_query(self, sql_query, params=None):
        try:
            if params:
                self.cursor.execute(sql_query, params)
            else:
                self.cursor.execute(sql_query)
            results = self.cursor.fetchall()
            self.connection.commit()
            return results
        except mysql.connector.Error as ex:
            raise SqlException(f"Error executing query: {ex}")

    def create_cursor(self):
        return self.connection.cursor()


# # EXAMPLE for Testing connection
# select_query = '''
# SELECT * FROM Orders WHERE CustomerID = %s;
# '''
#
# try:
#     db_services = DatabaseServices(
#         host='localhost',
#         user='root',
#         password='root',
#         database_name='techshop'
#     )
#
#     db_services.connect()
#     cursor = db_services.create_cursor()
#
#     customer_id_to_search = 1
#     cursor.execute(select_query, (customer_id_to_search,))
#     results = cursor.fetchall()
#
#     for row in results:
#         print(row)
#
#     cursor.close()
#     db_services.disconnect()
#
# except Exception as e:
#     print(f"An error occurred: {e}")
