from exceptions.EventNotFoundException import EventNotFoundException
from exceptions.InvalidBookingIDException import InvalidBookingIDException
from exceptions.NullPointerException import NullPointerException
from services.BookingSystemServices import BookingSystemServices
from services.EventServices import EventServices
from utils.DBUtil import DBUtil


class TicketBookingSystem(EventServices, BookingSystemServices):
    def __init__(self, new_dbutil):
        super().__init__(new_dbutil)

    def main_menu(self):
        while True:
            print("\nSelect one options from the options given below : ")
            print("1. Create a new event.")
            print("2. Book tickets.")
            print("3. Cancel Tickets.")
            print("4. Know how many seats are Available.")
            print("5. See every event and it's details.")
            print("6. Exit.")
            choice = input("Enter your choice here : ")

            try:
                match choice:
                    case "1":
                        self.create_event()
                        print()
                    case "2":
                        num_tickets = int(input("\nPlease enter the number of tickets you want to book : "))
                        self.book_tickets(num_tickets)
                        print()
                    case "3":
                        booking_id = int(input("\nPlease enter your booking id here : "))
                        self.cancel_booking(booking_id)
                        print()
                    case "4":
                        self.get_available_tickets_count()
                        print()
                    case "5":
                        self.get_event_details()
                        print()
                    case "6":
                        break
                    case _:
                        print("Invalid input! Please Try Again.")
            except EventNotFoundException as e1:
                print("EventNotFoundException Exception occurred: ", e1)
            except InvalidBookingIDException as e2:
                print("InvalidBookingIDException Exception occurred: ", e2)
            except NullPointerException as e3:
                print("NullPointerException Exception occurred: ", e3)
            except Exception as ex:
                print("Exception occurred: ", ex)


if __name__ == "__main__":
    dbutil = DBUtil()
    events = TicketBookingSystem(dbutil)
    events.main_menu()
