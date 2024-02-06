from entities.Product import Product


class Electronics(Product):
    def __init__(self, productName, description, price, quantityInStock, productType, brand, warrantyPeriod):
        super().__init__(productName, description, price, quantityInStock, productType)
        self.__brand = brand
        self.__warranty_period = warrantyPeriod

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, value):
        self.__brand = value

    @property
    def warranty_period(self):
        return self.__warranty_period

    @warranty_period.setter
    def warranty_period(self, value):
        self.__warranty_period = value
