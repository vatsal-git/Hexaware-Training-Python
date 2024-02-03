from models.product import Product
from utils.validations import (
    validate_id,
    validate_number,
    validate_past_date
)
from utils.exceptions import (
    InvalidIDError,
    InvalidInstanceError,
    InvalidNumberError,
    InvalidDateError,
    InsufficientStockException
)


class Inventory:
    def __init__(self, inventory_id, product, quantity_in_stock, last_stock_update):
        self.__InventoryID = inventory_id
        self.__Product = product
        self.__QuantityInStock = quantity_in_stock
        self.__LastStockUpdate = last_stock_update

    # Getter methods
    @property
    def inventory_id(self):
        return self.__InventoryID

    @property
    def product(self):
        return self.__Product

    @property
    def quantity_in_stock(self):
        return self.__QuantityInStock

    @property
    def last_stock_update(self):
        return self.__LastStockUpdate

    # Setter methods
    @inventory_id.setter
    def inventory_id(self, new_inventory_id):
        if validate_id(new_inventory_id):
            self.__InventoryID = new_inventory_id
        else:
            raise InvalidIDError("Inventory ID should be a positive integer.")

    @product.setter
    def product(self, new_product):
        if isinstance(new_product, Product):
            self.__Product = new_product
        else:
            raise InvalidInstanceError("Product should be an instance of the Product class.")

    @quantity_in_stock.setter
    def quantity_in_stock(self, new_quantity_in_stock):
        if validate_number(new_quantity_in_stock):
            self.__QuantityInStock = new_quantity_in_stock
        else:
            raise InvalidNumberError("Quantity in stock should be a positive number.")

    @last_stock_update.setter
    def last_stock_update(self, new_last_stock_update):
        if validate_past_date(new_last_stock_update):
            self.__LastStockUpdate = new_last_stock_update
        else:
            raise InvalidDateError("Last stock update should be valid datetime.")

    def get_product(self):
        return self.product

    def get_quantity_in_stock(self):
        return self.quantity_in_stock

    def add_to_inventory(self, quantity):
        self.quantity_in_stock += quantity
        self.update_stock_quantity()

    def remove_from_inventory(self, quantity):
        if self.quantity_in_stock < quantity:
            self.quantity_in_stock -= quantity
            self.update_stock_quantity()
        else:
            raise InsufficientStockException()

    def update_stock_quantity(self, new_quantity=None):
        self.quantity_in_stock = new_quantity
        print("Stock quantity updated successfully.")

    def is_product_available(self):
        return self.quantity_in_stock > 0

    def get_inventory_value(self):
        return self.product.price * self.quantity_in_stock

    def list_low_stock_products(self, threshold):
        if self.quantity_in_stock < threshold:
            print(f"{self.product.product_name} is low in stock. Quantity: {self.quantity_in_stock}")

    def list_out_of_stock_products(self):
        if self.quantity_in_stock == 0:
            print(f"{self.product.product_name} is out of stock.")

    def list_all_products(self):
        print(f"Product: {self.product.product_name}, Quantity: {self.quantity_in_stock}")
