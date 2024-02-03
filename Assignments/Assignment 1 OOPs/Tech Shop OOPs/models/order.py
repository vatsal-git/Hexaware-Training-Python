from models.customer import Customer
from utils.constants import ORDER_STATUS_ENUM
from utils.validations import (
    validate_id,
    validate_number,
    validate_past_date,
    validate_enum
)
from utils.exceptions import (
    InvalidIDError,
    InvalidInstanceError,
    InvalidNumberError,
    InvalidDateError,
    InvalidEnumError
)


class Order:
    def __init__(self, order_id=None, customer=None, order_date=None, total_amount=None, order_status=None):
        self.__OrderID = order_id
        self.__Customer = customer
        self.__OrderDate = order_date
        self.__TotalAmount = total_amount
        self.__OrderStatus = order_status

    # Getter methods
    @property
    def order_id(self):
        return self.__OrderID

    @property
    def customer(self):
        return self.__Customer

    @property
    def order_date(self):
        return self.__OrderDate

    @property
    def total_amount(self):
        return self.__TotalAmount

    @property
    def order_status(self):
        return self.__OrderStatus

    # Setter methods
    @order_id.setter
    def order_id(self, new_order_id):
        if validate_id(new_order_id):
            self.__OrderID = new_order_id
        else:
            raise InvalidIDError("Order ID should be a positive integer.")

    @customer.setter
    def customer(self, new_customer):
        if isinstance(new_customer, Customer):
            self.__Customer = new_customer
        else:
            raise InvalidInstanceError("Customer should be an instance of the Customer class.")

    @order_date.setter
    def order_date(self, new_order_date):
        if validate_past_date(new_order_date):
            self.__OrderDate = new_order_date
        else:
            raise InvalidDateError("Order date cannot be in the future.")

    @total_amount.setter
    def total_amount(self, new_total_amount):
        if validate_number(new_total_amount, float):
            self.__TotalAmount = new_total_amount
        else:
            raise InvalidNumberError("Total amount should be a posetive number.")

    @order_status.setter
    def order_status(self, new_order_status):
        if validate_enum(new_order_status, ORDER_STATUS_ENUM):
            self.__OrderStatus = new_order_status
        else:
            raise InvalidEnumError(f"Invalid order status. Allowed values are: {', '.join(ORDER_STATUS_ENUM)}")

    def calculate_total_amount(self):
        pass

    def get_order_details(self):
        print(f"Order ID: {self.order_id}")
        print(f"Order Date: {self.order_date}")
        print(f"Customer: {self.customer.first_name} {self.customer.last_name}")
        print(f"Total Amount: ${self.total_amount:.2f}")
        print(f"Order Status: {self.order_status}")

    def update_order_status(self, new_status):
        self.order_status = new_status

    def cancel_order(self):
        self.update_order_status('Cancelled')
