from PyQt5.QtWidgets import QComboBox

from protocols import AddModifyViewDelegate
from view import AddStudentView


class ModifyStudentView(AddStudentView):
    def __init__(self, parent, delegate: AddModifyViewDelegate = None):
        AddStudentView.__init__(self, parent, delegate=delegate, title_prefix="Modyfikacja")
        self._set_up_initial_values(
            line_edit_values=self._line_edit_values(),
            combo_box_values=["302927 - Kub Kub"]
        )

    def _set_up_general(self):
        AddStudentView._set_up_general(self)
        self._fields = [("ID Studenta", QComboBox)] + self._fields[:-1]
        self._combo_box_items = [self._students]

    @property
    def _students(self):
        results = self._db_manager.query(f"""
        SELECT CONCAT(id_student, ' - ', imie, ' ', nazwisko) FROM Studenci
        """)
        return (result[0] for result in results)


    def _line_edit_values(self):
        results = self._db_manager.query(f"""
        SELECT imie, nazwisko, telefon, email FROM Studenci
        WHERE id_student = '{self._editable_fields["ID Studenta"].currentText().split(" - ")[0]}'
        """)
        return [value for value in results[0]]
