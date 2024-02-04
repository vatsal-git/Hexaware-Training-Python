import re
from exceptions.InvalidInputException import InvalidInputException


class InputValidator:
    @staticmethod
    def validate_string(value, field_name):
        if not value or not isinstance(value, str):
            raise InvalidInputException(f"{field_name} must be a non-empty string.")

    @staticmethod
    def validate_number(value, field_name):
        if not value or not isinstance(value, (int, float)):
            raise InvalidInputException(f"{field_name} must be a number.")

    @staticmethod
    def validate_email(value, field_name):
        email_regex = r'^\S+@\S+\.\S+$'
        if not value or not re.match(email_regex, value):
            raise InvalidInputException(f"Invalid {field_name} format.")
