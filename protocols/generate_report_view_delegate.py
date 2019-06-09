from abc import ABC, abstractmethod


class GenerateReportViewDelegate(ABC):
    @abstractmethod
    def view_did_select_theses_assigned_to_researcher(self, view, researcher):
        raise NotImplementedError

    @abstractmethod
    def view_did_select_theses_between_dates(self, view, date1, date2):
        raise NotImplementedError

    @abstractmethod
    def view_did_select_theses_on_career(self, view, career):
        raise NotImplementedError
