from entities.Event import Event


class Concert(Event):
    def __init__(self, event_name, event_date, artist, concert_type, customer=None):
        super().__init__(event_name, event_date, customer)
        self.artist = artist
        self.concert_type = concert_type

    def display_event_details(self):
        super().display_event_details()
        print(f"Artist: {self.artist}")
        print(f"Concert Type: {self.concert_type}")