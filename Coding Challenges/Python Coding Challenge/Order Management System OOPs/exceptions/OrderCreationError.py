class OrderCreationError(Exception):
    def __init__(self, message="Order Creation Error"):
        self.message = message
        super().__init__(self.message)