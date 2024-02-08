import mysql.connector

from exceptions.DatabaseConnectionException import DatabaseConnectionException
from exceptions.VehicleNotFoundException import VehicleNotFoundException
from interfaces.IVehicleService import IVehicleService
from entities.Vehicle import Vehicle


class VehicleService(IVehicleService):
    def __init__(self, db_context):
        self.db_context = db_context

    def get_vehicle_by_id(self, vehicle_id):
        query = "SELECT * FROM Vehicle WHERE VehicleID = %s"
        params = (vehicle_id,)

        try:
            cursor, connection = self.db_context.execute_query(query, params)
            fetched_vehicle = cursor.fetchone()

            if fetched_vehicle:
                return [*fetched_vehicle]
            else:
                raise VehicleNotFoundException(f"Vehicle with ID {vehicle_id} not found.")
        except mysql.connector.Error as err:
            raise DatabaseConnectionException(f"Error getting vehicle: {err}")

    def get_available_vehicles(self):
        query = "SELECT * FROM Vehicle WHERE Availability = True"

        try:
            cursor, connection = self.db_context.execute_query(query)
            fetched_vehicles = cursor.fetchall()

            if fetched_vehicles and len(fetched_vehicles) > 0:
                return [[*item] for item in fetched_vehicles]
            else:
                raise VehicleNotFoundException(f"No Vehicles Available.")
        except mysql.connector.Error as err:
            raise DatabaseConnectionException(f"Error getting vehicles: {err}")

    def add_vehicle(self, vehicle_data):
        query = "INSERT INTO Vehicle (Model, Make, Year, Color, RegistrationNumber, Availability, DailyRate) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        params = (
            vehicle_data['Model'],
            vehicle_data['Make'],
            vehicle_data['Year'],
            vehicle_data['Color'],
            vehicle_data['RegistrationNumber'],
            1 if vehicle_data['Availability'] == 'y' else 0,
            vehicle_data['DailyRate']
        )

        try:
            cursor, connection = self.db_context.execute_query(query, params)
            connection.commit()
        except mysql.connector.Error as err:
            raise DatabaseConnectionException(f"Error getting vehicles: {err}")

    def update_vehicle(self, vehicle_data):
        query = "UPDATE Vehicle SET Model = %s, Make = %s, Year = %s, Color = %s, RegistrationNumber = %s, Availability = %s, DailyRate = %s WHERE VehicleID = %s"
        params = (
            vehicle_data['Model'],
            vehicle_data['Make'],
            vehicle_data['Year'],
            vehicle_data['Color'],
            vehicle_data['RegistrationNumber'],
            vehicle_data['Availability'],
            vehicle_data['DailyRate'],
            vehicle_data['VehicleID']
        )

        try:
            cursor, connection = self.db_context.execute_query(query, params)
            connection.commit()
        except mysql.connector.Error as err:
            raise DatabaseConnectionException(f"Error getting vehicles: {err}")

    def remove_vehicle(self, vehicle_id):
        # Delete associated reservations
        reservation_query = "DELETE FROM Reservation WHERE VehicleID = %s"
        reservation_params = (vehicle_id,)

        try:
            cursor, connection = self.db_context.execute_query(reservation_query, reservation_params)
            connection.commit()
        except mysql.connector.Error as err:
            raise DatabaseConnectionException(f"Error deleting associated reservations: {err}")

        query = "DELETE FROM Vehicle WHERE VehicleID = %s"
        params = (vehicle_id,)

        try:
            cursor, connection = self.db_context.execute_query(query, params)
            connection.commit()
        except mysql.connector.Error as err:
            raise DatabaseConnectionException(f"Error getting vehicles: {err}")

    def get_all_vehicles(self):
        query = "SELECT * FROM Vehicle"

        try:
            cursor, connection = self.db_context.execute_query(query)
            fetched_vehicles = cursor.fetchall()

            if fetched_vehicles:
                return [[*item] for item in fetched_vehicles]
            else:
                raise VehicleNotFoundException(f"No Vehicles Found.")
        except mysql.connector.Error as err:
            raise DatabaseConnectionException(f"Error getting vehicles: {err}")
