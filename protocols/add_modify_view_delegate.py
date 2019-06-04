from abc import ABC, abstractmethod


class AddModifyViewDelegate(ABC):
    @abstractmethod
    def view_did_press_add_button(self, view, data):
        raise NotImplementedError

    @abstractmethod
    def view_did_press_modify_button(self, view, data):
        raise NotImplementedError
