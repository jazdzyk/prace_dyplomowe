from PyQt5.QtWidgets import QLineEdit, QComboBox, QTextEdit

from protocols import AddModifyViewDelegate
from view import BaseAddModifyView


class AddReviewView(BaseAddModifyView):
    def __init__(self, parent, delegate: AddModifyViewDelegate = None, title_prefix="Dodawanie"):
        BaseAddModifyView.__init__(self, parent, title_prefix=title_prefix, title_suffix="Recenzji")
        self._delegate = delegate
        self._set_up_general()
        self._set_up_ui()

    def set_displayed_thesis(self, thesis_title):
        self._editable_fields["Praca dyplomowa"].setCurrentText(thesis_title)

    def _set_up_general(self):
        BaseAddModifyView._set_up_general(self)
        self._fields = [
            ("Praca dyplomowa", QComboBox),
            ("Ocena", QLineEdit),
            ("Komentarz", QTextEdit)
        ]
        self._combo_box_items = [
            self._theses
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
    def _theses(self):
        results = self._db_manager.query(f"""
                    SELECT tytul FROM PraceDyplomowe
                    """)
        return (result[0] for result in results)
