from entities.Product import Product
from entities.User import User
from exceptions.OrderNotFoundException import OrderNotFoundException
from exceptions.OrderRetrievalError import OrderRetrievalError
from exceptions.ProductCreationError import ProductCreationError
from exceptions.ProductRetrievalError import ProductRetrievalError
from exceptions.UnauthorizedUserError import UnauthorizedUserError
from exceptions.UserNotFoundException import UserNotFoundException
from exceptions.UserRetrievalError import UserRetrievalError
from services.OrderProcessor import OrderProcessor
from utils.DBUtil import DBUtil


class OrderManagement:
    def __init__(self, new_order_processor):
        self.order_processor = new_order_processor

    @staticmethod
    def display_menu():
        print("\nOrder Management System Menu:")
        print("1. Create User")
        print("2. Create Product")
        print("3. Create Order")
        print("4. Cancel Order")
        print("5. Get All Products")
        print("6. Get Orders by User")
        print("7. Exit")

    def main(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == "1":   # Create User
                username = input("\nEnter Username: ")
                password = input("Enter Password: ")
                role = input("Enter Role (Admin/User): ")

                user = User(username, password, role)
                result = self.order_processor.createUser(user)
                print(result)

            elif choice == "2":  # Create Product
                username = input("\nEnter Username: ")
                password = input("Enter Password: ")

                try:
                    user, user_id = self.order_processor.getUserByUsernameAndPassword(username, password)
                    if user.role == "User":
                        raise UnauthorizedUserError("Permission denied. User must be an Admin to create a product.")

                    product_name = input("\nEnter Product Name: ")
                    description = input("Enter Product Description: ")
                    price = float(input("Enter Product Price: "))
                    quantity_in_stock = int(input("Enter Quantity in Stock: "))
                    product_type = input("Enter Product Type (Electronics/Clothing): ")

                    product = Product(product_name, description, price, quantity_in_stock, product_type)

                    try:
                        result = self.order_processor.createProduct(product)
                        print(result)

                    except ProductCreationError as e:
                        print(f"Error: {e}")

                except UnauthorizedUserError as e:
                    print(f"Error: {e}")

                except UserNotFoundException as e:
                    print(f"Error: {e}")

            elif choice == "3":  # Create Order
                username = input("\nEnter Username: ")
                password = input("Enter Password: ")

                try:
                    user, user_id = self.order_processor.getUserByUsernameAndPassword(username, password)

                    # Display a list of available products
                    products = self.order_processor.getAllProducts()
                    print("\nAvailable Products:")
                    for product in products:
                        print(f"{product['product_id']}. {product['product_name']} - ${product['price']}")

                    # Take input for multiple products to be added to the order
                    product_input = input("Enter Product IDs to add to the order (comma-separated): ")
                    product_ids = [int(product_id) for product_id in product_input.split(",")]

                    # Add products to the order
                    result = self.order_processor.addToOrder(user_id, product_ids)
                    print(result)

                except (UserNotFoundException, UserRetrievalError, ProductRetrievalError, UnauthorizedUserError) as e:
                    print(f"Error: {e}")

            elif choice == "4":  # Cancel Order
                username = input("\nEnter Username: ")
                password = input("Enter Password: ")
                order_id = int(input("Enter Order ID: "))

                try:
                    user, user_id = self.order_processor.getUserByUsernameAndPassword(username, password)
                    result = self.order_processor.cancelOrder(user_id, order_id)
                    print(result)
                except OrderNotFoundException as e:
                    print(f"Error: {e}")

            elif choice == "5":  # Get All Products
                try:
                    products = self.order_processor.getAllProducts()
                    print("\nAll Products:")
                    for product in products:
                        print(product)
                except ProductRetrievalError as e:
                    print(f"Error: {e}")

            elif choice == "6":  # Get Orders by User
                user_id = int(input("Enter User ID: "))

                try:
                    orders = self.order_processor.getOrderByUser(user_id)
                    print(f"Orders for User {user_id}:")
                    for order in orders:
                        print(order)
                except OrderRetrievalError as e:
                    print(f"Error: {e}")

            elif choice == "7":
                print("Exiting Order Management System.")
                break

            else:
                print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    db_context = DBUtil()
    order_processor = OrderProcessor(db_context)
    order_management = OrderManagement(order_processor)
    order_management.main()
