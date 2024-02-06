class ProductCreationError(Exception):
    def __init__(self, message="Product Creation Error"):
        self.message = message
        super().__init__(self.message)