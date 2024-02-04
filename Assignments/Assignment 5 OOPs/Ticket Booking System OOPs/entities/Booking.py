import random
from datetime import date
from entities.Event import Event


class Booking(Event):
    def __init__(self, event, customer):
        self._booking_id = random.randint(10000, 99999)
        self._customer = customer
        self._event = event
        self._num_tickets = len(customer)
        self._total_cost = 0
        self._booking_date = date.today()

    @property
    def booking_id(self):
        return self._booking_id

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, value):
        self._customer = value

    @property
    def event(self):
        return self._event

    @event.setter
    def event(self, value):
        self._event = value

    @property
    def num_tickets(self):
        return self._num_tickets

    @num_tickets.setter
    def num_tickets(self, value):
        self._num_tickets = value

    @property
    def total_cost(self):
        return self._total_cost

    @total_cost.setter
    def total_cost(self, value):
        self._total_cost = value

    @property
    def booking_date(self):
        return self._booking_date

    @booking_date.setter
    def booking_date(self, value):
        self._booking_date = value

    def calculate_booking_cost(self, num_tickets):
        pass

    def book_tickets(self, num_tickets):
        super().book_ticket(num_tickets)

    def cancel_booking(self, num_tickets):
        super().cancel_booking(num_tickets)

    def get_available_tickets_count(self):
        return self._event.available_seats

    def get_event_details(self):
        pass
