import datetime

from interfaces.IEventServices import IEventServices


class EventServices(IEventServices):
    def __init__(self, dbutil):
        self.dbutil = dbutil

    def create_event(self):
        # Take User Input
        event_name = input("\nEnter event name: ")
        date = input("Enter event Date(Y-m-d): ")
        event_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
        time = input("Enter event time in format HH:MM:SS: ")
        event_time = datetime.datetime.strptime(time, "%H:%M:%S").time()
        venue = input("Enter venue name: ")
        venue_address = input("Enter venue address: ")
        total_seats = int(input("Enter total seats: "))
        available_seats = int(input("Enter available seats: "))
        ticket_price = float(input("Enter ticket price: "))
        event_type = input("Enter event type ['Movie','Sports','Concert']: ")

        # Create Venue
        cursor = self.dbutil.get_cursor()
        query = "insert into venues (venue_name, address) values (%s, %s)"
        cursor.execute(query, (venue, venue_address))
        self.dbutil.con.commit()

        # Get Venue ID for Event Creation
        cursor.execute("select venue_id from venues where venue_name=%s", (venue, ))
        venue_id = cursor.fetchone()

        # Create Event
        createEvent = ("insert into events (event_name,event_date,event_time,venue_id,total_seats,available_seats,ticket_price,event_type) values (%s,%s,%s,%s,%s,%s,%s,%s)")
        cursor.execute(createEvent, (event_name, event_date, event_time, venue_id[0], total_seats, available_seats, ticket_price, event_type, ))
        self.dbutil.con.commit()

        # Get Events
        cursor.execute("select * from events")
        events = cursor.fetchall()

        # Print all events
        for event in events:
            print(event[-1])

        print(f"\nEvent id for this event is {events[-1][0]}")
        print("Event created successfully.")

    def get_event_details(self):
        cursor = self.dbutil.get_cursor()
        cursor.execute("select * from events")
        events = cursor.fetchall()

        # Print all events
        for event in events:
            print(event)

    def get_available_tickets_count(self):
        cursor = self.dbutil.get_cursor()
        query = "select event_name from events"
        cursor.execute(query)
        event_names = cursor.fetchall()

        # Print all events
        print("\nPlease select one events from below: ")
        for event in event_names:
            print(event)

        # Get Tickets Count
        selected_event = input("\nPlease type your event name: ")
        query = "select available_seats from events where event_name=%s"
        cursor.execute(query, (selected_event, ))
        seats = cursor.fetchall()
        print("\nAvailable seats: ", seats)
