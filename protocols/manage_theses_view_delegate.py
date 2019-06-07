from abc import ABC, abstractmethod


class ManageThesesViewDelegate(ABC):
    @abstractmethod
    def view_did_choose_to_manage_undefended_theses(self, view):
        raise NotImplementedError

    @abstractmethod
    def view_did_choose_to_manage_defended_theses(self, view):
        raise NotImplementedError

    @abstractmethod
    def view_did_select_displaying_data(self, view, data):
        raise NotImplementedError

    @abstractmethod
    def view_did_select_adding_review(self, view, data):
        raise NotImplementedError
