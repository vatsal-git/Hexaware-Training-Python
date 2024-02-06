from entities.Product import Product


class Clothing(Product):
    def __init__(self, productName, description, price, quantityInStock, productType, size, color):
        super().__init__(productName, description, price, quantityInStock, productType)
        self.__size = size
        self.__color = color

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        self.__color = value
