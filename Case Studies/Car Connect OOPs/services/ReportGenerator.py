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
        query = "SELECT SUM(TotalCost) AS OverallRevenue FROM Reservation"
        result = self.db_context.execute_query(query)

        if result:
            overall_revenue = result[0]['OverallRevenue']
            print(f"Overall Revenue: ${overall_revenue:.2f}")
        else:
            print("No revenue data available.")
