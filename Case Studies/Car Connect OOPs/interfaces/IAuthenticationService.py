from abc import ABC, abstractmethod


class IAuthenticationService(ABC):
    @abstractmethod
    def authenticate_customer(self, username, password):
        pass

    @abstractmethod
    def authenticate_admin(self, username, password):
        pass
