import mysql.connector

from exceptions.DatabaseConnectionException import DatabaseConnectionException
from exceptions.ReservationException import ReservationException


class ReportGenerator:
    def __init__(self, db_context, reservation_service=None, vehicle_service=None):
        self.reservation_service = reservation_service
        self.vehicle_service = vehicle_service
        self.db_context = db_context

    def generate_reservation_report(self, reservation_id):
        reservation = self.reservation_service.get_reservation_by_id(reservation_id)
        if reservation:
            report = f"Reservation Report\nReservation ID: {reservation.get_reservation_id()}\nCustomer: {reservation.get_customer().get_full_name()}\nVehicle: {reservation.get_vehicle().get_model()}"
            return report
        return "Reservation not found."

    def generate_vehicle_report(self, vehicle_id):
        vehicle = self.vehicle_service.get_vehicle_by_id(vehicle_id)
        if vehicle:
            report = f"Vehicle Report\nVehicle ID: {vehicle.get_vehicle_id()}\nModel: {vehicle.get_model()}\nMake: {vehicle.get_make()}\nYear: {vehicle.get_year()}"
            return report
        return "Vehicle not found."

    def view_overall_revenue(self):
        query = "SELECT SUM(TotalCost) AS OverallRevenue FROM Reservation WHERE Status = 'completed'"

        try:
            cursor, connection = self.db_context.execute_query(query)
            fetched_overall_revenue = cursor.fetchone()

            if fetched_overall_revenue:
                overall_revenue = fetched_overall_revenue[0]
                return overall_revenue if overall_revenue else 0
            else:
                raise ReservationException(f"No Revenue found.")
        except mysql.connector.Error as err:
            raise DatabaseConnectionException(f"Error getting revenue: {err}")
