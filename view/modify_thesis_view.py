from PyQt5.QtWidgets import QComboBox

from view import AddThesisView
from protocols import AddModifyViewDelegate


class ModifyThesisView(AddThesisView):
    def __init__(self, parent, delegate: AddModifyViewDelegate = None):
        AddThesisView.__init__(self, parent, delegate=delegate, title_prefix="Modyfikacja")
        self._set_up_initial_values(
            line_edit_values=self._line_edit_values(),
            combo_box_values=self._combo_box_values(),
            list_view_values=self._list_view_values()
        )

    def _set_up_general(self):
        AddThesisView._set_up_general(self)
        self._fields = [("Praca Dyplomowa", QComboBox)] + self._fields
        self._combo_box_items = [self._theses] + self._combo_box_items

    @property
    def _theses(self):
        results = self._db_manager.query(f"""
                SELECT tytul FROM PraceDyplomowe
                """)
        return (result[0] for result in results)

    def _line_edit_values(self):
        results = self._db_manager.query(f"""
        SELECT tytul, STRING_AGG(slowoKluczowe, ', ') FROM PraceDyplomowe
            LEFT JOIN SlowaKluczowePracy SKP on PraceDyplomowe.id_praca = SKP.id_praca
            LEFT JOIN SlowaKluczowe SK on SKP.id_slowoKluczowe = SK.id_slowoKluczowe
        GROUP BY tytul
        HAVING tytul = '{self._editable_fields["Praca Dyplomowa"].currentText().split(" - ")[0]}'
        """)
        return [value for value in results[0]]

    def _combo_box_values(self):
        results = self._db_manager.query(f"""
                SELECT nazwaRodzaju, nazwaWydzialu, nazwaKierunku, CONCAT(imie, ' ', nazwisko) 
                FROM RodzajStudiow
                    LEFT JOIN KierunekStudiow KS on RodzajStudiow.id_rodzajStudiow = KS.id_rodzajStudiow
                    LEFT JOIN PraceDyplomowe PD on KS.id_kierunek = PD.id_kierunekStudiow
                    LEFT JOIN PracownicyNaukowi PN on PD.id_promotor = PN.id_pracownikNaukowy
                    LEFT JOIN Katedra K on KS.id_katedra = K.id_Katedra
                    LEFT JOIN Wydzial W on K.id_Wydzial = W.id_Wydzial
                WHERE tytul = '{self._editable_fields["Praca Dyplomowa"].currentText()}'
                """)
        return [self._editable_fields["Praca Dyplomowa"].currentText()] + [value for value in results[0]]

    def _list_view_values(self):
        authors = [author[0] for author in self._db_manager.query(f"""
                SELECT CONCAT(imie, ' ', nazwisko) FROM Studenci
                LEFT JOIN AutorzyPracy AP on Studenci.id_student = AP.id_student
                LEFT JOIN PraceDyplomowe PD on AP.id_praca = PD.id_praca
                WHERE PD.tytul = '{self._editable_fields["Praca Dyplomowa"].currentText()}'
                """)]
        reviewers = [reviewer[0] for reviewer in self._db_manager.query(f"""
                SELECT CONCAT(imie, ' ', nazwisko) FROM PracownicyNaukowi
                    LEFT JOIN Recenzja R on PracownicyNaukowi.id_pracownikNaukowy = R.id_recenzujacy
                    LEFT JOIN PraceDyplomowe PD on PracownicyNaukowi.id_pracownikNaukowy = R.id_recenzujacy
                WHERE PD.tytul = '{self._editable_fields["Praca Dyplomowa"].currentText()}'
                """)]
        return [authors, reviewers]
