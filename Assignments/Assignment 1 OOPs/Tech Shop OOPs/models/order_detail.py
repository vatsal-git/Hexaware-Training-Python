from models.order import Order
from models.product import Product
from utils.exceptions import InvalidIDError, InvalidInstanceError, InvalidNumberError, IncompleteOrderException
from utils.validations import validate_id, validate_number


class OrderDetail:
    def __init__(self, order_detail_id, order, product, quantity):
        if product is None or order is None:
            raise IncompleteOrderException()

        self.__OrderDetailID = order_detail_id
        self.__Order = order
        self.__Product = product
        self.__Quantity = quantity

    # Getter methods
    @property
    def order_detail_id(self):
        return self.__OrderDetailID

    @property
    def order(self):
        return self.__Order

    @property
    def product(self):
        return self.__Product

    @property
    def quantity(self):
        return self.__Quantity

    # Setter methods
    @order_detail_id.setter
    def order_detail_id(self, new_order_detail_id):
        if validate_id(new_order_detail_id):
            self.__OrderDetailID = new_order_detail_id
        else:
            raise InvalidIDError("Order detail ID should be a positive integer.")

    @order.setter
    def order(self, new_order):
        if isinstance(new_order, Order):
            self.__Order = new_order
        else:
            raise InvalidInstanceError("Order should be an instance of the Order class.")

    @product.setter
    def product(self, new_product):
        if isinstance(new_product, Product):
            self.__Product = new_product
        else:
            raise InvalidInstanceError("Product should be an instance of the Product class.")

    @quantity.setter
    def quantity(self, new_quantity):
        if validate_number(new_quantity, int):
            self.__Quantity = new_quantity
        else:
            raise InvalidNumberError("Quantity should be a positive integer.")

    def calculate_subtotal(self):
        return self.__Quantity * self.__Product.price

    def get_order_detail_info(self):
        print(f"Order Detail ID: {self.order_detail_id}")
        print(f"Product: {self.product.product_name}")
        print(f"Quantity: {self.quantity}")
        print(f"Subtotal: ${self.calculate_subtotal():.2f}")

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity
        print("Quantity updated successfully.")

    def add_discount(self, discount_percent):
        if validate_number(discount_percent, data_type=float, max_value=101):
            self.product.price = self.product.price * (1 - discount_percent/100)
            print(f"Discount applied successfully. New product price is {self.product.price}")
        else:
            raise InvalidNumberError("Discount should be between 0% to 100%")
