from PyQt5.QtWidgets import QLineEdit

from protocols import AddModifyViewDelegate
from view import BaseAddModifyView


class AddStudentView(BaseAddModifyView):
    def __init__(self, parent, delegate: AddModifyViewDelegate = None, title_prefix="Dodawanie"):
        BaseAddModifyView.__init__(self, parent, title_prefix=title_prefix, title_suffix="Studenta")
        self._delegate = delegate
        self._set_up_general()
        self._set_up_ui()

    def _set_up_general(self):
        BaseAddModifyView._set_up_general(self)
        self._fields = [
            ("Imię", QLineEdit),
            ("Nazwisko", QLineEdit),
            ("Telefon", QLineEdit),
            ("Email", QLineEdit),
            ("Numer indeksu", QLineEdit)
        ]

    def _set_up_ui(self):
        if self._title_prefix == "Dodawanie":
            delegate_function = self._delegate.view_did_press_add_button
        else:
            delegate_function = self._delegate.view_did_press_modify_button
        self._create_layout(fields=self._fields,
                            delegate_function=delegate_function)
        self._add_callbacks()
