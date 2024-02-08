from datetime import datetime
import time

from exceptions.DatabaseConnectionException import DatabaseConnectionException
from exceptions.InvalidInputException import InvalidInputException
from services.AdminService import AdminService
from services.AuthenticationService import AuthenticationService
from services.CustomerService import CustomerService
from services.DatabaseContext import DatabaseContext
from services.ReportGenerator import ReportGenerator
from services.ReservationService import ReservationService
from services.VehicleService import VehicleService
from utils.Constants import CMD_COLOR_YELLOW, CMD_COLOR_DEFAULT, CMD_COLOR_BLUE, CMD_COLOR_RED
from utils.Validator import InputValidator

from utils.helper_functions import input_menu_choice


class MainModule:
    def __init__(self, new_db_context, user_data=None):
        self.isAuthenticated = False
        self.isAdmin = False
        self.user_data = user_data
        self.customer_service = CustomerService(new_db_context)
        self.admin_service = AdminService(new_db_context)
        self.vehicle_service = VehicleService(new_db_context)
        self.reservation_service = ReservationService(new_db_context)
        self.auth_service = AuthenticationService(self.customer_service, self.admin_service)
        self.input_validator = InputValidator()
        self.report_generator = ReportGenerator(new_db_context)

    def main_menu(self):
        if not self.isAuthenticated:
            self.auth_menu()
        elif self.isAuthenticated and not self.isAdmin and self.user_data:
            self.user_menu(self.user_data)
        elif self.isAuthenticated and self.isAdmin and self.user_data:
            self.admin_menu(self.user_data)

    def auth_menu(self):
        while True:
            print(f"\n{CMD_COLOR_YELLOW}Auth Menu{CMD_COLOR_DEFAULT}")
            print("1. User Auth Options")
            print("2. Admin Auth Options")
            print("0. Exit")
            choice = input_menu_choice()

            if choice == 0:
                break

            elif choice == 1:
                self.user_auth_menu()

            elif choice == 2:
                self.admin_auth_menu()

            else:
                print(f"{CMD_COLOR_RED}Invalid choice. Please enter a valid option.{CMD_COLOR_DEFAULT}")

    def user_auth_menu(self):
        while True:
            print(f"\n{CMD_COLOR_YELLOW}User Auth Options{CMD_COLOR_DEFAULT}")
            print("1. User Login")
            print("2. User Signup")
            print("0. Back to Auth Menu")
            choice = input_menu_choice()

            if choice == 0:
                break

            elif choice == 1:
                self.user_login()

            elif choice == 2:
                self.user_signup()

            else:
                print(f"{CMD_COLOR_RED}Invalid choice. Please enter a valid option.{CMD_COLOR_DEFAULT}")

    def user_login(self):
        try:
            username = input("\nEnter your username: ")
            password = input("Enter your password: ")
            user_data = self.auth_service.authenticate_customer(username, password)
            print(f"\n{CMD_COLOR_BLUE}Logged In Successfully!{CMD_COLOR_DEFAULT}")

            # Setting auth
            self.user_data = user_data
            self.isAuthenticated = True

            self.user_menu(user_data)
        except Exception as ex:
            print(f"\n{CMD_COLOR_RED}{ex}{CMD_COLOR_DEFAULT}")

    def user_signup(self):
        try:
            customer_data = {
                'FirstName': input("\nEnter your first name: "),
                'LastName': input("Enter your last name: "),
                'Email': input("Enter your email(eg. vatsal@email.com): "),
                'PhoneNumber': input("Enter your phone number(eg. 9998070564): "),
                'Address': input("Enter your address: "),
                'Username': input("Enter your username: "),
                'Password': input("Enter your password: "),
                'RegistrationDate': datetime.now()
            }

            self.customer_service.register_customer(customer_data)
            print(f"\n{CMD_COLOR_BLUE}Customer registered successfully!{CMD_COLOR_DEFAULT}")
        except Exception as ex:
            print(f"\n{CMD_COLOR_RED}{ex}{CMD_COLOR_DEFAULT}")

    def admin_auth_menu(self):
        while True:
            print(f"\n{CMD_COLOR_YELLOW}Admin Auth Options{CMD_COLOR_DEFAULT}")
            print("1. Admin Login")
            print("2. Admin Signup")
            print("0. Back to Auth Menu")
            choice = input_menu_choice()

            if choice == 0:
                break

            elif choice == 1:
                self.admin_login()

            elif choice == 2:
                self.admin_signup()

            else:
                print(f"{CMD_COLOR_RED}Invalid choice. Please enter a valid option.{CMD_COLOR_DEFAULT}")

    def admin_login(self):
        try:
            username = input("\nEnter your username: ")
            password = input("Enter your password: ")
            user_data = self.auth_service.authenticate_admin(username, password)
            print(f"\n{CMD_COLOR_BLUE}Logged In Successfully!{CMD_COLOR_DEFAULT}")

            # Setting auth
            self.user_data = user_data
            self.isAuthenticated = True
            self.isAdmin = True

            self.admin_menu(user_data)
        except Exception as ex:
            print(f"\n{CMD_COLOR_RED}{ex}{CMD_COLOR_DEFAULT}")

    def admin_signup(self):
        try:
            user_data = {
                'FirstName': input("\nEnter your first name: "),
                'LastName': input("Enter your last name: "),
                'Email': input("Enter your email(eg. vatsal@email.com): "),
                'PhoneNumber': input("Enter your phone number(eg. 9998070564): "),
                'Address': input("Enter your address: "),
                'Username': input("Enter your username: "),
                'Password': input("Enter your password: "),
                'RegistrationDate': datetime.now()
            }

            self.admin_service.register_admin(user_data)
            print(f"\n{CMD_COLOR_BLUE}Admin registered successfully!{CMD_COLOR_DEFAULT}")
        except Exception as ex:
            print(f"\n{CMD_COLOR_RED}{ex}{CMD_COLOR_DEFAULT}")

    def user_menu(self, user_data=None):
        if user_data is None:
            return

        while True:
            print(f"\n{CMD_COLOR_YELLOW}Main Menu{CMD_COLOR_DEFAULT}")
            print("1. Reserve a Vehicle")
            print("2. Logout")
            choice = input_menu_choice()

            if choice == 1:
                self.reserve_vehicle(user_data.customer_id)

            elif choice == 2:
                self.user_data = None
                self.isAuthenticated = False
                break

            else:
                print(f"{CMD_COLOR_RED}Invalid choice. Please enter a valid option.{CMD_COLOR_DEFAULT}")

    def reserve_vehicle(self, user_id):
        available_vehicles = self.vehicle_service.get_available_vehicles()

        if not len(available_vehicles):
            print("\nNo vehicles available to rent! Sorry!")
            return

        vehicle_indexes_list = [i[0] for i in available_vehicles]

        while True:
            print("\nAvailable Vehicles:")
            for idx, vehicle in enumerate(available_vehicles, start=1):
                print(f"VehicleID: {vehicle[0]} \n{vehicle}\n")
            print("0. Cancel")

            selected_vehicle_index = input_menu_choice("\nEnter a VehicleID to reserve (or 0 to Cancel): ")

            if selected_vehicle_index == 0:
                break

            elif selected_vehicle_index in vehicle_indexes_list:
                selected_vehicle = next(item for item in available_vehicles if item[0] == selected_vehicle_index)

                print("\nSelected: ", selected_vehicle)

                reservation_data = {
                    'CustomerID': user_id,
                    'VehicleID': selected_vehicle[0],
                    'StartDate': input("Enter start date and time(eg. YYYY-MM-DD HH:MI:SS): "),
                    'EndDate': input("Enter end date and time(eg. YYYY-MM-DD HH:MI:SS): "),
                    'TotalCost': selected_vehicle[7],
                    'Status': 'pending'
                }

                try:
                    self.reservation_service.create_reservation(reservation_data)
                    print(f"\n{CMD_COLOR_BLUE}Reservation successful!{CMD_COLOR_DEFAULT}")
                    break
                except Exception as ex:
                    print(f"\n{CMD_COLOR_RED}{ex}{CMD_COLOR_DEFAULT}")
            else:
                print(f"{CMD_COLOR_RED}Invalid choice. Please enter a valid option.{CMD_COLOR_DEFAULT}")
                print("Showing list again, wait...")
                time.sleep(2)

    def admin_menu(self, admin_data=None):
        if admin_data is None:
            return

        while True:
            print(f"\n{CMD_COLOR_YELLOW}Main Menu{CMD_COLOR_DEFAULT}")
            print("1. Vehicle Management")
            print("2. Reporting")
            print("3. Logout")
            choice = input_menu_choice()

            if choice == 1:
                self.vehicle_management_menu()

            elif choice == 2:
                self.reporting_menu()

            elif choice == 3:
                self.user_data = None
                self.isAuthenticated = False
                self.isAdmin = True
                break

            else:
                print(f"{CMD_COLOR_RED}Invalid choice. Please enter a valid option.{CMD_COLOR_DEFAULT}")

    def vehicle_management_menu(self):
        while True:
            print(f"\n{CMD_COLOR_YELLOW}Vehicle Management{CMD_COLOR_DEFAULT}")
            print("1. Create Vehicle")
            print("2. Show Vehicle")
            print("3. Update Vehicle")
            print("4. Delete Vehicle")
            print("0. Back to Main Menu")
            choice = input_menu_choice()

            if choice == 0:
                break

            elif choice == 1:
                self.create_vehicle()

            elif choice == 2:
                self.show_vehicle()

            elif choice == 3:
                self.update_vehicle()

            elif choice == 4:
                self.delete_vehicle()

            else:
                print(f"{CMD_COLOR_RED}Invalid choice. Please enter a valid option.{CMD_COLOR_DEFAULT}")

    def create_vehicle(self):
        print("\nCreate Vehicle")

        try:
            vehicle_data = {
                'Model': input("Enter the vehicle model: "),
                'Make': input("Enter the vehicle make: "),
                'Year': int(input("Enter the manufacturing year(eg. 2024): ")),
                'Color': input("Enter the vehicle color: "),
                'RegistrationNumber':  input("Enter the registration number(eg. GJ059062): "),
                'Availability': input("Is the vehicle available? (y/n): "),
                'DailyRate': float(input("Enter the daily rental rate: "))
            }

        except Exception as ex:
            print(f"\n{CMD_COLOR_RED}Invalid Input: {ex}{CMD_COLOR_DEFAULT}")
            return

        try:
            self.vehicle_service.add_vehicle(vehicle_data)
            print(f"\n{CMD_COLOR_BLUE}Vehicle created successfully!{CMD_COLOR_DEFAULT}")
        except Exception as ex:
            print(f"\n{CMD_COLOR_RED}{ex}{CMD_COLOR_DEFAULT}")

    def show_vehicle(self):
        try:
            available_vehicles = self.vehicle_service.get_available_vehicles()
            print("\nAvailable Vehicles:")
            for vehicle in available_vehicles:
                print(vehicle)
        except Exception as ex:
            print(f"\n{CMD_COLOR_RED}{ex}{CMD_COLOR_DEFAULT}")

    def update_vehicle(self):
        print("\nUpdate Vehicle")
        try:
            vehicle_id = int(input("Enter the Vehicle ID you want to update: "))
            existing_vehicle = self.vehicle_service.get_vehicle_by_id(vehicle_id)
        except Exception as ex:
            print(f"\n{CMD_COLOR_RED}Invalid VehicleID: {ex}{CMD_COLOR_DEFAULT}")
            return

        if existing_vehicle:
            print("\nExisting Vehicle Details: ", existing_vehicle)

            # Create a dictionary with updated data
            print("\nRe-enter info with updated data: ")

            try:
                updated_vehicle_data = {
                    'VehicleID': vehicle_id,
                    'Model': input("Enter updated model: "),
                    'Make': input("Enter updated make: "),
                    'Year': int(input("Enter updated year: ")),
                    'Color': input("Enter updated color: "),
                    'RegistrationNumber': input("Enter updated registration number: "),
                    'DailyRate': float(input("Enter updated daily rate: ")),
                    'Availability': existing_vehicle[6]
                }
            except Exception as ex:
                print(f"\n{CMD_COLOR_RED}Invalid Input: {ex}{CMD_COLOR_DEFAULT}")
                return

            try:
                self.vehicle_service.update_vehicle(updated_vehicle_data)
                print(f"\n{CMD_COLOR_BLUE}Vehicle updated successfully!{CMD_COLOR_DEFAULT}")
            except Exception as ex:
                print(f"\n{CMD_COLOR_RED}{ex}{CMD_COLOR_DEFAULT}")

    def delete_vehicle(self):
        print("\nDelete Vehicle")
        try:
            vehicle_id = int(input("Enter the Vehicle ID you want to delete: "))
        except Exception as ex:
            print(f"\n{CMD_COLOR_RED}Invalid Input: {ex}{CMD_COLOR_DEFAULT}")
            return

        try:
            self.vehicle_service.remove_vehicle(vehicle_id)
            print(f"\n{CMD_COLOR_BLUE}Vehicle with ID {vehicle_id} deleted successfully.{CMD_COLOR_DEFAULT}")
        except Exception as ex:
            print(f"\n{CMD_COLOR_RED}{ex}{CMD_COLOR_DEFAULT}")

    def reporting_menu(self):
        while True:
            print(f"\n{CMD_COLOR_YELLOW}Reporting{CMD_COLOR_DEFAULT}")
            print("1. See Reservation History for a Vehicle")
            print("2. See Vehicle Utilization")
            print("3. See Revenue")
            print("0. Back to Main Menu")
            choice = input_menu_choice()

            if choice == 0:
                break

            elif choice == 1:
                self.see_reservation_history()

            elif choice == 2:
                self.see_vehicle_utilization()

            elif choice == 3:
                try:
                    revenue = self.report_generator.view_overall_revenue()
                    print(f"\n{CMD_COLOR_BLUE}Overall revenue: {revenue}$.{CMD_COLOR_DEFAULT}")
                except Exception as ex:
                    print(f"\n{CMD_COLOR_RED}{ex}{CMD_COLOR_DEFAULT}")

            else:
                print(f"{CMD_COLOR_RED}Invalid choice. Please enter a valid option.{CMD_COLOR_DEFAULT}")

    def see_reservation_history(self):
        print("\nReservation History for a Vehicle")
        try:
            vehicle_id = int(input("Enter the Vehicle ID to see reservation history: "))
        except Exception as ex:
            print(f"\n{CMD_COLOR_RED}Invalid Input: {ex}{CMD_COLOR_DEFAULT}")
            return

        try:
            reservations = self.reservation_service.get_reservation_history(vehicle_id)

            print("\nReservation History:")
            for reservation in reservations:
                print(reservation)
        except Exception as ex:
            print(f"\n{CMD_COLOR_RED}Invalid Input: {ex}{CMD_COLOR_DEFAULT}")
            return

    def see_vehicle_utilization(self):
        vehicle_id = input("Enter Vehicle ID: ")
        utilization_data = self.reservation_service.get_utilization_for_vehicle(vehicle_id)
        if utilization_data:
            print(f"Utilization for Vehicle {vehicle_id}: {utilization_data}%")
        else:
            print(f"No utilization data available for Vehicle {vehicle_id}")


if __name__ == "__main__":
    db_context = DatabaseContext()

    try:
        db_context.connect()  # Connecting to database
        interface = MainModule(db_context)
        interface.main_menu()
        db_context.disconnect()  # Disconnect database after exiting
    except DatabaseConnectionException as e:
        print(e)
