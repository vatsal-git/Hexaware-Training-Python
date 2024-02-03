from models.product import Product
from utils.constants import CMD_COLOR_YELLOW,  CMD_COLOR_DEFAULT
from utils.exceptions import InvalidIDError, InvalidStringError
from utils.validations import validate_id


class ProductServices:
    def __init__(self, database_connector):
        self.db_services = database_connector

    def add_new_product(self):
        product = Product()
        product_input = self.take_product_input()

        # Validating Inputs
        product.product_name = product_input['product_name']
        product.description = product_input['description']
        product.price = product_input['price']
        product.category = product_input['category']

        # Check for duplicate product in the database
        if self.is_product_name_registered(product.product_name):
            raise InvalidStringError("Product with this name is already registered.")

        # Insert new product into the database using query method
        query = '''
        INSERT INTO Products (product_name, description, price, category)
        VALUES (%s, %s, %s, %s)
        '''
        values = (product.product_name, product.description, product.price, product.category)
        result = self.db_services.execute_query(query, values)

        if result is not None:
            print("Product added successfully.")
        return

    def update_product_information(self):
        product_id = int(input("Enter product ID to update: "))
        product = self.get_product_by_id(product_id)

        if product:
            product.update_product_info()
            update_input = self.take_product_input(update=True)

            # Validating Inputs
            if 'product_name' in update_input:
                product.product_name = update_input['product_name']
            if 'description' in update_input:
                product.description = update_input['description']
            if 'price' in update_input:
                product.price = update_input['price']
            if 'category' in update_input:
                product.category = update_input['category']

            # Update product information in the database using query method
            query = '''
            UPDATE Products
            SET product_name = %s, description = %s, price = %s, category = %s
            WHERE product_id = %s
            '''
            values = (
                update_input['product_name'],
                update_input['description'],
                update_input['price'],
                update_input['category'],
                product_id
            )
            result = self.db_services.execute_query(query, values)

            if result is not None:
                print("Product information updated successfully.")
            return
        else:
            raise InvalidIDError("Product Id not matching any records.")

    def remove_product(self):
        product_id = int(input("Enter product ID to remove: "))
        product = self.get_product_by_id(product_id)

        if product:
            # Check if the product has existing orders
            if self.has_existing_orders_for_product(product_id):
                raise InvalidIDError("Product has existing orders. Cannot remove.")

            # Remove product from the database using query method
            query = "DELETE FROM Products WHERE product_id = %s"
            result = self.db_services.execute_query(query, (product_id,))

            if result is not None:
                print("Product removed successfully.")
        else:
            raise InvalidIDError("Product Id not matching any records.")

    @staticmethod
    def take_product_input(update=False):
        print(f"{CMD_COLOR_YELLOW}\nGive Inputs{CMD_COLOR_DEFAULT}")

        if update:
            print("*Note - Leave the field empty to retain existing data.")

        # Input dictionary
        product_input = {
            'product_name': input("Enter new product name: ") if update else input("Enter product name: "),
            'description': input("Enter new description: ") if update else input("Enter description: "),
            'price': float(input("Enter new price: ")) if update else float(input("Enter price: ")),
            'category': input("Enter new category: ") if update else input("Enter category: ")
        }

        if update:
            update_input = {key: value for key, value in product_input.items() if len(value) != 0}
            return update_input

        return product_input

    def is_product_name_registered(self, product_name):
        query = "SELECT COUNT(*) FROM Products WHERE product_name = %s"
        result = self.db_services.execute_query(query, (product_name,))
        return result[0][0] > 0 if result else False

    def has_existing_orders_for_product(self, product_id):
        query = "SELECT COUNT(*) FROM Orders WHERE product_id = %s"
        result = self.db_services.execute_query(query, (product_id,))
        return result[0][0] > 0 if result else False

    def get_product_by_id(self, product_id):
        if not validate_id(product_id):
            raise InvalidIDError("Invalid product ID.")

        query = "SELECT * FROM Products WHERE product_id = %s"
        result = self.db_services.execute_query(query, (product_id,))

        if result:
            product_data = result[0]
            return Product(*product_data)
        else:
            raise InvalidIDError("Product ID not matching any records.")

    def get_all_products(self, search_str=None):
        if search_str is not None:
            # If search string is provided, modify the query to search for the product name or description
            query = """
             SELECT * FROM Products
             WHERE product_name LIKE %s OR description LIKE %s
             """
            search_pattern = f"%{search_str}%"
            values = (search_pattern, search_pattern)
        else:
            # If no search string, retrieve all products
            query = "SELECT * FROM Products"
            values = None

        result = self.db_services.execute_query(query, values)

        if result:
            products = [Product(*product_data) for product_data in result]
            return products
        else:
            return None
