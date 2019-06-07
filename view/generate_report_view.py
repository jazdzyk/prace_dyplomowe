from PyQt5.QtWidgets import QPushButton, QHBoxLayout

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
        pass

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
        self._add_widgets_to_layout((button1, button2), layout)
        layout.addStretch(1)

        return layout
