import mysql.connector
import time
import configparser


class DBUtil:
    @staticmethod
    def getDBConn(max_retries=3, retry_delay=2):
        config = configparser.ConfigParser()
        config.read('../config.ini')
        database_config = config['Database']

        for attempt in range(1, max_retries + 1):
            try:
                connection = mysql.connector.connect(
                    host=database_config['host'],
                    user=database_config['user'],
                    password=database_config['password'],
                    database=database_config['database']
                )
                return connection
            except mysql.connector.Error as err:
                print(f"Error: {err}")
                if attempt < max_retries:
                    print(f"Retrying connection (Attempt {attempt}/{max_retries})...")
                    time.sleep(retry_delay)
                else:
                    print(f"Max retries reached. Unable to establish a connection.")
                    return None
