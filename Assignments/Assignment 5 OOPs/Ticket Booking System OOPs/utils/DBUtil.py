from mysql import connector
import mysql


class DBUtil:
    def __init__(self):
        self.con = mysql.connector.connect(
            host="localhost",
            port="3306",
            user="root",
            password="root",
            database="ticketbookingsystem"
        )

    def get_cursor(self):
        return self.con.cursor()
