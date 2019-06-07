from enum import Enum

from PyQt5.QtWidgets import QGroupBox, QRadioButton, QLineEdit, QPushButton, QTableView, QVBoxLayout, QHBoxLayout

from protocols import SearchDataViewDelegate
from view import BaseView


class SearchDataView(BaseView):
    class __SearchRangeOption(Enum):
        PEOPLE = 0
        THESES = 1

    def __init__(self, parent=None, delegate: SearchDataViewDelegate = None):
        BaseView.__init__(self, parent)
        self._delegate = delegate
        self._set_up_general()
        self._set_up_ui()

    def _set_up_general(self):
        self._title = " Wyszukaj..."
        self._range_option = SearchDataView.__SearchRangeOption.PEOPLE
        self._search_query_text = ""

    def _set_up_ui(self):
        self.__set_up_range_box()
        self.__set_up_search_keyword_box()
        self.__set_up_results_box()

    def _set_range_option(self, value):
        self._range_option = value
        self._delegate.view_did_toggle_search_range_option(self, value)
        self.__update_results_box()

    def __set_up_range_box(self):
        def on_left_radio_button_clicked():
            self._set_range_option(SearchDataView.__SearchRangeOption.PEOPLE)

        def on_right_radio_button_clicked():
            self._set_range_option(SearchDataView.__SearchRangeOption.THESES)

        left_radio_button = QRadioButton("Osoby")
        left_radio_button.setChecked(True)
        left_radio_button.clicked.connect(on_left_radio_button_clicked)
        right_radio_button = QRadioButton("Prace dyplomowe")
        right_radio_button.clicked.connect(on_right_radio_button_clicked)

        layout = QHBoxLayout()
        self._add_widgets_to_layout((left_radio_button, right_radio_button), layout)
        layout.addStretch(1)

        group_box = QGroupBox("Zakres")
        group_box.setLayout(layout)
        self.addWidget(group_box)

    def __set_up_search_keyword_box(self):
        line_edit = QLineEdit()

        def on_line_edit_editing_finished():
            self._search_query_text = line_edit.text()

        def on_button_clicked():
            self._delegate.view_did_press_search_button(self, line_edit.text())

        def on_line_edit_return_pressed():
            on_button_clicked()

        line_edit.setPlaceholderText("Tutaj wpisz hasło, które chcesz wyszukać...")
        line_edit.editingFinished.connect(on_line_edit_editing_finished)
        line_edit.returnPressed.connect(on_line_edit_return_pressed)

        button = QPushButton("Wyszukaj")
        button.clicked.connect(on_button_clicked)
        layout = QHBoxLayout()
        layout.addWidget(line_edit, 7)
        layout.addWidget(button, 1)

        group_box = QGroupBox("Hasło wyszukiwania")
        group_box.setLayout(layout)
        self.addWidget(group_box)

    def __set_up_results_box(self):
        table_view = QTableView()

        layout = QVBoxLayout()
        layout.addLayout(self.__create_results_buttons())
        layout.addWidget(table_view)

        group_box = QGroupBox("Wyniki wyszukiwania")
        group_box.setLayout(layout)
        self.addWidget(group_box)

    def __create_results_buttons(self):
        def on_left_button_clicked():
            self._delegate.view_did_choose_to_display_students(self)

        def on_mid_button_clicked():
            self._delegate.view_did_choose_to_display_researchers(self)

        def on_right_button_clicked():
            self._delegate.view_did_choose_to_display_theses(self)

        self._results_left_button = QPushButton("Studenci")
        self._results_left_button.clicked.connect(on_left_button_clicked)
        self._results_mid_button = QPushButton("Pracownicy naukowi")
        self._results_mid_button.clicked.connect(on_mid_button_clicked)
        self._results_right_buton = QPushButton("Prace dyplomowe")
        self._results_right_buton.clicked.connect(on_right_button_clicked)
        self._results_right_buton.setEnabled(False)

        layout = QHBoxLayout()
        self._add_widgets_to_layout((self._results_left_button, self._results_mid_button, self._results_right_buton),
                                    layout)
        layout.addStretch(1)

        return layout

    def __update_results_box(self):
        self._results_left_button.setEnabled(self._range_option == SearchDataView.__SearchRangeOption.PEOPLE)
        self._results_mid_button.setEnabled(self._range_option == SearchDataView.__SearchRangeOption.PEOPLE)
        self._results_right_buton.setEnabled(self._range_option == SearchDataView.__SearchRangeOption.THESES)