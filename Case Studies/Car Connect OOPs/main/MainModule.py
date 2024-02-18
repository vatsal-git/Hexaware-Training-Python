from datetime import datetime, timedelta
import time
from prettytable import PrettyTable

from exceptions.DatabaseConnectionException import DatabaseConnectionException
from exceptions.InvalidInputException import InvalidInputException
from services.AdminService import AdminService
from services.AuthenticationService import AuthenticationService
from services.CustomerService import CustomerService
from services.DatabaseContext import DatabaseContext
from services.ReportGenerator import ReportGenerator
from services.ReservationService import ReservationService
from services.VehicleService import VehicleService
from utils.Validator import InputValidator
from utils.HelperFunctions import input_menu_choice, print_error, print_title, print_info, print_welcome


class MainModule:
    def __init__(self, new_db_context, user_data=None):
        self.input_validator = InputValidator()

        # Auth Setup
        self.isAuthenticated = False
        self.isAdmin = False
        self.user_data = user_data

        # Services setup
        self.customer_service = CustomerService(new_db_context)
        self.admin_service = AdminService(new_db_context)
        self.vehicle_service = VehicleService(new_db_context)
        self.reservation_service = ReservationService(new_db_context)
        self.auth_service = AuthenticationService(new_db_context)
        self.report_generator = ReportGenerator(new_db_context)

    def main_menu(self):
        print_welcome()
        if not self.isAuthenticated:
            self.auth_menu()
        elif self.isAuthenticated and not self.isAdmin and self.user_data:
            self.user_menu(self.user_data)
        elif self.isAuthenticated and self.isAdmin and self.user_data:
            self.admin_menu(self.user_data)

    def auth_menu(self):
        while True:
            print_title("\nAuth Menu")
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
                print_error("Invalid choice. Please enter a valid option.")

    def user_auth_menu(self):
        while True:
            print_title("\nUser Auth Options")
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
                print_error("Invalid choice. Please enter a valid option.")

    def user_login(self):
        try:
            username = input("\nEnter your username: ")
            password = input("Enter your password: ")
            user_data = self.auth_service.authenticate_customer(username, password)

            print_info("\nLogged In Successfully!")
            user_data.show_details()

            # Setting auth
            self.user_data = user_data
            self.isAuthenticated = True

            # Route to Main Menu
            self.user_menu(user_data)
        except Exception as ex:
            print_error(f"\n{ex}")

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
        except Exception as ex:
            print_error(f"\nInvalid Input: {ex}")
            return

        try:
            self.customer_service.register_customer(customer_data)
            print_info("\nCustomer registered successfully!")
        except Exception as ex:
            print_error(f"\n{ex}")

    def admin_auth_menu(self):
        while True:
            print_title("\nAdmin Auth Options")
            print("1. Admin Login")
            print("0. Back to Auth Menu")
            choice = input_menu_choice()

            if choice == 0:
                break

            elif choice == 1:
                self.admin_login()

            else:
                print_error("Invalid choice. Please enter a valid option.")

    def admin_login(self):
        try:
            username = input("\nEnter your username: ")
            password = input("Enter your password: ")
            user_data = self.auth_service.authenticate_admin(username, password)

            print_info("\nLogged In Successfully!")
            user_data.show_details()

            # Setting auth
            self.user_data = user_data
            self.isAuthenticated = True
            self.isAdmin = True

            # Route to Main Menu
            self.admin_menu(user_data)
        except Exception as ex:
            print_error(f"\n{ex}")

    def user_menu(self, user_data=None):
        if user_data is None:
            return

        while True:
            print_title(f"\nMain Menu")
            print("1. Reserve a Vehicle")
            print("2. Your existing Reservations")
            print("3. Logout")
            choice = input_menu_choice()

            if choice == 1:
                self.reserve_vehicle(user_data.customer_id)

            elif choice == 2:
                self.existing_reservations(user_data.customer_id)

            elif choice == 3:
                self.user_data = None
                self.isAuthenticated = False
                break

            else:
                print_error("Invalid choice. Please enter a valid option.")

    def reserve_vehicle(self, user_id):
        while True:
            print_title("\nAvailable Vehicles:")
            try:
                available_vehicles = self.show_available_vehicles()
                vehicle_indexes_list = [i.vehicle_id for i in available_vehicles]
            except Exception as ex:
                print_error(f"\n{ex}")
                break
            print("0. Cancel")

            selected_vehicle_id = input_menu_choice("\nEnter a VehicleID to reserve (or 0 to Cancel): ")

            if selected_vehicle_id == 0:
                break

            elif selected_vehicle_id in vehicle_indexes_list:
                selected_vehicle = next(item for item in available_vehicles if item.vehicle_id == selected_vehicle_id)

                print_info(f"\nSelected Vehicle:")
                selected_vehicle.show_details()

                start_date_str = input("\nEnter start date and time(eg. YYYY-MM-DD HH:MI:SS): ")
                end_date_str = input("Enter end date and time(eg. YYYY-MM-DD HH:MI:SS): ")

                try:
                    start_date = datetime.strptime(start_date_str, "%Y-%m-%d %H:%M:%S")
                    end_date = datetime.strptime(end_date_str, "%Y-%m-%d %H:%M:%S")

                    if start_date < datetime.now():
                        raise InvalidInputException("Start date should be greater than or equal to the current date and time")

                    if end_date <= start_date + timedelta(days=1):
                        raise InvalidInputException("Booking should be for at least 1 day")

                    num_days = (end_date - start_date).days
                    if num_days < 1:
                        raise InvalidInputException("Booking should be of at least 1 day")

                    total_cost = selected_vehicle.daily_rate * num_days
                except Exception as ex:
                    print_error(f"\nInvalid Input: {ex}")
                    return

                reservation_data = {
                    'CustomerID': user_id,
                    'VehicleID': selected_vehicle.vehicle_id,
                    'StartDate': start_date_str,
                    'EndDate': end_date_str,
                    'TotalCost': total_cost,
                    'Status': 'pending'
                }

                try:
                    self.reservation_service.create_reservation(reservation_data)
                    print_info(f"\nReservation successful!")
                    return
                except Exception as ex:
                    print_error(f"\n{ex}")
            else:
                print_error("Invalid choice. Please enter a valid option.")
                if len(available_vehicles) > 15:  # Users will not see the error if the list is long
                    countdown = 3
                    while countdown > 0:
                        print(f"Showing list again in {countdown}...")
                        time.sleep(1)
                        countdown -= 1

    def existing_reservations(self, user_id):
        reservations = self.reservation_service.get_reservations_by_customer_id(user_id)

        print_info(f"\nMy Reservation: ")
        table = PrettyTable()
        table.field_names = ["ReservationID", "Model", "Make", "Color", "RegistrationNumber",
                             "Duration", "TotalCost"]
        for reservation in reservations:
            row = []
            for i in reservation:
                row.append(i)
            table.add_row(row)
        print(table)

    def admin_menu(self, admin_data=None):
        if admin_data is None:
            return

        while True:
            print_title("\nMain Menu")
            print("1. New Admin Signup")
            print("2. Vehicle Management")
            print("3. Reporting")
            print("4. Logout")
            choice = input_menu_choice()

            if choice == 1:
                self.admin_signup()

            elif choice == 2:
                self.vehicle_management_menu()

            elif choice == 3:
                self.reporting_menu()

            elif choice == 4:
                self.user_data = None
                self.isAuthenticated = False
                self.isAdmin = True
                break

            else:
                print_error("Invalid choice. Please enter a valid option.")

    def admin_signup(self):
        try:
            user_data = {
                'FirstName': input("\nEnter your first name: "),
                'LastName': input("Enter your last name: "),
                'Email': input("Enter your email(eg. vatsal@email.com): "),
                'PhoneNumber': input("Enter your phone number(eg. 9998070564): "),
                'Address': input("Enter your address: "),
                'Username': input("Enter your username: ").strip(),
                'Password': input("Enter your password: "),
                'RegistrationDate': datetime.now()
            }

            self.admin_service.register_admin(user_data)
            print_info(f"\nAdmin registered successfully!")
        except Exception as ex:
            print_error(f"\n{ex}")

    def vehicle_management_menu(self):
        while True:
            print_title("\nVehicle Management")
            print("1. Create Vehicle")
            print("2. Show All Vehicles")
            print("3. Update Vehicle")
            print("4. Delete Vehicle")
            print("0. Back to Main Menu")
            choice = input_menu_choice()

            if choice == 0:
                break

            elif choice == 1:
                self.create_vehicle()

            elif choice == 2:
                try:
                    self.show_vehicles()
                except Exception as ex:
                    print_error(f"\n{ex}")

            elif choice == 3:
                self.update_vehicle()

            elif choice == 4:
                self.delete_vehicle()

            else:
                print_error("Invalid choice. Please enter a valid option.")

    def create_vehicle(self):
        print_title("\nCreate Vehicle")

        try:
            vehicle_data = {
                'Model': input("Enter the vehicle model: "),
                'Make': input("Enter the vehicle make: "),
                'Year': int(input("Enter the manufacturing year(eg. 2024): ")),
                'Color': input("Enter the vehicle color: "),
                'RegistrationNumber':  input("Enter the registration number(eg. GJ059062): "),
                'DailyRate': float(input("Enter the daily rental rate: "))
            }
        except Exception as ex:
            print_error(f"\nInvalid Input: {ex}")
            return

        try:
            self.vehicle_service.add_vehicle(vehicle_data)
            print_info(f"\nVehicle created successfully!")
        except Exception as ex:
            print_error(f"\n{ex}")

    def show_vehicles(self):
        try:
            print_title("\nAll Vehicles:")
            vehicles = self.vehicle_service.get_all_vehicles()
            table = PrettyTable()
            table.field_names = ["VehicleID", "Model", "Make", "Year", "Color", "RegistrationNumber", "Availability", "DailyRate"]
            for vehicle in vehicles:
                table.add_row([vehicle.vehicle_id, vehicle.model, vehicle.make, vehicle.year, vehicle.color, vehicle.registration_number, vehicle.availability, f"{vehicle.daily_rate:.2f}"])
            print(table)
            return vehicles
        except Exception as ex:
            print_error(f"\n{ex}")

    def show_available_vehicles(self):
        try:
            available_vehicles = self.vehicle_service.get_available_vehicles()
            table = PrettyTable()
            table.field_names = ["VehicleID", "Model", "Make", "Year", "Color", "RegistrationNumber", "DailyRate"]
            for vehicle in available_vehicles:
                table.add_row([vehicle.vehicle_id, vehicle.model, vehicle.make, vehicle.year, vehicle.color, vehicle.registration_number, f"{vehicle.daily_rate:.2f}"])
            print(table)
            return available_vehicles
        except Exception as ex:
            print_error(f"\n{ex}")

    def update_vehicle(self):
        while True:
            print_title("\nAvailable Vehicles:")
            try:
                vehicles = self.show_vehicles()
                vehicle_indexes_list = [i.vehicle_id for i in vehicles]
            except Exception as ex:
                print_error(f"\n{ex}")
                break
            print("0. Cancel")

            selected_vehicle_id = input_menu_choice("\nEnter a VehicleID to update (or 0 to Cancel): ")

            if selected_vehicle_id == 0:
                break

            elif selected_vehicle_id in vehicle_indexes_list:
                try:
                    existing_vehicle = self.vehicle_service.get_vehicle_by_id(selected_vehicle_id)
                except Exception as ex:
                    print_error(f"\n{ex}")
                    return

                print_info(f"\nExisting Details of selected Vehicle:")
                existing_vehicle.show_details()

                # Create a dictionary with updated data
                print("\nRe-enter info with updated data: ")
                try:
                    updated_vehicle_data = {
                        'VehicleID': selected_vehicle_id,
                        'Model': input("Enter updated model: ") or existing_vehicle.model,
                        'Make': input("Enter updated make: ") or existing_vehicle.make,
                        'Year': int(input("Enter updated year: ")) if input("Update year? (y/n): ").upper() == 'y' else
                        existing_vehicle.year,
                        'Color': input("Enter updated color: ") or existing_vehicle.color,
                        'RegistrationNumber': input("Enter updated registration number: ") or existing_vehicle.registration_number,
                        'DailyRate': float(input("Enter updated daily rate: ")) if input(
                            "Update daily rate? (Y/N): ").upper() == 'Y' else existing_vehicle.daily_rate,
                        'Availability': input("Enter Availability: ") or existing_vehicle.availability
                    }

                except Exception as ex:
                    print_error(f"\nInvalid Input: {ex}")
                    return

                try:
                    self.vehicle_service.update_vehicle(updated_vehicle_data)
                    print_info(f"\nVehicle updated successfully!")
                    return
                except Exception as ex:
                    print_error(f"\n{ex}")

            else:
                print_error("Invalid choice. Please enter a valid option.")
                if len(vehicles) > 15:  # Users will not see the error if the list is long
                    countdown = 3
                    while countdown > 0:
                        print(f"Showing list again in {countdown}...")
                        time.sleep(1)
                        countdown -= 1

    def delete_vehicle(self):
        while True:
            print_title("\nAvailable Vehicles:")
            try:
                vehicles = self.show_vehicles()
                vehicle_indexes_list = [i.vehicle_id for i in vehicles]
            except Exception as ex:
                print_error(f"\n{ex}")
                break
            print("0. Cancel")

            selected_vehicle_id = input_menu_choice("\nEnter a VehicleID to delete (or 0 to Cancel): ")

            if selected_vehicle_id == 0:
                break

            elif selected_vehicle_id in vehicle_indexes_list:
                try:
                    self.vehicle_service.remove_vehicle(selected_vehicle_id)
                    print_info(f"\nVehicle with ID {selected_vehicle_id} deleted successfully.")
                    break
                except Exception as ex:
                    print_error(f"\n{ex}")

            else:
                print_error("Invalid choice. Please enter a valid option.")
                if len(vehicles) > 15:  # Users will not see the error if the list is long
                    countdown = 3
                    while countdown > 0:
                        print(f"Showing list again in {countdown}...")
                        time.sleep(1)
                        countdown -= 1

    def reporting_menu(self):
        while True:
            print_title(f"\nReporting")
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
                self.see_revenue()

            else:
                print_error("Invalid choice. Please enter a valid option.")

    def see_reservation_history(self):
        while True:
            print_title("\nAvailable Vehicles:")
            try:
                vehicles = self.show_vehicles()
                vehicle_indexes_list = [i.vehicle_id for i in vehicles]
            except Exception as ex:
                print_error(f"\n{ex}")
                break
            print("0. Cancel")

            selected_vehicle_id = input_menu_choice("\nEnter a VehicleID to See Reservation History (or 0 to Cancel): ")

            if selected_vehicle_id == 0:
                break

            elif selected_vehicle_id in vehicle_indexes_list:
                try:
                    reservations = self.report_generator.get_reservation_history(selected_vehicle_id)

                    print_info(f"\nReservation History: ")
                    table = PrettyTable()
                    table.field_names = ["ReservationID", "CustomerName", "Email", "Phone", "Vehicle", "Color", "RegistrationNumber",
                                         "Duration", "TotalCost"]
                    for reservation in reservations:
                        row = []
                        for i in reservation:
                            row.append(i)
                        table.add_row(row)
                    print(table)
                    break
                except Exception as ex:
                    print_error(f"\n{ex}")

            else:
                print_error("Invalid choice. Please enter a valid option.")
                if len(vehicles) > 15:  # Users will not see the error if the list is long
                    countdown = 3
                    while countdown > 0:
                        print(f"Showing list again in {countdown}...")
                        time.sleep(1)
                        countdown -= 1

    def see_vehicle_utilization(self):
        while True:
            print_title("\nAvailable Vehicles:")

            try:
                available_vehicles = self.show_available_vehicles()
                vehicle_indexes_list = [i.vehicle_id for i in available_vehicles]
            except Exception as ex:
                print_error(f"\n{ex}")
                break
            print("0. Cancel")

            selected_vehicle_id = input_menu_choice("\nEnter a VehicleID to See its Utilization (or 0 to Cancel): ")

            if selected_vehicle_id == 0:
                break

            elif selected_vehicle_id in vehicle_indexes_list:
                try:
                    utilization_data = self.report_generator.get_utilization_for_vehicle(selected_vehicle_id)
                    print_info(f"\nUtilization for Vehicle: {utilization_data}%")
                    print("*Note: Vehicle Utilization = (Total Reservations / Max Reservations After Service) * 100")
                    break
                except Exception as ex:
                    print_error(f"\n{ex}")

            else:
                print_error("Invalid choice. Please enter a valid option.")
                if len(available_vehicles) > 15:  # Users will not see the error if the list is long
                    countdown = 3
                    while countdown > 0:
                        print(f"Showing list again in {countdown}...")
                        time.sleep(1)
                        countdown -= 1

    def see_revenue(self):
        try:
            revenue = self.report_generator.view_overall_revenue()
            print_info(f"\nOverall revenue: {revenue}$.")
        except Exception as ex:
            print_error(f"\n{ex}")


if __name__ == "__main__":
    db_context = DatabaseContext()

    try:
        db_context.connect()  # Connecting to database
        interface = MainModule(db_context)
        interface.main_menu()
        db_context.disconnect()  # Disconnect database after exiting
    except DatabaseConnectionException as e:
        print(e)
