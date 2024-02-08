import unittest
from exceptions.AuthenticationException import AuthenticationException
from services.AuthenticationService import AuthenticationService
from services.CustomerService import CustomerService
from services.DatabaseContext import DatabaseContext


class TestCustomerAuthentication(unittest.TestCase):
    def setUp(self):
        db_context = DatabaseContext()
        db_context.connect()
        self.customer_service = CustomerService(db_context)
        self.auth_service = AuthenticationService(self.customer_service)

    def test_invalid_credentials(self):
        invalid_username = "notvatsal"
        invalid_password = "notroot"

        with self.assertRaises(AuthenticationException) as context:
            self.auth_service.authenticate_customer(invalid_username, invalid_password)
        self.assertIn("Incorrect Username or Password", str(context.exception))

    def test_valid_credentials(self):
        valid_username = "vatsal"
        valid_password = "root"

        try:
            self.auth_service.authenticate_customer(valid_username, valid_password)
        except AuthenticationException as e:
            self.fail(f"Unexpected exception raised: {e}")


if __name__ == '__main__':
    unittest.main()
