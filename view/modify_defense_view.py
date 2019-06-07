from PyQt5.QtCore import QDate

from protocols import AddModifyViewDelegate
from view import AddDefenseView


class ModifyDefenseView(AddDefenseView):
    def __init__(self, parent, delegate: AddModifyViewDelegate = None):
        AddDefenseView.__init__(self, parent, delegate=delegate, title_prefix="Modyfikacja")
        self._set_up_initial_values(
            combo_box_values=["druga", "trzeci", "trzecia"],
            date_edit_values=[QDate(2019, 3, 1)],
            line_edit_values=["5.0"]
        )
