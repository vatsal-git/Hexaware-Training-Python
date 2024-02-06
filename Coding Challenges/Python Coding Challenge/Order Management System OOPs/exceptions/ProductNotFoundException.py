class ProductNotFoundException(Exception):
    def __init__(self, message="Product Not Found Exception"):
        self.message = message
        super().__init__(self.message)