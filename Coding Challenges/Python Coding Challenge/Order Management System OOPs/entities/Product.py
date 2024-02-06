class Product:
    def __init__(self, productName, description, price, quantityInStock, productType):
        # self.__product_id = productId  #  Made ID auto-increment
        self.__product_name = productName
        self.__description = description
        self.__price = price
        self.__quantity_in_stock = quantityInStock
        self.__type = productType

    #  Made ID auto-increment
    # @property
    # def product_id(self):
    #     return self.__product_id
    #
    # @product_id.setter
    # def product_id(self, value):
    #     self.__product_id = value

    @property
    def product_name(self):
        return self.__product_name

    @product_name.setter
    def product_name(self, value):
        self.__product_name = value

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value

    @property
    def quantity_in_stock(self):
        return self.__quantity_in_stock

    @quantity_in_stock.setter
    def quantity_in_stock(self, value):
        self.__quantity_in_stock = value

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        self.__type = value
