from exceptions.ReservationException import ReservationException
from interfaces.IReservationService import IReservationService
from entities.Reservation import Reservation


class ReservationService(IReservationService):
    def __init__(self, db_context):
        self.db_context = db_context

    def get_reservation_by_id(self, reservation_id):
        query = "SELECT * FROM Reservation WHERE ReservationID = %s"
        params = (reservation_id,)
        result = self.db_context.execute_query(query, params)
        if result:
            return Reservation(**result[0])

    def get_reservations_by_customer_id(self, customer_id):
        query = "SELECT * FROM Reservation WHERE CustomerID = %s"
        params = (customer_id,)
        results = self.db_context.execute_query(query, params)
        return [Reservation(**res) for res in results]

    def create_reservation(self, reservation_data):
        query = "INSERT INTO Reservation (CustomerID, VehicleID, StartDate, EndDate, TotalCost, Status) VALUES (%s, %s, %s, %s, %s, %s)"
        params = (
            reservation_data['CustomerID'],
            reservation_data['VehicleID'],
            reservation_data['StartDate'],
            reservation_data['EndDate'],
            reservation_data['TotalCost'],
            reservation_data['Status']
        )
        try:
            self.db_context.execute_query(query, params)
            return True
        except Exception as e:
            raise ReservationException(f"Failed to create reservation: {str(e)}")

    def update_reservation(self, reservation_data):
        query = "UPDATE Reservation SET StartDate = %s, EndDate = %s, TotalCost = %s, Status = %s WHERE ReservationID = %s"
        params = (
            reservation_data['StartDate'],
            reservation_data['EndDate'],
            reservation_data['TotalCost'],
            reservation_data['Status'],
            reservation_data['ReservationID']
        )
        try:
            self.db_context.execute_query(query, params)
            return True
        except Exception as e:
            raise ReservationException(f"Failed to update reservation: {str(e)}")

    def cancel_reservation(self, reservation_id):
        query = "UPDATE Reservation SET Status = 'Canceled' WHERE ReservationID = %s"
        params = (reservation_id,)
        try:
            self.db_context.execute_query(query, params)
            return True
        except Exception as e:
            raise ReservationException(f"Failed to cancel reservation: {str(e)}")

    def get_reservation_history(self, vehicle_id):
        query = "SELECT * FROM Reservation WHERE VehicleID = %s"
        params = (vehicle_id,)
        reservations = self.db_context.execute_query(query, params)
        return reservations

    def get_utilization_for_vehicle(self, vehicle_id):
        query = "SELECT COUNT(*) AS TotalReservations FROM Reservation WHERE VehicleID = %s"
        params = (vehicle_id,)
        total_reservations = self.db_context.execute_query(query, params)

        if not total_reservations:
            return None

        total_available_days = 365  # Suppose a car can be used for only 1 year

        if total_available_days is not None:
            utilization_percentage = (total_reservations / total_available_days) * 100
            return utilization_percentage
        else:
            return None
