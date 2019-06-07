from PyQt5.QtWidgets import QComboBox

from view import AddResearcherView
from protocols import AddModifyViewDelegate


class ModifyResearcherView(AddResearcherView):
    def __init__(self, parent, delegate: AddModifyViewDelegate = None):
        AddResearcherView.__init__(self, parent, delegate=delegate, title_prefix="Modyfikacja")
        self._set_up_initial_values(
            line_edit_values=["Mao", "Mao", "100100100", "mao@mao.pl"],
            combo_box_values=["2 - Mao Mao", "dr inż.", "IMiR", "druga"]
        )

    def _set_up_general(self):
        AddResearcherView._set_up_general(self)
        self._fields = [("ID Pracownika naukowego", QComboBox)] + self._fields
        self._combo_box_items = [("1 - Wao Wao", "2 - Mao Mao", "3 - Dao Dao")] + self._combo_box_items
