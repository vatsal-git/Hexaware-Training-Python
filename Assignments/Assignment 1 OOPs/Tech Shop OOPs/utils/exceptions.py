import logging

# Configure logging
logging.basicConfig(filename='../logs/error.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')


class InvalidIDError(Exception):
    def __init__(self, message="Invalid ID"):
        self.message = message
        super().__init__(self.message)
        logging.error(message, exc_info=True)


class InvalidStringError(Exception):
    def __init__(self, message="Invalid String."):
        self.message = message
        super().__init__(self.message)
        logging.error(message, exc_info=True)


class InvalidEmailError(Exception):
    def __init__(self, message="Invalid Email."):
        self.message = message
        super().__init__(self.message)
        logging.error(message, exc_info=True)


class InvalidPhoneError(Exception):
    def __init__(self, message="Invalid Phone."):
        self.message = message
        super().__init__(self.message)
        logging.error(message, exc_info=True)


class InvalidListError(Exception):
    def __init__(self, message="Invalid List."):
        self.message = message
        super().__init__(self.message)
        logging.error(message, exc_info=True)


class InvalidNumberError(Exception):
    def __init__(self, message="Invalid Number."):
        self.message = message
        super().__init__(self.message)
        logging.error(message, exc_info=True)


class InvalidDateError(Exception):
    def __init__(self, message="Invalid Date."):
        self.message = message
        super().__init__(self.message)
        logging.error(message, exc_info=True)


class InvalidInstanceError(Exception):
    def __init__(self, message="Invalid Instance."):
        self.message = message
        super().__init__(self.message)
        logging.error(message, exc_info=True)


class InvalidEnumError(Exception):
    def __init__(self, message="Invalid Enum."):
        self.message = message
        super().__init__(self.message)
        logging.error(message, exc_info=True)


class InsufficientStockException(Exception):
    def __init__(self, message="Insufficient Stock."):
        self.message = message
        super().__init__(self.message)
        logging.error(message, exc_info=True)


class IncompleteOrderException(Exception):
    def __init__(self, message="Order detail requires order and product objects."):
        self.message = message
        super().__init__(self.message)
        logging.error(message, exc_info=True)


class PaymentFailedException(Exception):
    def __init__(self, message="There was an issue with the payment."):
        self.message = message
        super().__init__(self.message)
        logging.error(message, exc_info=True)


class IOException(Exception):
    def __init__(self, message="Error occurred in data persistence."):
        self.message = message
        super().__init__(self.message)
        logging.error(message, exc_info=True)


class SqlException(Exception):
    def __init__(self, message="Error occurred in database or SQL."):
        self.message = message
        super().__init__(self.message)
        logging.error(message, exc_info=True)


class ConcurrencyException(Exception):
    def __init__(self, message="Data conflict/concurrency occurred."):
        self.message = message
        super().__init__(self.message)
        logging.error(message, exc_info=True)


class AuthenticationException(Exception):
    def __init__(self, message="Unauthorized Access."):
        self.message = message
        super().__init__(self.message)
        logging.error(message, exc_info=True)
