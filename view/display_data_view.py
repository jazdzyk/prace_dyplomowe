from PyQt5.QtWidgets import QHBoxLayout, QLabel, QLineEdit, QTextEdit
from PyQt5.QtCore import Qt
from view import BaseView


class DisplayDataView(BaseView):
    def __init__(self, parent=None):
        BaseView.__init__(self, parent)
        self._set_up_general()
        self._set_up_ui()

    def update_displayed_values(self, data):
        for key, text in data.items():
            self._line_edits[key].setText(text)

    def _set_up_general(self):
        self._title = "Podgląd danych"
        self._line_edits = {}

    def _set_up_ui(self):
        data = (
            ("Temat", True), ("Autorzy", True), ("Promotor", True), ("Ocena promotora", True),
            ("Komentarz promotora", False), ("Recenzenci", True), ("Oceny recenzentów", True),
            ("Komentarze recenzentów", False), ("Słowa kluczowe", False), ("Kierunek studiów", True),
            ("Rodzaj studiów", True), ("Katedra", True), ("Wydział", True), ("Data obrony", True),
            ("Przewodniczący komisji", True), ("Ocena ostateczna", True)
        )

        for _data in data:
            title, line = _data
            self.addLayout(self.__create_horizontal_layout(title, line))
        self.addStretch(1)

    def __create_horizontal_layout(self, title, line):
        label = QLabel(title)
        label.setStyleSheet("""
        color: rgb(50, 50, 50);
        """)

        line_edit = QLineEdit() if line else QTextEdit()
        line_edit.setEnabled(False)
        line_edit.setStyleSheet("""
        :disabled {
            color: rgb(0, 0, 0);
        }
        """)
        self._line_edits[title] = line_edit

        layout = QHBoxLayout()
        layout.addWidget(label, 1, Qt.AlignTop)
        layout.addWidget(line_edit, 4)

        return layout
