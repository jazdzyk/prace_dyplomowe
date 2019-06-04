from view import BaseView
from PyQt5.QtWidgets import QLabel, QComboBox, QLineEdit, QTextEdit, QPushButton, QHBoxLayout
from PyQt5.QtCore import Qt


class BaseAddModifyView(BaseView):
    def __init__(self, parent, title_prefix, title_suffix):
        BaseView.__init__(self, parent)
        self._title_prefix = title_prefix
        self._title_suffix = title_suffix
        self._set_up_general()

    def _set_up_general(self):
        self._title = f"{self._title_prefix} {self._title_suffix}"
        self._editable_fields = {}
        self._data = {}

    def _create_layout(self, fields, delegate_function):
        for title, qclass in fields:
            self.addLayout(self.__create_horizontal_layout(title, qclass))

        def on_button_clicked():
            delegate_function(self, self._data)

        button = QPushButton("Zapisz dane")
        button.clicked.connect(on_button_clicked)
        self.addWidget(button)
        self.addStretch(1)

    def __create_horizontal_layout(self, title, QClass):
        label = QLabel(title)
        label.setStyleSheet("""
        color: rgb(50, 50, 50);
        """)

        editable = QClass()
        self._editable_fields[title] = editable

        layout = QHBoxLayout()
        layout.addWidget(label, 1, Qt.AlignTop)
        layout.addWidget(editable, 4)

        return layout
