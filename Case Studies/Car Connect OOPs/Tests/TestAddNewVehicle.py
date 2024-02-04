import unittest

from entities.Vehicle import Vehicle
from services.VehicleService import VehicleService
from services.DatabaseContext import DatabaseContext


class TestAddNewVehicle(unittest.TestCase):
    def setUp(self):
        self.db_context = DatabaseContext(database="CarConnect")
        self.db_context.connect()
        self.vehicle_service = VehicleService(self.db_context)

    def test_add_new_vehicle(self):
        new_vehicle_data = {
            'Model': 'r15',
            'Make': 'Yamaha',
            'Year': 2023,
            'Color': 'Black',
            'RegistrationNumber': 'GJ05123',
            'Availability': 'y',  # y for True and n for False
            'DailyRate': 500.00,
        }

        try:
            self.vehicle_service.add_vehicle(new_vehicle_data)
            curr_cursor = self.db_context.get_current_cursor()
            new_vehicle_id = curr_cursor.lastrowid

            added_vehicle_result = self.vehicle_service.get_vehicle_by_id(new_vehicle_id)
            added_vehicle = Vehicle(*added_vehicle_result[0])

            self.assertIsNotNone(added_vehicle)
            self.assertEqual(new_vehicle_data['Model'], added_vehicle.model)
            self.assertEqual(new_vehicle_data['Make'], added_vehicle.make)
            self.assertEqual(new_vehicle_data['Year'], added_vehicle.year)
            self.assertEqual(new_vehicle_data['Color'], added_vehicle.color)
            self.assertEqual(new_vehicle_data['RegistrationNumber'], added_vehicle.registration_number)
            self.assertEqual(new_vehicle_data['Availability'], 'y' if added_vehicle.availability == 1 else 'n')
            self.assertEqual(new_vehicle_data['DailyRate'], added_vehicle.daily_rate)

        except Exception as e:
            self.fail(f"Exception raised: {e}")


if __name__ == '__main__':
    unittest.main()
