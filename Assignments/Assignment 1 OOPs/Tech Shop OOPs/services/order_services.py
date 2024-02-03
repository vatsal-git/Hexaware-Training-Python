from models.order import Order
from utils.constants import CMD_COLOR_YELLOW, CMD_COLOR_DEFAULT
from utils.exceptions import InvalidIDError, InvalidEnumError
from utils.validations import validate_id, validate_enum
from services.database_services import DatabaseServices
from datetime import datetime


class OrderServices:
    def __init__(self, db_services, customer_services, product_services):
        self.db_services = db_services
        self.customer_services = customer_services
        self.product_services = product_services

    def place_new_order(self):
        customer_id = int(input('Who is placing the order? Enter customer id: '))
        customer = self.customer_services.get_customer_by_id(customer_id)

        if customer:
            order = Order()
            order_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Take order and calculate total
            order.total_amount = self.get_total_amount()

            # Insert new order into the database using query method
            query = '''
            INSERT INTO Orders (customer_id, order_date, total_amount, order_status)
            VALUES (%s, %s, %s, %s)
            '''
            values = (customer_id, order_date, order.total_amount, 'Pending')
            result = self.db_services.execute_query(query, values)

            if result is not None:
                print("\nOrder placed successfully.")
            return
        else:
            raise InvalidIDError("Customer Id not matching any records.")

    def track_order_status(self):
        order_id = int(input('Enter order id to track: '))
        order = self.get_order_by_id(order_id)

        if order:
            print("\nCurrent Order Details:")
            order.get_order_details()
        else:
            raise InvalidIDError("Order Id not matching any records.")

    def cancel_order(self):
        order_id = int(input('Enter order id to track: '))
        order = self.get_order_by_id(order_id)

        if order:
            # Update order status to 'Cancelled' in the database using query method
            query = "UPDATE Orders SET order_status = %s WHERE order_id = %s"
            values = ('Cancelled', order_id)

            result = self.db_services.execute_query(query, values)

            if result is not None:
                print("Order cancelled successfully.")
            else:
                print("Failed to cancel the order.")
            return
        else:
            print("Order not found.")

    def get_total_amount(self):
        print(f"{CMD_COLOR_YELLOW}\nWhat products to Order: {CMD_COLOR_DEFAULT}")

        all_products = self.product_services.get_all_products()
        for p in all_products:
            print(p)
        selected_product_ids = input("Enter product IDs (comma-separated): ").split(',')

        total_amount = 0.0
        for product in all_products:
            if product.product_id in selected_product_ids:
                total_amount += product.price

        print(f"\nTotal Amount for Selected Products: ${total_amount:.2f}")
        return float(total_amount)

    def get_order_by_id(self, order_id):
        if not validate_id(order_id):
            raise InvalidIDError("Invalid order ID.")

        query = "SELECT * FROM Orders WHERE order_id = %s"
        result = self.db_services.execute_query(query, (order_id,))

        if result:
            order_data = result[0]
            return Order(*order_data)
        else:
            raise InvalidIDError("Customer Id not matching any records.")
