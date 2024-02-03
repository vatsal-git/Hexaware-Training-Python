from models.customer import Customer
from utils.constants import CMD_COLOR_YELLOW, CMD_COLOR_DEFAULT
from utils.exceptions import InvalidEmailError, InvalidIDError
from models.customer import Customer
from utils.validations import validate_id


class CustomerServices:
    def __init__(self, db_services):
        self.db_services = db_services

    def register_customer(self):
        customer = Customer()
        user_input = self.take_customer_input()

        # Validating Inputs
        customer.first_name = user_input['first_name']
        customer.last_name = user_input['last_name']
        customer.email = user_input['email']
        customer.phone = user_input['phone']
        customer.address = user_input['address']

        print("\nEntered data:")
        customer.get_customer_details()

        # Check for duplicate email in the database
        if self.is_email_registered(customer.email):
            raise InvalidEmailError("Email address is already registered.")

        # Insert new customer into the database using query method
        query = '''
        INSERT INTO Customers (first_name, last_name, email, phone, address)
        VALUES (%s, %s, %s, %s, %s)
        '''
        values = (customer.first_name, customer.last_name, customer.email, customer.phone, customer.address)
        result = self.db_services.execute_query(query, values)

        if result is not None:
            print("\nCustomer registered successfully.")
        return

    def update_customer_account(self):
        customer_id = int(input("\nEnter customer ID to update: "))
        customer = self.db_services.get_customer_by_id(customer_id)

        print("\nExisting data:")
        customer.get_customer_details()

        if customer:
            customer = Customer()
            update_input = self.take_customer_input(update=True)

            # Validating Inputs
            if 'first_name' in update_input:
                customer.first_name = update_input['first_name']
            if 'last_name' in update_input:
                customer.last_name = update_input['last_name']
            if 'email' in update_input:
                customer.email = update_input['email']
            if 'phone' in update_input:
                customer.phone = update_input['phone']
            if 'address' in update_input:
                customer.address = update_input['address']

            # Construct the SET part of the query dynamically based on non-empty fields
            set_parts = [f"{key} = %s" for key in update_input.keys()]
            set_clause = ', '.join(set_parts)

            print('set_clause =>', set_clause)

            # Update customer information in the database using the dynamically constructed query
            query = f"UPDATE Customers SET {set_clause} WHERE customer_id = %s"

            # Include values for non-empty fields and customer_id at the end
            values = list(update_input.values()) + [customer_id]

            # Execute the query
            result = self.db_services.execute_query(query, values)

            if result is not None:
                print("\nCustomer information updated successfully.")
            return
        else:
            raise InvalidIDError("Customer Id not matching any records.")

    @staticmethod
    def take_customer_input(update=False):
        print(f"{CMD_COLOR_YELLOW}\nGive Inputs{CMD_COLOR_DEFAULT}")

        if update:
            print("*Note - Leave the field empty to retain existing data.")

        # Input dictionary
        customer_input = {
            'first_name': input("Enter new first name: ") if update else input("Enter first name: "),
            'last_name': input("Enter new last name: ") if update else input("Enter last name: "),
            'email': input("Enter new email address: ") if update else input("Enter email address: "),
            'phone': input("Enter new phone number: ") if update else input("Enter phone number: "),
            'address': input("Enter new address: ") if update else input("Enter address: ")
        }

        if update:
            update_input = {key: value for key, value in customer_input.items() if len(value) != 0}
            return update_input

        return customer_input

    def is_email_registered(self, email):
        query = "SELECT COUNT(*) FROM Customers WHERE email = %s"
        result = self.db_services.execute_query(query, (email,))
        return result[0][0] > 0 if result else False

    def get_customer_by_id(self, customer_id):
        if not validate_id(customer_id):
            raise InvalidIDError("Invalid customer ID.")

        query = "SELECT * FROM Customers WHERE customer_id = %s"
        result = self.db_services.execute_query(query, (customer_id,))

        if result:
            customer_data = result[0]
            return Customer(*customer_data)
        else:
            raise InvalidIDError("Customer Id not matching any records.")

