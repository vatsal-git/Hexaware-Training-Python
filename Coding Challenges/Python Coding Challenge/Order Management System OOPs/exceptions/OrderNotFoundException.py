class OrderNotFoundException(Exception):
    def __init__(self, message="Order Not Found Exception"):
        self.message = message
        super().__init__(self.message)