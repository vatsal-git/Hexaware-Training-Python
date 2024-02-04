from datetime import date
from exceptions.EventNotFoundException import EventNotFoundException
from exceptions.InvalidBookingIDException import InvalidBookingIDException
from interfaces.IBookingSystemServices import IBookingSystemServices


class BookingSystemServices(IBookingSystemServices):
    def __init__(self, dbutil):
        self.dbutil = dbutil

    def calculate_booking_cost(self, num_tickets):
        pass

    def book_tickets(self, num_tickets):
        # Take User Input
        print("\nPlease enter customer details: ")
        customer_name = input("Enter your name: ")
        customer_email = input("Enter you email: ")
        customer_phone = input("Enter your phone number: ")

        # Create Customer
        cursor = self.dbutil.get_cursor()
        cursor.execute("insert into customers(customer_name,email,phone_number) values (%s,%s,%s)",
                       (customer_name, customer_email, customer_phone,))
        cursor.fetchall()
        self.dbutil.con.commit()

        # Set Customer ID
        cursor.execute("select customer_id from customers where customer_name=%s", (customer_name,))
        cursor.fetchall()
        customer_row = cursor.fetchone()
        customer_id = -1
        if customer_row:
            customer_id = customer_row[0]

        # Print all Events
        print("\nSelect one event from the events list: ")
        cursor.execute("select event_name from events")
        events = cursor.fetchall()
        for event in events:
            print(event[0])

        # Select Event and Book Event
        name_of_event = input("\nEnter event name: ")
        cursor.execute("select event_id,ticket_price from events where event_name = %s", (name_of_event,))
        rows = cursor.fetchone()
        event_id = -1
        price = 0
        available_seats = 0
        if rows:
            event_id, price, available_seats = rows

        # See if tickets are available
        if available_seats < num_tickets:
            raise Exception('Not enough tickets available. Tickets available: ', available_seats)

        ticket_type = input("What type of ticket you want? - 1.Silver(x1) 2.Gold(x2) 3.Dimond(x3) ?")
        total_cost = price * num_tickets * ticket_type
        today = date.today()
        query = "insert into bookings (customer_id, event_id, num_tickets, total_cost, booking_date) values (%s,%s,%s,%s,%s)"
        cursor.execute(query, (customer_id, event_id, num_tickets, total_cost, today))

        result = cursor.fetchall()
        if result is None:
            raise EventNotFoundException()

        self.dbutil.con.commit()

        # Get Booking
        cursor.execute("select booking_id from bookings where customer_id = %s", (customer_id,))
        booking_id = cursor.fetchone()
        if booking_id:
            b_id = booking_id[0]
        print("\nCongratulations! Your booking is confirmed. Your booking id is ", b_id)

    def cancel_booking(self, booking_id):
        cursor = self.dbutil.get_cursor()
        query = "delete from bookings where booking_id = %s"
        cursor.execute(query, (booking_id,))

        result = cursor.fetchall()
        if result is None:
            raise InvalidBookingIDException()

        self.dbutil.con.commit()
        print("\nYour booking is cancelled successfully.")

    def get_booking_details(self, booking_id):
        pass
