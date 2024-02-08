import re
from exceptions.InvalidInputException import InvalidInputException


class InputValidator:
    @staticmethod
    def validate_email(value):
        email_regex = r'^\S+@\S+\.\S+$'
        if not value or not re.match(email_regex, value):
            raise InvalidInputException(f"Invalid Email format.")

    @staticmethod
    def validate_phone(value):
        phone_number_regex = r'^\d{10}$'
        if not value or not re.match(phone_number_regex, value):
            raise InvalidInputException(f"Invalid Phone Number. It should be of 10-digit.")
