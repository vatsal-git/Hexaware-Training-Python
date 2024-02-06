class UserCreationError(Exception):
    def __init__(self, message="User Creation Error"):
        self.message = message
        super().__init__(self.message)