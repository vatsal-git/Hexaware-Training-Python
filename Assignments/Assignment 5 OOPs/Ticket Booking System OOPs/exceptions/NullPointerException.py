class NullPointerException(Exception):
    def __init__(self, message="Null pointer exception"):
        self.message = message
        super().__init__(self.message)