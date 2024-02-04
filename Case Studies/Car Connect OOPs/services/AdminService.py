from exceptions.AdminNotFoundException import AdminNotFoundException
from interfaces.IAdminService import IAdminService
from entities.Admin import Admin
from datetime import datetime


class AdminService(IAdminService):
    def __init__(self, db_context):
        self.db_context = db_context

    def get_admin_by_id(self, admin_id):
        query = "SELECT * FROM Admin WHERE AdminID = %s"
        params = (admin_id,)
        result = self.db_context.execute_query(query, params)
        if result:
            return Admin(**result[0])
        else:
            raise AdminNotFoundException()

    def get_admin_by_username(self, username):
        query = "SELECT * FROM Admin WHERE Username = %s"
        params = (username,)
        result = self.db_context.execute_query(query, params)
        if result:
            return Admin(*result[0])
        else:
            raise AdminNotFoundException()

    def register_admin(self, admin_data):
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
        self.db_context.execute_query(query, params)

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
