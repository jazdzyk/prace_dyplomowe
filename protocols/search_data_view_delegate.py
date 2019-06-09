from abc import ABC, abstractmethod


class SearchDataViewDelegate(ABC):
    @abstractmethod
    def view_did_press_search_button(self, view, search_query_text):
        raise NotImplementedError

    @abstractmethod
    def view_did_choose_to_display_students(self, view):
        raise NotImplementedError

    @abstractmethod
    def view_did_choose_to_display_researchers(self, view):
        raise NotImplementedError

    @abstractmethod
    def view_did_choose_to_display_theses(self, view):
        raise NotImplementedError

    @abstractmethod
    def view_did_toggle_search_range_option(self, view, search_range_option):
        raise NotImplementedError

    @abstractmethod
    def view_wants_to_display_detailed_data(self, view, selected_row):
        raise NotImplementedError
