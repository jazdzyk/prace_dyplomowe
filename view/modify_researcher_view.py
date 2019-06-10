from PyQt5.QtWidgets import QComboBox

from view import AddResearcherView
from protocols import AddModifyViewDelegate


class ModifyResearcherView(AddResearcherView):
    def __init__(self, parent, delegate: AddModifyViewDelegate = None):
        AddResearcherView.__init__(self, parent, delegate=delegate, title_prefix="Modyfikacja")
        self._set_up_initial_values(
            line_edit_values=self._line_edit_values(),
            combo_box_values=["2 - Pawel Kalinowski", "doktor",
                              "Elektrotechniki, Automatyki, Informatyki i Inzynierii Biomedycznej",
                              "Automatyki i Robotyki"]
        )

    def _set_up_general(self):
        AddResearcherView._set_up_general(self)
        self._fields = [("ID Pracownika naukowego", QComboBox)] + self._fields
        self._combo_box_items = [self._researchers] + self._combo_box_items

    @property
    def _researchers(self):
        results = self._db_manager.query(f"""
                    SELECT CONCAT(id_pracownikNaukowy, ' - ', imie, ' ', nazwisko) FROM PracownicyNaukowi
                    """)
        return (result[0] for result in results)

    def _line_edit_values(self):
        results = self._db_manager.query(f"""
        SELECT imie, nazwisko, telefon, email FROM PracownicyNaukowi
        WHERE id_pracownikNaukowy = '{self._editable_fields["ID Pracownika naukowego"].currentText().split(" - ")[0]}'
        """)
        return [value for value in results[0]]
