from models.product import Product
from utils.exceptions import InvalidIDError, InsufficientStockException


class InventoryServices:
    def __init__(self, db_services, product_services):
        self.db_services = db_services
        self.product_services = product_services

    def add_product_to_inventory(self):
        product_id = int(input("Enter id for product to add to inventory: "))

        # Check if the product ID already exists in the inventory
        existing_inventory = self.get_inventory_by_product_id(product_id)

        if existing_inventory is not None:
            # Product already exists in the inventory, increment quantity
            new_quantity = existing_inventory.quantity_in_stock + 1
            self.update_stock_quantity(product_id, new_quantity)
            print(f"Product '{existing_inventory.product_name}' quantity updated to {new_quantity}.")

        else:
            # Product does not exist in the inventory, add a new row
            query = '''
            INSERT INTO Inventory (product_id, quantity)
            VALUES (%s, %s)
            '''
            values = (product_id, 1)
            self.db_services.execute_query(query, values)

    def update_stock_quantity(self, new_product_id=None, new_quantity=None):
        if new_product_id is None:
            product_id = int(input("Enter product ID to update stock quantity: "))
        else:
            product_id = new_product_id

        product = self.product_services.get_product_by_id(product_id)

        if product:
            if new_product_id is None:
                quantity = int(input("Enter new stock quantity: "))
            else:
                quantity = new_quantity

            # Update stock quantity in the inventory
            query = "UPDATE Products SET stock_quantity = %s WHERE product_id = %s"
            values = (quantity, product_id)
            self.db_services.execute_query(query, values)

            print("Stock quantity updated successfully.")
        else:
            raise InvalidIDError("Product ID not matching any records.")

    def remove_product_from_inventory(self):
        product_id = int(input("Enter product ID to remove from the inventory: "))
        inventory_data = self.get_inventory_by_product_id(product_id)

        if inventory_data.quantity >= 1:
            # Remove product from the inventory
            self.update_stock_quantity(product_id, inventory_data.quantity - 1)
            print("One quantity of Product removed from the inventory successfully.")
        else:
            raise InvalidIDError("Product ID not matching any records.")

    def list_low_stock_products(self, threshold=10):
        # List products with low stock (e.g., stock less than a threshold)
        query = "SELECT * FROM Products WHERE stock_quantity < %s"
        result = self.db_services.execute_query(query, (threshold,))

        if result:
            products = [Product(*product_data) for product_data in result]
            self.display_product_list(products)
        else:
            print("No products with low stock.")

    def list_out_of_stock_products(self):
        # List products that are out of stock
        query = "SELECT * FROM Products WHERE stock_quantity = 0"
        result = self.db_services.execute_query(query)

        if result:
            products = [Product(*product_data) for product_data in result]
            self.display_product_list(products)
        else:
            print("No out-of-stock products.")

    def get_inventory_by_product_id(self, product_id):
        query = "SELECT * FROM Inventory WHERE product_id = %s"
        result = self.db_services.execute_query(query, (product_id,))

        if result:
            inventory_data = [inventory_data for inventory_data in result]
            return inventory_data
        else:
            print("No out-of-stock products.")

    def get_product_details(self, product_id):
        # Get details of a specific product in the inventory
        product = self.product_services.get_product_by_id(product_id)

        if product:
            product.get_product_details()
        else:
            raise InvalidIDError("Product ID not matching any records.")

    def check_stock_availability(self, product_id, quantity):
        # Check if there is sufficient stock for a product
        product = self.product_services.get_product_by_id(product_id)

        if product and product.stock_quantity >= quantity:
            return True
        else:
            raise InsufficientStockException("Insufficient stock for the requested quantity.")

    @staticmethod
    def display_product_list(products):
        for product in products:
            product.get_product_details()
            print("-" * 30)
