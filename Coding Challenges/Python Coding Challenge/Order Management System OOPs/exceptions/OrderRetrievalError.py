class OrderRetrievalError(Exception):
    def __init__(self, message="Order Retrieval Error"):
        self.message = message
        super().__init__(self.message)