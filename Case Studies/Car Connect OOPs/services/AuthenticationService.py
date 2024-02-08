from exceptions.AuthenticationException import AuthenticationException
from interfaces.IAuthenticationService import IAuthenticationService


class AuthenticationService(IAuthenticationService):
    def __init__(self, customer_service=None, admin_service=None):
        self.customer_service = customer_service
        self.admin_service = admin_service

    def authenticate_customer(self, username, password):
        customer = self.customer_service.get_customer_by_username(username)
        if not customer or not customer.authenticate(password):
            raise AuthenticationException("Incorrect Username or Password")
        return customer

    def authenticate_admin(self, username, password):
        admin = self.admin_service.get_admin_by_username(username)
        if not admin or not admin.authenticate(password):
            raise AuthenticationException("Incorrect Username or Password")
        return admin
