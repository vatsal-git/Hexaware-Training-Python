import unittest

from entities.Vehicle import Vehicle
from services.VehicleService import VehicleService
from services.DatabaseContext import DatabaseContext


class TestGetAvailableVehicles(unittest.TestCase):
    def setUp(self):
        db_context = DatabaseContext(database="CarConnect")
        db_context.connect()
        self.vehicle_service = VehicleService(db_context)

    def test_get_available_vehicles(self):
        test_vehicles = [
            {
                'Model': 'Subaru BRZ',
                'Make': 'Subaru',
                'Year': 2022,
                'Color': 'Dark Gray',
                'RegistrationNumber': '534',
                'Availability': 'y',
                'DailyRate': 700.00,
            },
            {
                'Model': 'Mitsubishi Eclipse Cross',
                'Make': 'Mitsubishi',
                'Year': 2023,
                'Color': 'Deep Blue',
                'RegistrationNumber': '324',
                'Availability': 'n',
                'DailyRate': 750.00,
            },
            {
                'Model': 'Honda HR-V',
                'Make': 'Honda',
                'Year': 2021,
                'Color': 'Burgundy',
                'RegistrationNumber': '123',
                'Availability': 'y',
                'DailyRate': 720.00,
            },
        ]

        for vehicle_data in test_vehicles:
            self.vehicle_service.add_vehicle(vehicle_data, isTest=True)

        available_vehicles = self.vehicle_service.get_available_vehicles()
        for vehicle in available_vehicles:
            self.assertEqual(vehicle.availability,  1)


if __name__ == '__main__':
    unittest.main()
