from datetime import datetime

from exceptions.InvalidInputException import InvalidInputException
from services.AdminService import AdminService
from services.AuthenticationService import AuthenticationService
from services.CustomerService import CustomerService
from services.DatabaseContext import DatabaseContext
from services.ReportGenerator import ReportGenerator
from services.ReservationService import ReservationService
from services.VehicleService import VehicleService
from utils.Constants import CMD_COLOR_YELLOW, CMD_COLOR_DEFAULT, CMD_COLOR_BLUE
from utils.Validator import InputValidator


class MainModule:
    def __init__(self, new_db_context):
        self.isAuthenticated = False
        self.isAdmin = False
        self.user_data = None
        self.customer_service = CustomerService(new_db_context)
        self.admin_service = AdminService(new_db_context)
        self.vehicle_service = VehicleService(new_db_context)
        self.reservation_service = ReservationService(new_db_context)
        self.auth_service = AuthenticationService(self.customer_service, self.admin_service)
        self.input_validator = InputValidator()
        self.report_generator = ReportGenerator(new_db_context)

    def main_menu(self):
        if not self.isAuthenticated:
            self.default_menu()
        elif self.isAuthenticated and not self.isAdmin:
            self.user_menu(self.user_data)
        elif self.isAuthenticated and self.isAdmin:
            self.admin_menu(self.user_data)

    def default_menu(self):
        while True:
            print(f"\n{CMD_COLOR_YELLOW}Auth Menu{CMD_COLOR_DEFAULT}")
            print("1. User Auth Options")
            print("2. Admin Auth Options")
            print("0. Exit")

            choice1 = int(input("Enter your choice: "))

            if choice1 == 0:
                break

            elif choice1 == 1:
                self.user_auth_menu()

            elif choice1 == 2:
                self.admin_auth_menu()

            else:
                print("Invalid choice. Please enter a valid option.")

    def user_auth_menu(self):
        while True:
            print(f"\n{CMD_COLOR_YELLOW}User Auth Options{CMD_COLOR_DEFAULT}")
            print("1. User Login")
            print("2. User Signup")
            print("0. Back to Main Menu")

            choice2 = int(input("Enter your choice: "))

            if choice2 == 0:
                break

            elif choice2 == 1:
                self.user_login()

            elif choice2 == 2:
                self.user_signup()

            else:
                print("Invalid choice. Please enter a valid option.")

    def user_login(self):
        try:
            username = input("\nEnter your username: ")
            password = input("Enter your password: ")
            user_data = self.auth_service.authenticate_customer(username, password)
            print(f"\n{CMD_COLOR_BLUE}Logged In Successfully!{CMD_COLOR_DEFAULT}")

            self.user_data = user_data
            self.isAuthenticated = True
            self.isAdmin = False

            self.user_menu(user_data)
        except Exception as e:
            print(f"\nError: {e}")

    def user_signup(self):
        try:
            customer_data = {
                'FirstName': input("\nEnter your first name: "),
                'LastName': input("Enter your last name: "),
                'Email': input("Enter your email: "),
                'PhoneNumber': input("Enter your phone number: "),
                'Address': input("Enter your address: "),
                'Username': input("Enter your username: "),
                'Password': input("Enter your password: "),
                'RegistrationDate': datetime.now()  # Assuming you have a way to get the current date
            }

            self.customer_service.register_customer(customer_data)
            print("User registered successfully!")

        except InvalidInputException as e:
            print(f"Error: {e}")

    def admin_auth_menu(self):
        while True:
            print(f"\n{CMD_COLOR_YELLOW}Admin Auth Options{CMD_COLOR_DEFAULT}")
            print("1. Admin Login")
            print("2. Admin Signup")
            print("0. Back to Main Menu")
            choice2 = int(input("Enter your choice: "))

            if choice2 == 0:
                break

            elif choice2 == 1:
                self.admin_login()

            elif choice2 == 2:
                self.admin_signup()

    def admin_login(self):
        try:
            username = input("\nEnter your username: ")
            password = input("Enter your password: ")
            user_data = self.auth_service.authenticate_admin(username, password)
            print(f"\n{CMD_COLOR_BLUE}Logged In Successfully!{CMD_COLOR_DEFAULT}")

            self.user_data = user_data
            self.isAuthenticated = True
            self.isAdmin = True

            self.admin_menu(user_data)
        except Exception as e:
            print(f"\nError: {e}")

    def admin_signup(self):
        try:
            user_data = {
                'FirstName': input("\nEnter your first name: "),
                'LastName': input("Enter your last name: "),
                'Email': input("Enter your email: "),
                'PhoneNumber': input("Enter your phone number: "),
                'Address': input("Enter your address: "),
                'Username': input("Enter your username: "),
                'Password': input("Enter your password: "),
                'RegistrationDate': datetime.now()  # Assuming you have a way to get the current date
            }

            self.admin_service.register_admin(user_data)
            print("User registered successfully!")

        except InvalidInputException as e:
            print(f"Error: {e}")

    def user_menu(self, user_data=None):
        if user_data is None:
            return

        while True:
            print(f"\n{CMD_COLOR_YELLOW}Main Menu{CMD_COLOR_DEFAULT}")
            print("1. Reserve a Vehicle")
            print("2. Logout")
            print("0. Exit")
            choice1 = int(input("Enter your choice: "))

            if choice1 == 0:
                break

            elif choice1 == 1:
                self.reserve_vehicle_menu(user_data)

            elif choice1 == 2:
                break

    def reserve_vehicle_menu(self, user_data):
        print(f"\n{CMD_COLOR_YELLOW}Reserve a Vehicle{CMD_COLOR_DEFAULT}")

        available_vehicles = self.vehicle_service.get_available_vehicles()

        if not len(available_vehicles):
            print("\nNo vehicles available to rent! Sorry!")
            return

        print("\nAvailable Vehicles:")
        for idx, vehicle in enumerate(available_vehicles, start=1):
            print(f"{idx}. {vehicle}")

        selected_vehicle_index = int(input("\nSelect a vehicle to reserve (enter 0 to go back): "))

        if selected_vehicle_index == 0:
            return
        elif 0 < selected_vehicle_index <= len(available_vehicles):
            selected_vehicle = available_vehicles[selected_vehicle_index - 1]

            reservation_data = {
                'CustomerID': user_data['CustomerID'],
                'VehicleID': selected_vehicle['VehicleID'],
                'StartDate': input("Enter start date and time: "),
                'EndDate': input("Enter end date and time: "),
                'TotalCost': selected_vehicle['DailyRate'],
                'Status': 'pending'
            }

            try:
                self.reservation_service.create_reservation(reservation_data)
                print("Reservation successful!")

            except Exception as e:
                print(f"Error: {e}")
        else:
            print("Invalid selection. Please try again.")

    def admin_menu(self, admin_data=None):
        if admin_data is None:
            return

        while True:
            print(f"\n{CMD_COLOR_YELLOW}Main Menu{CMD_COLOR_DEFAULT}")
            print("1. Vehicle Management")
            print("2. Reporting")
            print("3. Logout")
            print("0. Exit")
            choice1 = int(input("Enter your choice: "))

            if choice1 == 0:
                break

            elif choice1 == 1:
                self.vehicle_management_menu()

            elif choice1 == 2:
                self.reporting_menu()

            elif choice1 == 3:
                break

    def vehicle_management_menu(self):
        while True:
            print(f"\n{CMD_COLOR_YELLOW}Vehicle Management{CMD_COLOR_DEFAULT}")
            print("1. Create Vehicle")
            print("2. Show Vehicle")
            print("3. Update Vehicle")
            print("4. Delete Vehicle")
            print("0. Back to Main Menu")
            choice2 = int(input("Enter your choice: "))

            if choice2 == 0:
                break

            elif choice2 == 1:
                self.create_vehicle_menu()

            elif choice2 == 2:
                self.show_vehicle_menu()

            elif choice2 == 3:
                self.update_vehicle_menu()

            elif choice2 == 4:
                self.delete_vehicle_menu()

    def reporting_menu(self):
        while True:
            print(f"\n{CMD_COLOR_YELLOW}Reporting{CMD_COLOR_DEFAULT}")
            print("1. See Reservation History for a Vehicle")
            print("2. See Vehicle Utilization")
            print("3. See Revenue")
            print("0. Back to Main Menu")
            choice2 = int(input("Enter your choice: "))

            if choice2 == 0:
                break

            elif choice2 == 1:
                self.see_reservation_history()

            elif choice2 == 2:
                self.see_vehicle_utilization()

            elif choice2 == 3:
                self.report_generator.view_overall_revenue()

    def create_vehicle_menu(self):
        print("\nCreate Vehicle")

        vehicle_data = {
            'Model': input("Enter the vehicle model: "),
            'Make': input("Enter the vehicle make: "),
            'Year': input("Enter the manufacturing year: "),
            'Color': input("Enter the vehicle color: "),
            'RegistrationNumber':  input("Enter the registration number: "),
            'Availability': input("Is the vehicle available? (y/n): "),
            'DailyRate': input("Enter the daily rental rate: ")
        }

        try:
            self.vehicle_service.add_vehicle(vehicle_data)
            print("Vehicle created successfully!")

        except InvalidInputException as e:
            print(f"Error: {e}")

    def show_vehicle_menu(self):
        print("\nShow Vehicle")

        try:
            available_vehicles = self.vehicle_service.get_available_vehicles()

            if available_vehicles:
                print("\nAvailable Vehicles:")
                for vehicle in available_vehicles:
                    print(vehicle)
                    print("------------------------------")

            else:
                print("No available vehicles.")

        except Exception as e:
            print(f"Error: {e}")

    def update_vehicle_menu(self):
        print("\nUpdate Vehicle")
        try:
            vehicle_id = int(input("Enter the Vehicle ID you want to update: "))
            existing_vehicle = self.vehicle_service.get_vehicle_by_id(vehicle_id)

            if existing_vehicle:
                print("\nExisting Vehicle Details: ", existing_vehicle)
                print("------------------------------")

                print("\nRe-enter info with updated data: ")
                # Create a dictionary with updated data
                updated_vehicle_data = {
                    'VehicleID': vehicle_id,
                    'Model': input("Enter updated model: "),
                    'Make': int(input("Enter updated make: ")),
                    'Year': input("Enter updated year: "),
                    'Color': input("Enter updated color: "),
                    'RegistrationNumber': input("Enter updated registration number: "),
                    'DailyRate': float(input("Enter updated daily rate: ")),
                    'Availability': existing_vehicle.Availability
                }

                self.vehicle_service.update_vehicle(updated_vehicle_data)
                print("Vehicle updated successfully!")

            else:
                print(f"No vehicle found with ID {vehicle_id}.")

        except ValueError:
            print("Invalid input. Please enter a valid numeric value for Vehicle ID.")
        except Exception as e:
            print(f"Error: {e}")

    def delete_vehicle_menu(self):
        print("\nDelete Vehicle")
        try:
            vehicle_id = int(input("Enter the Vehicle ID you want to delete: "))

            # Call the remove_vehicle method from the vehicle service
            self.vehicle_service.remove_vehicle(vehicle_id)
            print(f"Vehicle with ID {vehicle_id} deleted successfully.")

        except ValueError:
            print("Invalid input. Please enter a valid numeric value for Vehicle ID.")
        except Exception as e:
            print(f"Error: {e}")

    def see_reservation_history(self):
        print("\nReservation History for a Vehicle")
        try:
            vehicle_id = int(input("Enter the Vehicle ID to see reservation history: "))

            # Call the method from ReservationService to get reservation history
            reservations = self.reservation_service.get_reservation_history(vehicle_id)

            if reservations:
                print("Reservation History:")
                for reservation in reservations:
                    print(reservation)
                    print("------------------------")
            else:
                print("No reservation history found for the specified vehicle.")

        except ValueError:
            print("Invalid input. Please enter a valid numeric value for Vehicle ID.")

    def see_vehicle_utilization(self):
        vehicle_id = input("Enter Vehicle ID: ")
        utilization_data = self.reservation_service.get_utilization_for_vehicle(vehicle_id)
        if utilization_data:
            print(f"Utilization for Vehicle {vehicle_id}: {utilization_data}%")
        else:
            print(f"No utilization data available for Vehicle {vehicle_id}")


if __name__ == "__main__":
    db_context = DatabaseContext(database="CarConnect")
    db_context.connect()
    interface = MainModule(db_context)
    interface.main_menu()
