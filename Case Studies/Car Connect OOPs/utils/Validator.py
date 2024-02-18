import re
from exceptions.InvalidInputException import InvalidInputException


class InputValidator:
    @staticmethod
    def validate_email(value):
        email_regex = r'^\S+@\S+\.\S+$'
        if not value or not re.match(email_regex, value):
            raise InvalidInputException("Invalid Email format.")

    @staticmethod
    def validate_phone(value):
        phone_number_regex = r'^\d{10}$'
        if not value or not re.match(phone_number_regex, value):
            raise InvalidInputException("Invalid Phone Number. It should be of 10-digit.")

    @staticmethod
    def validate_username(value):
        username_regex = r'^[a-zA-Z](?:[a-zA-Z0-9]{0,19})?$'
        if not value or not re.match(username_regex, value):
            raise InvalidInputException("Invalid Username. It should contain only alphanumeric characters and be between 4 to 20 characters without white-space.")
