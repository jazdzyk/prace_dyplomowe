from PyQt5.QtWidgets import QLineEdit, QListView, QComboBox

from protocols import AddModifyViewDelegate
from view import BaseAddModifyView


class AddThesisView(BaseAddModifyView):
    def __init__(self, parent, delegate: AddModifyViewDelegate = None, title_prefix="Dodawanie"):
        BaseAddModifyView.__init__(self, parent, title_prefix=title_prefix, title_suffix="Pracy dyplomowej")
        self._delegate = delegate
        self._set_up_general()
        self._set_up_ui()

    def _set_up_general(self):
        BaseAddModifyView._set_up_general(self)
        self._fields = [
            ("Temat", QLineEdit),
            ("Rodzaj studiów", QComboBox),
            ("Wydział", QComboBox),
            ("Kierunek studiów", QComboBox),
            ("Autorzy", QListView),
            ("Promotor", QComboBox),
            ("Recenzenci", QListView),
            ("Słowa kluczowe", QLineEdit)
        ]
        self._combo_box_items = [
            self._studies_type,
            self._faculties,
            self._courses,
            self._researchers
        ]
        self._list_view_items = [
            self._students,
            self._researchers
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
    def _studies_type(self):
        results = self._db_manager.query(f"""
                SELECT nazwaRodzaju FROM RodzajStudiow
                """)
        return (result[0] for result in results)

    @property
    def _faculties(self):
        results = self._db_manager.query(f"""
            SELECT nazwaWydzialu FROM Wydzial
            """)
        return (result[0] for result in results)

    @property
    def _courses(self):
        results = self._db_manager.query(f"""
            SELECT nazwaKierunku FROM KierunekStudiow
                LEFT JOIN Katedra K on KierunekStudiow.id_katedra = K.id_Katedra
            WHERE id_Wydzial = 2
            """)
        return (result[0] for result in results)

    @property
    def _researchers(self):
        results = self._db_manager.query(f"""
                SELECT CONCAT(imie, ' ', nazwisko) FROM PracownicyNaukowi
                """)
        return (result[0] for result in results)

    @property
    def _students(self):
        results = self._db_manager.query(f"""
                    SELECT CONCAT(imie, ' ', nazwisko) FROM Studenci
                    """)
        return (result[0] for result in results)

