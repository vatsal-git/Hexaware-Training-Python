from utils.validations import (
    validate_id,
    validate_string,
    validate_email,
    validate_phone
)
from utils.exceptions import (
    InvalidIDError,
    InvalidStringError,
    InvalidEmailError,
    InvalidPhoneError
)


class Customer:
    def __init__(self, customer_id=None, first_name=None, last_name=None, email=None, phone=None, address=None, total_orders=None):
        self.__CustomerID = customer_id
        self.__FirstName = first_name
        self.__LastName = last_name
        self.__Email = email
        self.__Phone = phone
        self.__Address = address
        self.__TotalOrders = total_orders if total_orders else 0

    # Getter methods
    @property
    def customer_id(self):
        return self.__CustomerID

    @property
    def first_name(self):
        return self.__FirstName

    @property
    def last_name(self):
        return self.__LastName

    @property
    def email(self):
        return self.__Email

    @property
    def phone(self):
        return self.__Phone

    @property
    def address(self):
        return self.__Address

    @property
    def total_orders(self):
        return self.__TotalOrders

    # Setter methods
    @customer_id.setter
    def customer_id(self, new_customer_id):
        if validate_id(new_customer_id):
            self.__CustomerID = new_customer_id
        else:
            raise InvalidIDError("Customer ID should be a positive integer.")

    @first_name.setter
    def first_name(self, new_first_name):
        if validate_string(new_first_name, min_len=3):
            self.__FirstName = new_first_name
        else:
            raise InvalidStringError("First name should be at least 3 characters long.")

    @last_name.setter
    def last_name(self, new_last_name):
        if validate_string(new_last_name, min_len=3):
            self.__LastName = new_last_name
        else:
            raise InvalidStringError("Last name should be at least 3 characters long.")

    @email.setter
    def email(self, new_email):
        if validate_email(new_email):
            self.__Email = new_email
        else:
            raise InvalidEmailError("Invalid email format.")

    @phone.setter
    def phone(self, new_phone):
        if validate_phone(new_phone):
            self.__Phone = new_phone
        else:
            raise InvalidPhoneError("Invalid phone format.")

    @address.setter
    def address(self, new_address):
        if validate_string(new_address):
            self.__Address = new_address
        else:
            raise InvalidStringError("Address cannot be empty.")

    def calculate_total_orders(self):
        pass

    def get_customer_details(self):
        print(f"Customer ID: {self.customer_id}")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Phone: {self.phone}")
        print(f"Address: {self.address}")
        print(f"Total Orders: {self.total_orders}")

    def update_customer_info(self, new_email=None, new_phone=None, new_address=None):
        if new_email:
            self.email = new_email
        if new_phone:
            self.phone = new_phone
        if new_address:
            self.address = new_address
        print("Customer information updated successfully.")
