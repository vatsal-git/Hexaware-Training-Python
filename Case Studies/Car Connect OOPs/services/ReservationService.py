import mysql.connector

from exceptions.DatabaseConnectionException import DatabaseConnectionException
from exceptions.ReservationException import ReservationException
from interfaces.IReservationService import IReservationService


class ReservationService(IReservationService):
    def __init__(self, db_context):
        self.db_context = db_context

    def get_reservation_by_id(self, reservation_id):
        query = "SELECT * FROM Reservation WHERE ReservationID = %s"
        params = (reservation_id,)

        try:
            cursor, connection = self.db_context.execute_query(query, params)
            fetched_reservation = cursor.fetchone()

            if fetched_reservation:
                return [*fetched_reservation]
            else:
                raise ReservationException(f"Reservation with ID {reservation_id} not found.")
        except mysql.connector.Error as err:
            raise DatabaseConnectionException(f"Error getting reservation: {err}")

    def get_reservations_by_customer_id(self, customer_id):
        query = "SELECT * FROM Reservation WHERE CustomerID = %s"
        params = (customer_id,)

        try:
            cursor, connection = self.db_context.execute_query(query, params)
            fetched_reservations = cursor.fetchall()

            if fetched_reservations and len(fetched_reservations) > 0:
                return [[*item] for item in fetched_reservations]
            else:
                raise ReservationException(f"No Reservations Found.")
        except mysql.connector.Error as err:
            raise DatabaseConnectionException(f"Error getting reservations: {err}")

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
            cursor, connection = self.db_context.execute_query(query, params)
            connection.commit()
        except mysql.connector.Error as err:
            raise DatabaseConnectionException(f"Error creating reservation: {err}")

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
            cursor, connection = self.db_context.execute_query(query, params)
            connection.commit()
        except mysql.connector.Error as err:
            raise DatabaseConnectionException(f"Error updating reservation: {err}")

    def cancel_reservation(self, reservation_id):
        query = "UPDATE Reservation SET Status = 'Canceled' WHERE ReservationID = %s"
        params = (reservation_id,)

        try:
            cursor, connection = self.db_context.execute_query(query, params)
            connection.commit()
        except mysql.connector.Error as err:
            raise DatabaseConnectionException(f"Error cancelling reservation: {err}")

    def get_reservation_history(self, vehicle_id):
        query = "SELECT * FROM Reservation WHERE VehicleID = %s"
        params = (vehicle_id,)

        try:
            cursor, connection = self.db_context.execute_query(query, params)
            fetched_reservations = cursor.fetchall()

            if fetched_reservations and len(fetched_reservations) > 0:
                return [[*item] for item in fetched_reservations]
            else:
                raise ReservationException(f"No Reservations Found.")
        except mysql.connector.Error as err:
            raise DatabaseConnectionException(f"Error getting reservations: {err}")

    def get_utilization_for_vehicle(self, vehicle_id):
        query = "SELECT COUNT(*) AS TotalReservations FROM Reservation WHERE VehicleID = %s"
        params = (vehicle_id,)

        try:
            cursor, connection = self.db_context.execute_query(query, params)
            fetched_reservation_count = cursor.fetchone()

            if fetched_reservation_count:
                total_reservations = fetched_reservation_count[0]
                return total_reservations
            else:
                raise ReservationException(f"No Utilization Found.")
        except mysql.connector.Error as err:
            raise DatabaseConnectionException(f"Error getting utilization: {err}")
