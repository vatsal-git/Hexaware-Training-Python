class OrderProcessorException(Exception):
    def __init__(self, message="Order Processing Exception"):
        self.message = message
        super().__init__(self.message)