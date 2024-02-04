from exceptions.VehicleNotFoundException import VehicleNotFoundException
from interfaces.IVehicleService import IVehicleService
from entities.Vehicle import Vehicle


class VehicleService(IVehicleService):
    def __init__(self, db_context):
        self.db_context = db_context

    def get_vehicle_by_id(self, vehicle_id):
        query = "SELECT * FROM Vehicle WHERE VehicleID = %s"
        params = (vehicle_id,)
        result = self.db_context.execute_query(query, params)
        if result:
            return result
        else:
            raise VehicleNotFoundException(f"Vehicle with ID {vehicle_id} not found.")

    def get_available_vehicles(self):
        query = "SELECT * FROM Vehicle WHERE Availability = True"
        results = self.db_context.execute_query(query)
        return results

    def add_vehicle(self, vehicle_data):
        query = "INSERT INTO Vehicle (Model, Make, Year, Color, RegistrationNumber, Availability, DailyRate) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        params = (
            vehicle_data['Model'],
            vehicle_data['Make'],
            vehicle_data['Year'],
            vehicle_data['Color'],
            vehicle_data['RegistrationNumber'],
            1 if vehicle_data['Availability'] == 'y' or vehicle_data['Availability'] == 'Y' else 0,
            vehicle_data['DailyRate']
        )
        self.db_context.execute_query(query, params)

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
        self.db_context.execute_query(query, params)

    def remove_vehicle(self, vehicle_id):
        query = "DELETE FROM Vehicle WHERE VehicleID = %s"
        params = (vehicle_id,)
        self.db_context.execute_query(query, params)

    def get_all_vehicles(self):
        query = "SELECT * FROM Vehicle"
        results = self.db_context.execute_query(query)
        if not results:
            raise VehicleNotFoundException("No vehicles found.")
        return results
