from PyQt5.QtWidgets import QLineEdit, QComboBox, QDateEdit

from protocols import AddModifyViewDelegate
from view import BaseAddModifyView


class AddDefenseView(BaseAddModifyView):
    def __init__(self, parent, delegate: AddModifyViewDelegate = None, title_prefix="Dodawanie"):
        BaseAddModifyView.__init__(self, parent, title_prefix=title_prefix, title_suffix="Obrony")
        self._delegate = delegate
        self._set_up_general()
        self._set_up_ui()

    def _set_up_general(self):
        BaseAddModifyView._set_up_general(self)
        self._fields = [
            ("Praca dyplomowa", QComboBox),
            ("Przewodniczący komisji", QComboBox),
            ("Miejsce obrony", QComboBox),
            ("Data obrony", QDateEdit),
            ("Ocena końcowa", QLineEdit)
        ]
        self._combo_box_items = [
            self._theses,
            self._researchers,
            self._places
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
    def _theses(self):
        results = self._db_manager.query(f"""
                SELECT tytul FROM PraceDyplomowe
                """)
        return (result[0] for result in results)

    @property
    def _researchers(self):
        results = self._db_manager.query(f"""
                    SELECT CONCAT(imie, ' ', nazwisko) FROM PracownicyNaukowi
                    """)
        return (result[0] for result in results)

    @property
    def _places(self):
        results = self._db_manager.query(f"""
                    SELECT CONCAT(sala, ', ', budynek) FROM Lokalizacja
                    """)
        return (result[0] for result in results)
