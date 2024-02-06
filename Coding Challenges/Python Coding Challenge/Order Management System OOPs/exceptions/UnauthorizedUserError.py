class UnauthorizedUserError(Exception):
    def __init__(self, message="Unauthorized User Error"):
        self.message = message
        super().__init__(self.message)