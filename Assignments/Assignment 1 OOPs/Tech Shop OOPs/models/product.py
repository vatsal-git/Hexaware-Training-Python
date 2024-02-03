from utils.exceptions import InvalidIDError, InvalidStringError, InvalidNumberError
from utils.validations import validate_id, validate_string, validate_number


class Product:
    def __init__(self, product_id=None, product_name=None, description=None, price=None, category=None):
        self.__ProductID = product_id
        self.__ProductName = product_name
        self.__Description = description
        self.__Price = price
        self.__Category = category

    # Getter methods
    @property
    def product_id(self):
        return self.__ProductID

    @property
    def product_name(self):
        return self.__ProductName

    @property
    def description(self):
        return self.__Description

    @property
    def price(self):
        return self.__Price

    @property
    def category(self):
        return self.__Category

        # Setter methods

    @product_id.setter
    def product_id(self, new_product_id):
        if validate_id(new_product_id):
            self.__ProductID = new_product_id
        else:
            raise InvalidIDError("Product ID should be a positive integer.")

    @product_name.setter
    def product_name(self, new_product_name):
        if validate_string(new_product_name):
            self.__ProductName = new_product_name
        else:
            raise InvalidStringError("Product name cannot be empty.")

    @description.setter
    def description(self, new_description):
        if validate_string(new_description, min_len=10):
            self.__Description = new_description
        else:
            raise InvalidStringError("Description should have at least 10 characters.")

    @price.setter
    def price(self, new_price):
        if validate_number(new_price, float):
            self.__Price = new_price
        else:
            raise InvalidNumberError("Price should be a positive number.")

    @category.setter
    def category(self, new_category):
        if validate_string(new_category):
            self.__Category = new_category
        else:
            raise InvalidStringError("Category name cannot be empty.")

    def get_product_details(self):
        print(f"Product ID: {self.product_id}")
        print(f"Product Name: {self.product_name}")
        print(f"Description: {self.description}")
        print(f"Price: ${self.price:.2f}")
        print(f"Price: {self.category}")

    def update_product_info(self, new_price=None, new_description=None, new_category=None):
        if new_price is not None:
            self.price = new_price
        if new_description is not None:
            self.description = new_description
        if new_category is not None:
            self.category = new_category
        print("Product information updated successfully.")

    @staticmethod
    def is_product_in_stock(product_id_to_check):
        pass
