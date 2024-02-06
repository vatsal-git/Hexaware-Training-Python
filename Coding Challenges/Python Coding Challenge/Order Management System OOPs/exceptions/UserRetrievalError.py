class UserRetrievalError(Exception):
    def __init__(self, message="User Retrieval Error"):
        self.message = message
        super().__init__(self.message)