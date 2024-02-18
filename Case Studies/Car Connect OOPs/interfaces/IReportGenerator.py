from abc import ABC, abstractmethod


class IReportGenerator(ABC):

    @abstractmethod
    def get_reservation_history(self, vehicle_id):
        pass

    @abstractmethod
    def get_utilization_for_vehicle(self, vehicle_id):
        pass

    @abstractmethod
    def view_overall_revenue(self):
        pass
