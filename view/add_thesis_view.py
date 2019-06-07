from PyQt5.QtWidgets import QLineEdit, QListView, QComboBox

from protocols import AddModifyViewDelegate
from view import BaseAddModifyView


class AddThesisView(BaseAddModifyView):
    def __init__(self, parent, delegate: AddModifyViewDelegate = None, title_prefix="Dodawanie"):
        BaseAddModifyView.__init__(self, parent, title_prefix=title_prefix, title_suffix="Pracy dyplomowej")
        self._delegate = delegate
        self._set_up_general()
        self._set_up_ui()

    def _set_up_general(self):
        BaseAddModifyView._set_up_general(self)
        self._fields = [
            ("Temat", QLineEdit),
            ("Rodzaj studiów", QComboBox),
            ("Wydział", QComboBox),
            ("Kierunek studiów", QComboBox),
            ("Autorzy", QListView),
            ("Promotor", QComboBox),
            ("Recenzenci", QListView),
            ("Słowa kluczowe", QLineEdit)
        ]
        self._combo_box_items = [
            ("licencjackie", "inżynierskie", "magisterskie", "doktoranckie"),
            ("EAIIB", "IMiR", "IET"),
            ("pierwszy", "drugi", "trzeci"),
            ("Józek Józek", "Władziu Władziu", "Zdzisław Zdzisław", "Stasiu Stasiu")
        ]
        self._list_view_items = [
            ("Adam Małysz", "Robert Mateja", "Simon Amann", "Łukasz Kruczek", "Jan Kowalski", "Zdzisław Kowalski",
             "Jan Kowal", "Zygmunt Staszczyk", "Adam Małysz", "Robert Mateja", "Simon Amann", "Łukasz Kruczek",
             "Jan Kowalski", "Adam Małysz", "Robert Mateja", "Simon Amann", "Łukasz Kruczek", "Jan Kowalski"),
            ("Jan Kowalski", "Zdzisław Kowalski", "Adam Małysz", "Robert Mateja", "Simon Amann", "Łukasz Kruczek",
             "Jan Kowal", "Zygmunt Staszczyk")
        ]

    def _set_up_ui(self):
        if self._title_prefix == "Dodawanie":
            delegate_function = self._delegate.view_did_press_add_button
        else:
            delegate_function = self._delegate.view_did_press_modify_button
        self._create_layout(fields=self._fields,
                            delegate_function=delegate_function)
        self._add_callbacks()
