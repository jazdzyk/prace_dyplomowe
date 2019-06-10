from PyQt5.QtWidgets import QTableView, QPushButton, QHBoxLayout, QHeaderView, QAbstractItemView

from model.table.management_table_model import ManagementTableModel
from protocols import ManageThesesViewDelegate
from view import BaseView


class ManageThesesView(BaseView):
    def __init__(self, parent, delegate: ManageThesesViewDelegate = None):
        BaseView.__init__(self, parent)
        self._delegate = delegate
        self._set_up_general()
        self._set_up_ui()

    def set_table_view(self, data):
        def on_table_selected_row(selected, deselected):
            self._selected_row = [index.data() for index in selected.indexes()]

        model = ManagementTableModel(data)
        self._table_view.setModel(model)
        self._table_view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self._table_view.selectionModel().selectionChanged.connect(on_table_selected_row)
        self._table_view.setSelectionBehavior(QAbstractItemView.SelectRows)
        self._table_view.show()

    def _set_up_general(self):
        self._title = "Zarządzaj pracami dyplomowymi"
        self._selected_row = None

    def _set_up_ui(self):
        self._table_view = QTableView()

        self._layout.addLayout(self.__create_top_buttons())
        self._layout.addWidget(self._table_view)
        self._layout.addLayout(self.__create_bottom_buttons())
        self._layout.addStretch(1)

    def __create_top_buttons(self):
        def on_left_button_clicked():
            self._delegate.view_did_choose_to_manage_undefended_theses(self)

        def on_right_button_clicked():
            self._delegate.view_did_choose_to_manage_defended_theses(self)

        left_button = QPushButton("Prace nieobronione")
        left_button.clicked.connect(on_left_button_clicked)
        right_buton = QPushButton("Prace obronione")
        right_buton.clicked.connect(on_right_button_clicked)

        layout = QHBoxLayout()
        self._add_widgets_to_layout((left_button, right_buton), layout)
        layout.addStretch(1)

        return layout

    def __create_bottom_buttons(self):
        def on_left_button_clicked():
            self._delegate.view_did_select_displaying_data(self, self._selected_row)

        def on_right_button_clicked():
            self._delegate.view_did_select_adding_review(self, self._selected_row)

        left_button = QPushButton("Podgląd danych")
        left_button.clicked.connect(on_left_button_clicked)
        right_buton = QPushButton("Dodanie recenzji")
        right_buton.clicked.connect(on_right_button_clicked)

        layout = QHBoxLayout()
        layout.addStretch(1)
        self._add_widgets_to_layout((left_button, right_buton), layout)

        return layout
