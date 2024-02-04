class Reservation:
    def __init__(self, reservation_id, customer_id, vehicle_id, start_date, end_date, total_cost, status):
        self.__ReservationID = reservation_id
        self.__CustomerID = customer_id
        self.__VehicleID = vehicle_id
        self.__StartDate = start_date
        self.__EndDate = end_date
        self.__TotalCost = total_cost
        self.__Status = status

    # Getter methods with @property decorator
    @property
    def reservation_id(self):
        return self.__ReservationID

    @property
    def customer_id(self):
        return self.__CustomerID

    @property
    def vehicle_id(self):
        return self.__VehicleID

    @property
    def start_date(self):
        return self.__StartDate

    @property
    def end_date(self):
        return self.__EndDate

    @property
    def total_cost(self):
        return self.__TotalCost

    @property
    def status(self):
        return self.__Status

    # Setter methods with @<property_name>.setter decorator
    @reservation_id.setter
    def reservation_id(self, reservation_id):
        self.__ReservationID = reservation_id

    @customer_id.setter
    def customer_id(self, customer_id):
        self.__CustomerID = customer_id

    @vehicle_id.setter
    def vehicle_id(self, vehicle_id):
        self.__VehicleID = vehicle_id

    @start_date.setter
    def start_date(self, start_date):
        self.__StartDate = start_date

    @end_date.setter
    def end_date(self, end_date):
        self.__EndDate = end_date

    @total_cost.setter
    def total_cost(self, total_cost):
        self.__TotalCost = total_cost

    @status.setter
    def status(self, status):
        self.__Status = status

    def calculate_total_cost(self):
        pass