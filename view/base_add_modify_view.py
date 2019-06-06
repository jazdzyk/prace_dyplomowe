from view import BaseView
from PyQt5.QtWidgets import QLabel, QLineEdit, QTextEdit, QPushButton, QHBoxLayout, QDateEdit, QListView, QComboBox
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import Qt, QDate
from PyQt5.Qt import QAbstractItemView


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
        button_layout = QHBoxLayout()
        button_layout.addStretch(1)
        button_layout.addWidget(button)
        button_layout.addStretch(1)
        self.addLayout(button_layout)
        self.addStretch(1)

    def _on_line_edit_editing_finished(self, key, field):
        def _callback():
            self._data[key] = field.text()

        return _callback

    def _on_combo_box_current_text_changed(self, key):
        def _callback(text):
            self._data[key] = text

        return _callback

    def _on_date_edit_date_changed(self, key, field):
        def _callback():
            self._data[key] = self.__format_date_string(field.date())

        return _callback

    def _on_list_view_clicked(self, key, list_view_model):
        def _callback(index):
            text = list_view_model.itemFromIndex(index).text()
            if key in self._data:
                if text in self._data[key]:
                    self._data[key].remove(text)
                else:
                    self._data[key].append(text)
            else:
                self._data[key] = [text]

        return _callback

    def _on_text_edit_text_changed(self, key, field):
        def _callback():
            self._data[key] = field.toPlainText()

        return _callback

    def _add_callbacks(self, **kwargs):
        combo_box_items = kwargs.get("combo_box_items")
        combo_box_count = 0

        list_view_items = kwargs.get("list_view_items")
        list_view_count = 0

        for key, field in self._editable_fields.items():
            if isinstance(field, QLineEdit):
                field.editingFinished.connect(self._on_line_edit_editing_finished(key, field))
            elif isinstance(field, QComboBox):
                for index, text in enumerate(combo_box_items[combo_box_count]):
                    field.insertItem(index, text)
                field.currentTextChanged.connect(self._on_combo_box_current_text_changed(key))
                combo_box_count += 1
                self._data[key] = field.currentText()
            elif isinstance(field, QDateEdit):
                field.setDate(QDate.currentDate())
                self._data[key] = self.__format_date_string(QDate.currentDate())
                field.dateChanged.connect(self._on_date_edit_date_changed(key, field))
            elif isinstance(field, QTextEdit):
                field.textChanged.connect(self._on_text_edit_text_changed(key, field))
            elif isinstance(field, QListView):
                model = QStandardItemModel()
                field.setModel(model)
                field.setSelectionMode(QAbstractItemView.MultiSelection)
                for text in list_view_items[list_view_count]:
                    model.appendRow(QStandardItem(text))
                field.clicked.connect(self._on_list_view_clicked(key, model))
                list_view_count += 1
                self._data[key] = []

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

    @staticmethod
    def __format_date_string(date):
        return f"{date.day()}/{date.month()}/{date.year()}"
