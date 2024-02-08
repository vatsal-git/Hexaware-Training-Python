from datetime import datetime
import mysql.connector

from exceptions.CustomerNotFoundException import CustomerNotFoundException
from exceptions.DatabaseConnectionException import DatabaseConnectionException
from interfaces.ICustomerService import ICustomerService
from entities.Customer import Customer
from utils.Validator import InputValidator


class CustomerService(ICustomerService):
    def __init__(self, db_context):
        self.db_context = db_context

    def get_customer_by_id(self, customer_id):
        query = "SELECT * FROM Customer WHERE CustomerID = %s"
        params = (customer_id,)

        try:
            cursor, connection = self.db_context.execute_query(query, params)
            fetched_customer = cursor.fetchone()

            if fetched_customer:
                return Customer(*fetched_customer)
            else:
                return None
        except mysql.connector.Error as err:
            raise CustomerNotFoundException(f"Error getting customer: {err}")

    def get_customer_by_username(self, username):
        query = "SELECT * FROM Customer WHERE Username = %s"
        params = (username,)

        try:
            cursor, connection = self.db_context.execute_query(query, params)
            fetched_customer = cursor.fetchone()

            if fetched_customer:
                return Customer(*fetched_customer)
            else:
                return None
        except mysql.connector.Error as err:
            raise CustomerNotFoundException(f"Error getting customer: {err}")

    def register_customer(self, customer_data):
        InputValidator.validate_email(customer_data['Email'])
        InputValidator.validate_phone(customer_data['PhoneNumber'])

        query = "INSERT INTO Customer (FirstName, LastName, Email, PhoneNumber, Address, Username, Password, RegistrationDate) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        params = (
            customer_data['FirstName'],
            customer_data['LastName'],
            customer_data['Email'],
            customer_data['PhoneNumber'],
            customer_data['Address'],
            customer_data['Username'],
            customer_data['Password'],
            datetime.now()
        )

        try:
            cursor, connection = self.db_context.execute_query(query, params)
            connection.commit()
        except mysql.connector.Error as err:
            raise DatabaseConnectionException(f"Error creating customer: {err}")

    def update_customer(self, customer_data):
        self.get_customer_by_id(customer_data['CustomerID'])  # Validate if customer exists
        query = "UPDATE Customer SET FirstName = %s, LastName = %s, Email = %s, PhoneNumber = %s, Address = %s WHERE CustomerID = %s"
        params = (
            customer_data['FirstName'],
            customer_data['LastName'],
            customer_data['Email'],
            customer_data['PhoneNumber'],
            customer_data['Address'],
            customer_data['CustomerID']
        )
        self.db_context.execute_query(query, params)

    def delete_customer(self, customer_id):
        self.get_customer_by_id(customer_id)  # Validate if customer exists
        query = "DELETE FROM Customer WHERE CustomerID = %s"
        params = (customer_id,)
        self.db_context.execute_query(query, params)
