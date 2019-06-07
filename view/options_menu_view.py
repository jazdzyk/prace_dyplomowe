from enum import Enum

from PyQt5.QtWidgets import QVBoxLayout, QButtonGroup, QPushButton

from protocols import OptionsMenuViewDelegate


class OptionsMenuView(QVBoxLayout):
    class Options(Enum):
        ADD_DEFENSE_VIEW = (0, "Dodaj obronę")
        ADD_RESEARCHER_VIEW = (1, "Dodaj pracownika naukowego")
        ADD_REVIEW_VIEW = (2, "Dodaj recenzję")
        ADD_STUDENT_VIEW = (3, "Dodaj studenta")
        ADD_THESIS_VIEW = (4, "Dodaj pracę dyplomową")
        MODIFY_DEFENSE_VIEW = (5, "Modyfikuj obronę")
        MODIFY_RESEARCHER_VIEW = (6, "Modyfikuj pracownika naukowego")
        MODIFY_STUDENT_VIEW = (7, "Modyfikuj studenta")
        MODIFY_THESIS_VIEW = (8, "Modyfikuj pracę dyplomową")
        SEARCH_DATA = (9, "Wyszukaj dane")
        GENERATE_REPORT = (10, "Generuj raport")
        MANAGE_THESES = (11, "Zarządzaj pracami")

        @property
        def id(self):
            return self._value_[0]

        @property
        def name(self):
            return self._value_[1]

    def __init__(self, options: Options, parent=None, delegate: OptionsMenuViewDelegate = None):
        QVBoxLayout.__init__(self, parent)
        self._delegate = delegate
        self._set_up_ui(options)

    def _set_up_ui(self, options: [Options]):
        button_group = QButtonGroup()
        for option in options:
            button = QPushButton(option.name)
            button_group.addButton(button, option.id)
            self.addWidget(button)

        def on_button_clicked(id):
            self._delegate.view_did_select_option(self, OptionsMenuView.Options((id, button_group.button(id).text())))
        self.addStretch(1)
        button_group.buttonClicked[int].connect(on_button_clicked)
