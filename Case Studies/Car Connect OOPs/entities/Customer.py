class Customer:
    def __init__(self, customer_id, first_name, last_name, email, phone_number, address, username, password, registration_date):
        self.__CustomerID = customer_id
        self.__FirstName = first_name
        self.__LastName = last_name
        self.__Email = email
        self.__PhoneNumber = phone_number
        self.__Address = address
        self.__Username = username
        self.__Password = password
        self.__RegistrationDate = registration_date

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
    def phone_number(self):
        return self.__PhoneNumber

    @property
    def address(self):
        return self.__Address

    @property
    def username(self):
        return self.__Username

    @property
    def password(self):
        return self.__Password

    @property
    def registration_date(self):
        return self.__RegistrationDate

    # Setter methods with @<property_name>.setter decorator

    @customer_id.setter
    def customer_id(self, customer_id):
        self.__CustomerID = customer_id

    @first_name.setter
    def first_name(self, first_name):
        self.__FirstName = first_name

    @last_name.setter
    def last_name(self, last_name):
        self.__LastName = last_name

    @email.setter
    def email(self, email):
        self.__Email = email

    @phone_number.setter
    def phone_number(self, phone_number):
        self.__PhoneNumber = phone_number

    @address.setter
    def address(self, address):
        self.__Address = address

    @username.setter
    def username(self, username):
        self.__Username = username

    @password.setter
    def password(self, password):
        self.__Password = password

    @registration_date.setter
    def registration_date(self, registration_date):
        self.__RegistrationDate = registration_date

    def authenticate(self, password):
        return self.__Password == password

    def show_details(self):
        print(f"Customer ID: {self.customer_id} | Username: {self.username}")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Email: {self.email} | Phone Number: {self.phone_number}")
        print(f"Address: {self.address}")
        print(f"Registration Date: {self.registration_date}")
