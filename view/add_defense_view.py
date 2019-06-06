from PyQt5.QtWidgets import QLineEdit, QComboBox, QDateEdit

from protocols import AddModifyViewDelegate
from view import BaseAddModifyView


class AddDefenseView(BaseAddModifyView):
    def __init__(self, parent, delegate: AddModifyViewDelegate = None):
        BaseAddModifyView.__init__(self, parent, title_prefix="Dodawanie", title_suffix="Obronę")
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

    def _set_up_ui(self):
        self._create_layout(fields=self._fields,
                            delegate_function=self._delegate.view_did_press_add_button)
        self._add_callbacks(combo_box_items=[
            ("pierwsza", "druga", "trzecia"),
            ("pierwszy", "drugi", "trzeci"),
            ("pierwsza", "druga", "trzecia")
        ])
