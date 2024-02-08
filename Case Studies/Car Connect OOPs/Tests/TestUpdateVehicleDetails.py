import unittest

from entities.Vehicle import Vehicle
from services.DatabaseContext import DatabaseContext
from services.VehicleService import VehicleService


class TestUpdateVehicleDetails(unittest.TestCase):
    def setUp(self):
        self.db_context = DatabaseContext(database="CarConnect")
        self.db_context.connect()
        self.vehicle_service = VehicleService(self.db_context)

    def test_update_vehicle_details(self):
        updated_vehicle_data = {
            'VehicleID': 5,
            'Model': 'gggg',
            'Make': 'hhhh',
            'Year': 2023,
            'Color': 'yyyy',
            'RegistrationNumber': 'iiisi',
            'Availability': False,
            'DailyRate': 600.0
        }

        self.vehicle_service.update_vehicle(updated_vehicle_data, isTest=True)

        updated_vehicle_result = self.vehicle_service.get_vehicle_by_id(updated_vehicle_data['VehicleID'])
        updated_vehicle = Vehicle(*updated_vehicle_result)

        # Check if the details have been updated correctly
        self.assertEqual(updated_vehicle.model, updated_vehicle_data['Model'])
        self.assertEqual(updated_vehicle.make, updated_vehicle_data['Make'])
        self.assertEqual(updated_vehicle.year, updated_vehicle_data['Year'])
        self.assertEqual(updated_vehicle.color, updated_vehicle_data['Color'])
        self.assertEqual(updated_vehicle.registration_number, updated_vehicle_data['RegistrationNumber'])
        self.assertEqual(updated_vehicle.availability, 1 if updated_vehicle_data['Availability'] else 0)
        self.assertEqual(updated_vehicle.daily_rate, updated_vehicle_data['DailyRate'])


if __name__ == '__main__':
    unittest.main()
