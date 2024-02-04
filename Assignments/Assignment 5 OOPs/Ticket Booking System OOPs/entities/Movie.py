from entities.Event import Event


class Movie(Event):
    def __init__(self, event_name, event_date, genre, actor_name, actress_name, customer=None):
        super().__init__(event_name, event_date, customer)
        self.genre = genre
        self.actor_name = actor_name
        self.actress_name = actress_name

    def display_event_details(self):
        super().display_event_details()
        print(f"Genre: {self.genre}")
        print(f"Actor: {self.actor_name}")
        print(f"Actress: {self.actress_name}")