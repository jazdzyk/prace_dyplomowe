from PyQt5.QtWidgets import QLineEdit, QComboBox

from protocols import AddModifyViewDelegate
from view import BaseAddModifyView


class AddResearcherView(BaseAddModifyView):
    def __init__(self, parent, delegate: AddModifyViewDelegate = None):
        BaseAddModifyView.__init__(self, parent, title_prefix="Dodawanie", title_suffix="Pracownika naukowego")
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
            ("Stopień naukowy", QComboBox),
            ("Wydział", QComboBox),
            ("Katedra", QComboBox)
        ]

    def _set_up_ui(self):
        self._create_layout(fields=self._fields,
                            delegate_function=self._delegate.view_did_press_add_button)
        self._add_callbacks(combo_box_items=[
            ("dr", "dr inż.", "dr hab.", "dr hab. inż.", "prof. nadzw.", "prof."),
            ("EAIIB", "IMiR", "IET"),
            ("pierwsza", "druga", "trzecia")
        ])
