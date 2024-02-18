class Admin:
    def __init__(self, admin_id, first_name, last_name, email, phone_number, username, password, role, join_date):
        self.__AdminID = admin_id
        self.__FirstName = first_name
        self.__LastName = last_name
        self.__Email = email
        self.__PhoneNumber = phone_number
        self.__Username = username
        self.__Password = password
        self.__Role = role
        self.__JoinDate = join_date

    # Getter methods with @property decorator
    @property
    def admin_id(self):
        return self.__AdminID

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
    def username(self):
        return self.__Username

    @property
    def password(self):
        return self.__Password

    @property
    def role(self):
        return self.__Role

    @property
    def join_date(self):
        return self.__JoinDate

    # Setter methods with @<property_name>.setter decorator
    @admin_id.setter
    def admin_id(self, admin_id):
        self.__AdminID = admin_id

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

    @username.setter
    def username(self, username):
        self.__Username = username

    @password.setter
    def password(self, password):
        self.__Password = password

    @role.setter
    def role(self, role):
        self.__Role = role

    @join_date.setter
    def join_date(self, join_date):
        self.__JoinDate = join_date

    def authenticate(self, password):
        return self.__Password == password

    def show_details(self):
        print(f"Admin ID: {self.admin_id} | Username: {self.username}")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Email: {self.email} | Phone Number: {self.phone_number}")
        print(f"Role: {self.role}")
        print(f"Join Date: {self.join_date}")
