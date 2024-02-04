from abc import *


class IEventServices(ABC):
    @abstractmethod
    def create_event(self):
        pass

    @abstractmethod
    def get_event_details(self):
        pass

    @abstractmethod
    def get_available_tickets_count(self):
        pass
