from PyQt5.QtWidgets import QComboBox

from view import AddThesisView
from protocols import AddModifyViewDelegate


class ModifyThesisView(AddThesisView):
    def __init__(self, parent, delegate: AddModifyViewDelegate = None):
        AddThesisView.__init__(self, parent, delegate=delegate, title_prefix="Modyfikacja")
        self._set_up_initial_values(
            line_edit_values=["pierwsza", "uno dos, tres, cuatro cinco, seis"],
            combo_box_values=["druga", "inżynierskie", "IET", "trzeci", "Władziu Władziu"],
            list_view_values=[("Robert Mateja", "Łukasz Kruczek"), ("Adam Małysz", "Simon Amann")]
        )

    def _set_up_general(self):
        AddThesisView._set_up_general(self)
        self._fields = [("Praca Dyplomowa", QComboBox)] + self._fields
        self._combo_box_items = [("pierwsza", "druga", "trzecia")] + self._combo_box_items
