class UserNotFoundException(Exception):
    def __init__(self, message="User Not Found Exception"):
        self.message = message
        super().__init__(self.message)