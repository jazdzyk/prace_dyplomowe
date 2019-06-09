from PyQt5.QtWidgets import QLineEdit, QComboBox

from protocols import AddModifyViewDelegate
from view import BaseAddModifyView


class AddResearcherView(BaseAddModifyView):
    def __init__(self, parent, delegate: AddModifyViewDelegate = None, title_prefix="Dodawanie"):
        BaseAddModifyView.__init__(self, parent, title_prefix=title_prefix, title_suffix="Pracownika naukowego")
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
        self._combo_box_items = [
            self._degrees,
            self._faculties,
            self._academic_departments
        ]

    def _set_up_ui(self):
        if self._title_prefix == "Dodawanie":
            delegate_function = self._delegate.view_did_press_add_button
        else:
            delegate_function = self._delegate.view_did_press_modify_button
        self._create_layout(fields=self._fields,
                            delegate_function=delegate_function)
        self._add_callbacks()

    @property
    def _degrees(self):
        results = self._db_manager.query(f"""
        SELECT nazwaStopniaNaukowego FROM StopienNaukowy
        """)
        return (result[0] for result in results)

    @property
    def _faculties(self):
        results = self._db_manager.query(f"""
        SELECT nazwaWydzialu FROM Wydzial
        """)
        return (result[0] for result in results)

    @property
    def _academic_departments(self):
        results = self._db_manager.query(f"""
        SELECT nazwaKatedry FROM Katedra
        WHERE id_Wydzial = 2
        """)
        return (result[0] for result in results)
