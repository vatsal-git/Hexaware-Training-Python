import mysql.connector

from exceptions.DatabaseConnectionException import DatabaseConnectionException
from exceptions.ReservationException import ReservationException
from interfaces.IReportGenerator import IReportGenerator
from services.ReservationService import ReservationService
from services.VehicleService import VehicleService


class ReportGenerator(IReportGenerator, ReservationService, VehicleService):
    def __init__(self, db_context):
        super().__init__(db_context)
        self.db_context = db_context

    def get_reservation_history(self, vehicle_id):
        query = """
            SELECT r.ReservationID, CONCAT(c.FirstName, ' ', c.LastName) AS CustomerName, c.Email, c.PhoneNumber,  CONCAT(v.Make, ' ', v.Model) AS Vehicle, v.Color, v.RegistrationNumber, CONCAT(r.StartDate, ' - ', r.EndDate) AS Duration, r.TotalCost 
            FROM Reservation r 
            JOIN Vehicle v on v.VehicleID = r.VehicleID
            JOIN Customer c on c.CustomerID = r.CustomerID
            WHERE r.VehicleID = %s            
        """
        params = (vehicle_id,)

        try:
            cursor, connection = self.db_context.execute_query(query, params)
            fetched_reservations = cursor.fetchall()

            if fetched_reservations and len(fetched_reservations) > 0:
                return [[*item] for item in fetched_reservations]
            else:
                raise ReservationException("No Reservations Found.")
        except mysql.connector.Error as err:
            raise DatabaseConnectionException(f"Error getting reservations: {err}")

    def get_utilization_for_vehicle(self, vehicle_id):
        query = "SELECT SUM(DATEDIFF(EndDate, StartDate)) AS TotalDaysUsed FROM Reservation WHERE VehicleID = %s"
        params = (vehicle_id,)

        try:
            cursor, connection = self.db_context.execute_query(query, params)
            fetched_reservation_count = cursor.fetchone()

            if fetched_reservation_count:
                total_reservations = fetched_reservation_count[0]
                return (total_reservations / 10) * 100
            else:
                raise ReservationException("No Utilization Found.")
        except mysql.connector.Error as err:
            raise DatabaseConnectionException(f"Error getting utilization: {err}")

    def view_overall_revenue(self):
        query = "SELECT SUM(TotalCost) AS OverallRevenue FROM Reservation"

        try:
            cursor, connection = self.db_context.execute_query(query)
            fetched_overall_revenue = cursor.fetchone()

            if fetched_overall_revenue:
                overall_revenue = fetched_overall_revenue[0]
                return overall_revenue if overall_revenue else 0
            else:
                raise ReservationException("No Revenue found.")
        except mysql.connector.Error as err:
            raise DatabaseConnectionException(f"Error getting revenue: {err}")
