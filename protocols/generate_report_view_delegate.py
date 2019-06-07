from abc import ABC, abstractmethod


class GenerateReportViewDelegate(ABC):
    @abstractmethod
    def view_did_select_theses_assigned_to_researcher(self, view):
        raise NotImplementedError

    @abstractmethod
    def view_did_select_theses_between_dates(self, view):
        raise NotImplementedError

    @abstractmethod
    def view_did_select_theses_on_career(self, view):
        raise NotImplementedError
