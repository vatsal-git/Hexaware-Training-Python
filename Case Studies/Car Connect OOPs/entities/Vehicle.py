class Vehicle:
    def __init__(self, vehicle_id, model, make, year, color, registration_number, availability, daily_rate):
        self.__VehicleID = vehicle_id
        self.__Model = model
        self.__Make = make
        self.__Year = year
        self.__Color = color
        self.__RegistrationNumber = registration_number
        self.__Availability = availability
        self.__DailyRate = daily_rate

    # Getter methods with @property decorator
    @property
    def vehicle_id(self):
        return self.__VehicleID

    @property
    def model(self):
        return self.__Model

    @property
    def make(self):
        return self.__Make

    @property
    def year(self):
        return self.__Year

    @property
    def color(self):
        return self.__Color

    @property
    def registration_number(self):
        return self.__RegistrationNumber

    @property
    def availability(self):
        return self.__Availability

    @property
    def daily_rate(self):
        return self.__DailyRate

    # Setter methods with @<property_name>.setter decorator
    @vehicle_id.setter
    def vehicle_id(self, vehicle_id):
        self.__VehicleID = vehicle_id

    @model.setter
    def model(self, model):
        self.__Model = model

    @make.setter
    def make(self, make):
        self.__Make = make

    @year.setter
    def year(self, year):
        self.__Year = year

    @color.setter
    def color(self, color):
        self.__Color = color

    @registration_number.setter
    def registration_number(self, registration_number):
        self.__RegistrationNumber = registration_number

    @availability.setter
    def availability(self, availability):
        self.__Availability = availability

    @daily_rate.setter
    def daily_rate(self, daily_rate):
        self.__DailyRate = daily_rate
