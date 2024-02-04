class Customer:
    def __init__(self, customer_name, email, phone):
        self._customer_name = customer_name
        self._email = email
        self._phone = phone

    @property
    def customer_name(self):
        return self._customer_name

    @customer_name.setter
    def customer_name(self, value):
        self._customer_name = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value

    def display_customer_details(self):
        print(f"Customer Name: {self._customer_name}")
        print(f"Email: {self._email}")
        print(f"Phone Number: {self._phone}")
