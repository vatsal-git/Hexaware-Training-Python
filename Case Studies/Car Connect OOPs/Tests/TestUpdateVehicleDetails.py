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
            'VehicleID': 1,
            'Model': 'Updated Model',
            'Make': 'Updated Make',
            'Year': 2023,
            'Color': 'Updated Color',
            'RegistrationNumber': 'Updated123',
            'Availability': False,
            'DailyRate': 60.0
        }
        self.vehicle_service.update_vehicle(updated_vehicle_data)

        updated_vehicle_result = self.vehicle_service.get_vehicle_by_id(updated_vehicle_data['VehicleID'])
        updated_vehicle = Vehicle(*updated_vehicle_result[0])

        # Check if the details have been updated correctly
        self.assertEqual(updated_vehicle.model, 'Updated Model')
        self.assertEqual(updated_vehicle.make, 'Updated Make')
        self.assertEqual(updated_vehicle.year, 2023)
        self.assertEqual(updated_vehicle.color, 'Updated Color')
        self.assertEqual(updated_vehicle.registration_number, 'Updated123')
        self.assertFalse(updated_vehicle.availability)
        self.assertEqual(updated_vehicle.daily_rate, 60.0)


if __name__ == '__main__':
    unittest.main()
