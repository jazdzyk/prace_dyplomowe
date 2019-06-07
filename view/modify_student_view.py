from PyQt5.QtWidgets import QComboBox

from view import AddStudentView
from protocols import AddModifyViewDelegate


class ModifyStudentView(AddStudentView):
    def __init__(self, parent, delegate: AddModifyViewDelegate = None):
        AddStudentView.__init__(self, parent, delegate=delegate, title_prefix="Modyfikacja")
        self._set_up_initial_values(
            line_edit_values=["Kub", "Kub", "100100100", "mao@mao.pl"],
            combo_box_values=["302927 - Kub Kub"]
        )

    def _set_up_general(self):
        AddStudentView._set_up_general(self)
        self._fields = [("ID Studenta", QComboBox)] + self._fields[:-1]
        self._combo_box_items = [("302926 - Jak Jaż", "302927 - Kub Kub", "302928 - Dao Dao")]
