from abc import ABC, abstractmethod


class DatabaseManagerDelegate(ABC):
    @abstractmethod
    def manager_reports_error(self, error):
        raise NotImplementedError
