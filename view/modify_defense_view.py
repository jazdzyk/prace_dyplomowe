from PyQt5.QtCore import QDate

from protocols import AddModifyViewDelegate
from view import AddDefenseView


class ModifyDefenseView(AddDefenseView):
    def __init__(self, parent, delegate: AddModifyViewDelegate = None):
        AddDefenseView.__init__(self, parent, delegate=delegate, title_prefix="Modyfikacja")
        self._set_up_initial_values(
            combo_box_values=self._combo_box_values(),
            date_edit_values=self._date_edit_values(),
            line_edit_values=self._line_edit_values()
        )

    def _line_edit_values(self):
        results = self._db_manager.query(f"""
        SELECT STRING_AGG(ocenaKoncowa, ', ') FROM AutorzyPracy
            LEFT JOIN PraceDyplomowe PD on AutorzyPracy.id_praca = PD.id_praca
        WHERE tytul = '{self._editable_fields["Praca dyplomowa"].currentText()}'
        """)
        return [value for value in results[0]]

    def _date_edit_values(self):
        date = self._db_manager.query(f"""
        SELECT data FROM Obrona
            LEFT JOIN PraceDyplomowe PD on Obrona.id_praca = PD.id_praca
        WHERE tytul = '{self._editable_fields["Praca dyplomowa"].currentText()}'
        """)[0][0]
        return [QDate(date.year, date.month, date.day)]

    def _combo_box_values(self):
        results = self._db_manager.query(f"""
        SELECT tytul, CONCAT(imie, ' ', nazwisko), CONCAT(sala, ', ', budynek) FROM PracownicyNaukowi
            LEFT JOIN KomisjaDyplomowa KD on PracownicyNaukowi.id_pracownikNaukowy = KD.id_przewodniczacy
            LEFT JOIN Obrona O on KD.id_komisja = O.id_komisja
            LEFT JOIN PraceDyplomowe PD on O.id_praca = PD.id_praca
            LEFT JOIN Lokalizacja L on O.id_lokalizacja = L.id_lokalizacja
        WHERE tytul = '{self._editable_fields["Praca dyplomowa"].currentText()}'
        """)
        return [value for value in results[0]]
