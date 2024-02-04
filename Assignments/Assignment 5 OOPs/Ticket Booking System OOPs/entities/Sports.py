from entities.Event import Event


class Sports(Event):
    def __init__(self, event_name, event_date, sport_name, teams_name, customer=None):
        super().__init__(event_name, event_date, customer)
        self.sport_name = sport_name
        self.teams_name = teams_name

    def display_event_details(self):
        super().display_event_details()
        print(f"Sport Name: {self.sport_name}")
        print(f"Teams: {self.teams_name}")