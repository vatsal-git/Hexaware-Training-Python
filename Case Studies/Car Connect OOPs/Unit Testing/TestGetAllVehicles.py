import unittest
from entities.Vehicle import Vehicle
from services.VehicleService import VehicleService
from services.DatabaseContext import DatabaseContext


class TestGetAllVehicles(unittest.TestCase):
    def setUp(self):
        db_context = DatabaseContext(database="CarConnect")
        db_context.connect()
        self.vehicle_service = VehicleService(db_context)

    def test_get_all_vehicles(self):
        test_vehicles = [
            {
                'Model': 'Toyota Corolla',
                'Make': 'Toyota',
                'Year': 2022,
                'Color': 'Silver',
                'RegistrationNumber': '1sadasd',
                'Availability': 'y',
                'DailyRate': 50.00,
            },
            {
                'Model': 'Honda Accord',
                'Make': 'Honda',
                'Year': 2023,
                'Color': 'Blue',
                'RegistrationNumber': '2dasdsa',
                'Availability': 'y',
                'DailyRate': 60.00,
            },
            {
                'Model': 'Ford Mustang',
                'Make': 'Ford',
                'Year': 2021,
                'Color': 'Red',
                'RegistrationNumber': '3asdas',
                'Availability': 'n',
                'DailyRate': 70.00,
            },
        ]

        for vehicle_data in test_vehicles:
            self.vehicle_service.add_vehicle(vehicle_data, isTest=True)

        all_vehicles = self.vehicle_service.get_all_vehicles()
        self.assertGreaterEqual(len(all_vehicles), len(test_vehicles))


if __name__ == '__main__':
    unittest.main()
