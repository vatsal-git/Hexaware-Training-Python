from datetime import datetime

from exceptions.CustomerNotFoundException import CustomerNotFoundException
from interfaces.ICustomerService import ICustomerService
from entities.Customer import Customer
from utils.Validator import InputValidator


class CustomerService(ICustomerService):
    def __init__(self, db_context):
        self.db_context = db_context

    def get_customer_by_id(self, customer_id):
        query = "SELECT * FROM Customer WHERE CustomerID = %s"
        params = (customer_id,)
        result = self.db_context.execute_query(query, params)
        if result:
            return Customer(*result[0])
        else:
            raise CustomerNotFoundException()

    def get_customer_by_username(self, username):
        query = "SELECT * FROM Customer WHERE Username = %s"
        params = (username,)
        result = self.db_context.execute_query(query, params)
        if result:
            return Customer(*result[0])
        else:
            raise CustomerNotFoundException()

    def register_customer(self, customer_data):
        InputValidator.validate_string(customer_data['FirstName'], "First Name")
        InputValidator.validate_string(customer_data['LastName'], "Last Name")
        InputValidator.validate_email(customer_data['Email'], "Email")
        InputValidator.validate_string(customer_data['PhoneNumber'], "Phone Number")
        InputValidator.validate_string(customer_data['Address'], "Address")
        InputValidator.validate_string(customer_data['Username'], "Username")
        InputValidator.validate_string(customer_data['Password'], "Password")

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
        self.db_context.execute_query(query, params)

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
