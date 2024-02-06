class ProductRetrievalError(Exception):
    def __init__(self, message="Product Retrieval Error"):
        self.message = message
        super().__init__(self.message)