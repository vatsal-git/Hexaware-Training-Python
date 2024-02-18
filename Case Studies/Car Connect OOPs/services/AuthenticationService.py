from exceptions.AuthenticationException import AuthenticationException
from interfaces.IAuthenticationService import IAuthenticationService
from services.AdminService import AdminService
from services.CustomerService import CustomerService


class AuthenticationService(IAuthenticationService, CustomerService, AdminService):
    def __init__(self, db_context):
        super().__init__(db_context)

    def authenticate_customer(self, username, password):
        customer = self.get_customer_by_username(username)
        if not customer or not customer.authenticate(password):
            raise AuthenticationException("Incorrect Username or Password")
        return customer

    def authenticate_admin(self, username, password):
        admin = self.get_admin_by_username(username)
        if not admin or not admin.authenticate(password):
            raise AuthenticationException("Incorrect Username or Password")
        return admin
