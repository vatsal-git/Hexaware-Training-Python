class InvalidBookingIDException(Exception):
    def __init__(self, message="Invalid Booking Id"):
        self.message = message
        super().__init__(self.message)