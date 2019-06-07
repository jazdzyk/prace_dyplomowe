import math

from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QPushButton, QHBoxLayout, QTableView, QLabel, QComboBox, QDateEdit

from protocols import GenerateReportViewDelegate
from view import BaseView


class GenerateReportView(BaseView):
    def __init__(self, parent, delegate: GenerateReportViewDelegate = None):
        BaseView.__init__(self, parent)
        self._delegate = delegate
        self._set_up_general()
        self._set_up_ui()

    def _set_up_general(self):
        self._title = "Generuj raport"

    def _set_up_ui(self):
        top_layout, researcher_combo_box = self.__create_horizontal_layout("Pracownik naukowy", [QComboBox])
        self._researcher_combo_box = researcher_combo_box[0]
        self.addLayout(top_layout)

        mid_layout, dates_edits = self.__create_horizontal_layout("Data obrony", [QDateEdit, QDateEdit])
        self._start_date, self._end_date = dates_edits
        self.addLayout(mid_layout)

        bottom_layout, career_combo_box = self.__create_horizontal_layout("Kierunek", [QComboBox])
        self._career_combo_box = career_combo_box[0]
        self.addLayout(bottom_layout)

        self._start_date.setDate(QDate.currentDate())
        self._end_date.setDate(QDate.currentDate())

        self.addLayout(self.__create_top_buttons())
        table_view = QTableView()
        self.addWidget(table_view)
        self.addStretch(1)

    def __create_top_buttons(self):
        def on_button1_clicked():
            self._delegate.view_did_select_theses_assigned_to_researcher(self)

        def on_button2_clicked():
            self._delegate.view_did_select_theses_between_dates(self)

        def on_button3_clicked():
            self._delegate.view_did_select_theses_on_career(self)

        button1 = QPushButton("Prace przypisane do pracownika naukowego")
        button1.clicked.connect(on_button1_clicked)
        button2 = QPushButton("Prace obronione w okresie między datami")
        button2.clicked.connect(on_button2_clicked)
        button3 = QPushButton("Prace obronione na kierunku studiów")
        button3.clicked.connect(on_button3_clicked)

        layout = QHBoxLayout()
        self._add_widgets_to_layout((button1, button2, button3), layout)
        layout.addStretch(1)

        return layout

    def __create_horizontal_layout(self, title, q_classes):
        label = QLabel(title)
        label.setStyleSheet("""
        color: rgb(50, 50, 50);
        """)

        editables = []
        for QClass in q_classes:
            editables.append(QClass())

        layout = QHBoxLayout()
        layout.addWidget(label, 1)
        for editable in editables:
            layout.addWidget(editable, int(math.ceil(4 / len(editables))))

        return layout, editables
