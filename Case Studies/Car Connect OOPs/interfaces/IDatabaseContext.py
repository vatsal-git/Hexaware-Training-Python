from abc import ABC, abstractmethod


class IDatabaseContext(ABC):
    @abstractmethod
    def connect(self, max_retries=3, retry_delay=2):
        pass

    @abstractmethod
    def disconnect(self):
        pass

    @abstractmethod
    def execute_query(self, query, values=None):
        pass
