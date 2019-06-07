from abc import ABC, abstractmethod


class OptionsMenuViewDelegate(ABC):
    @abstractmethod
    def view_did_select_option(self, view, option):
        raise NotImplementedError
