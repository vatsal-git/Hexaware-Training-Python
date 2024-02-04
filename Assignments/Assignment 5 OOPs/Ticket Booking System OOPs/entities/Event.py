from datetime import datetime
from entities.Venue import Venue


class Event(Venue):
    def __init__(self, event_name, event_date, event_time, venue, total_seats, available_seats, ticket_price, event_type):
        self._event_name = event_name
        self._event_date = datetime.strptime(event_date, "%Y-%m-%d").date()
        self._event_time = datetime.strptime(event_time, "%H:%M").time()
        self._venue_name = venue.venue_name
        self._total_seats = total_seats
        self._available_seats = available_seats
        self._ticket_price = ticket_price
        self._event_type = event_type

    @property
    def event_name(self):
        return self._event_name

    @event_name.setter
    def event_name(self, value):
        self._event_name = value

    @property
    def event_date(self):
        return self._event_date

    @event_date.setter
    def event_date(self, value):
        self._event_date = value

    @property
    def event_time(self):
        return self._event_time

    @event_time.setter
    def event_time(self, value):
        self._event_time = value

    @property
    def venue_name(self):
        return self._venue_name

    @venue_name.setter
    def venue_name(self, value):
        self._venue_name = value

    @property
    def total_seats(self):
        return self._total_seats

    @total_seats.setter
    def total_seats(self, value):
        self._total_seats = value

    @property
    def available_seats(self):
        return self._available_seats

    @available_seats.setter
    def available_seats(self, value):
        self._available_seats = value

    @property
    def ticket_price(self):
        return self._ticket_price

    @ticket_price.setter
    def ticket_price(self, value):
        self._ticket_price = value

    @property
    def event_type(self):
        return self._event_type

    @event_type.setter
    def event_type(self, value):
        self._event_type = value

    def calculate_total_revenue(self):
        return self._ticket_price * (self._total_seats - self._available_seats)

    def get_booked_tickets_count(self):
        return self._total_seats - self._available_seats

    def book_ticket(self, num_tickets):
        self._available_seats = self._available_seats - num_tickets

    def cancel_booking(self, num_tickets):
        self._available_seats = self._available_seats + num_tickets

    def display_event_details(self):
        print(f"Event name = {self._event_name}")
        print(f"Date of event = {self._event_date}")
        print(f"Time of event = {self._event_time}")
        print(f"Venue name = {self._venue_name}")
        print(f"Available Seats = {self._available_seats}")
