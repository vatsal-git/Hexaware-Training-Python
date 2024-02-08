from datetime import datetime
import mysql.connector

from exceptions.AdminNotFoundException import AdminNotFoundException
from exceptions.DatabaseConnectionException import DatabaseConnectionException
from interfaces.IAdminService import IAdminService
from entities.Admin import Admin
from utils.Validator import InputValidator


class AdminService(IAdminService):
    def __init__(self, db_context):
        self.db_context = db_context

    def get_admin_by_id(self, admin_id):
        query = "SELECT * FROM Admin WHERE AdminID = %s"
        params = (admin_id,)

        try:
            cursor, connection = self.db_context.execute_query(query, params)
            fetched_admin = cursor.fetchone()

            if fetched_admin:
                return Admin(*fetched_admin)
            else:
                return None
        except mysql.connector.Error as err:
            raise DatabaseConnectionException(f"Error getting admin: {err}")

    def get_admin_by_username(self, username):
        query = "SELECT * FROM Admin WHERE Username = %s"
        params = (username,)

        try:
            cursor, connection = self.db_context.execute_query(query, params)
            fetched_admin = cursor.fetchone()

            if fetched_admin:
                return Admin(*fetched_admin)
            else:
                return None
        except mysql.connector.Error as err:
            raise DatabaseConnectionException(f"Error getting admin: {err}")

    def register_admin(self, admin_data):
        InputValidator.validate_email(admin_data['Email'])
        InputValidator.validate_phone(admin_data['PhoneNumber'])

        query = "INSERT INTO Admin (FirstName, LastName, Email, PhoneNumber, Username, Password, Role, JoinDate) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        params = (
            admin_data['FirstName'],
            admin_data['LastName'],
            admin_data['Email'],
            admin_data['PhoneNumber'],
            admin_data['Username'],
            admin_data['Password'],
            'Admin',
            datetime.now()
        )

        try:
            cursor, connection = self.db_context.execute_query(query, params)
            connection.commit()
        except mysql.connector.Error as err:
            raise DatabaseConnectionException(f"Error creating admin: {err}")

    def update_admin(self, admin_data):
        self.get_admin_by_id(admin_data['AdminID'])  # Validate if admin exists
        query = "UPDATE Admin SET FirstName = %s, LastName = %s, Email = %s, PhoneNumber = %s WHERE AdminID = %s"
        params = (
            admin_data['FirstName'],
            admin_data['LastName'],
            admin_data['Email'],
            admin_data['PhoneNumber'],
            admin_data['AdminID']
        )
        self.db_context.execute_query(query, params)

    def delete_admin(self, admin_id):
        self.get_admin_by_id(admin_id)   # Validate if admin exists
        query = "DELETE FROM Admin WHERE AdminID = %s"
        params = (admin_id,)
        self.db_context.execute_query(query, params)
