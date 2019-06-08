from PyQt5.Qt import QMainWindow, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QVBoxLayout, QStackedLayout

from manager import DatabaseManager
from protocols import SearchDataViewDelegate, AddModifyViewDelegate, ManageThesesViewDelegate, \
    GenerateReportViewDelegate, OptionsMenuViewDelegate
from view import AddDefenseView, OptionsMenuView, AddResearcherView, AddReviewView, AddStudentView, AddThesisView, \
    GenerateReportView, ManageThesesView, ModifyDefenseView, ModifyResearcherView, ModifyStudentView, ModifyThesisView, \
    SearchDataView


class MainControllerMeta(type(QMainWindow), type(SearchDataViewDelegate)):
    pass


Options = OptionsMenuView.Options


class MainController(QMainWindow, SearchDataViewDelegate, AddModifyViewDelegate, ManageThesesViewDelegate,
                     GenerateReportViewDelegate, OptionsMenuViewDelegate,
                     metaclass=MainControllerMeta):

    def __init__(self, user, parent=None):
        QMainWindow.__init__(self, parent)
        self._user = user
        self.setCentralWidget(QWidget(self))
        self._set_up_ui()
        self.showMaximized()
        self._db_manager = DatabaseManager.instance()

    def _set_up_ui(self):
        self._main_layout = QVBoxLayout()
        self.centralWidget().setLayout(self._main_layout)
        self._set_up_top_label()
        self._horizontal_layout = QHBoxLayout()
        self._main_layout.addLayout(self._horizontal_layout)
        self._set_up_menu_view()
        self._set_up_stacked_view()

    def _set_up_stacked_view(self):
        self._action_stacked_layout = QStackedLayout()
        horizontal_layout = QHBoxLayout()
        horizontal_layout.addLayout(self._action_stacked_layout, 4)
        self._action_stacked_layout.addWidget(QLabel())
        self._action_stacked_layout.setCurrentIndex(0)
        horizontal_layout.addStretch(1)
        self._horizontal_layout.addLayout(horizontal_layout, 7)

    def _set_up_top_label(self):
        top_label = QLabel(f"Zalogowany jako {self._user}")
        top_label.setStyleSheet(f"""
        color: rgb(255, 255, 255);
        background-color: rgb(166, 148, 148);
        """)
        font = QFont()
        font.setPointSize(20)
        font.setBold(False)
        top_label.setFont(font)
        self._main_layout.addWidget(top_label)

    def _set_up_menu_view(self):
        horizontal_layout = QHBoxLayout()
        horizontal_layout.addStretch(1)
        horizontal_layout.addLayout(OptionsMenuView(options=(
            Options.ADD_STUDENT_VIEW,
            Options.MODIFY_STUDENT_VIEW,
            Options.ADD_RESEARCHER_VIEW,
            Options.MODIFY_RESEARCHER_VIEW,
            Options.ADD_THESIS_VIEW,
            Options.MODIFY_THESIS_VIEW,
            Options.ADD_DEFENSE_VIEW,
            Options.MODIFY_DEFENSE_VIEW,
            Options.SEARCH_DATA,
            Options.GENERATE_REPORT
        ), delegate=self))
        self._horizontal_layout.addLayout(horizontal_layout, 1)

    def _set_up_action_view(self, view):
        self._action_stacked_layout.takeAt(0)
        self._action_stacked_layout.addWidget(view)
        self._action_stacked_layout.setCurrentIndex(0)

    # SearchDataViewDelegate methods
    def view_did_press_search_button(self, view, search_query_text):
        print(f"view_did_press_search_button: {search_query_text}")

    def view_did_choose_to_display_students(self, view):
        print(f"view_did_choose_to_display_students: ")

    def view_did_choose_to_display_researchers(self, view):
        print(f"view_did_choose_to_display_researchers: ")

    def view_did_toggle_search_range_option(self, view, search_range_option):
        print(f"view_did_toggle_search_range_option: {search_range_option}")

    def view_did_choose_to_display_theses(self, view):
        print(f"view_did_choose_to_display_theses: ")

    # AddModifyViewDelegate methods
    def view_did_press_add_button(self, view, data):
        print(f"view_did_press_add_button: {data}")

    def view_did_press_modify_button(self, view, data):
        print(f"view_did_press_modify_button: {data}")

    # ManageThesesViewDelegate methods
    def view_did_choose_to_manage_undefended_theses(self, view):
        print(f"view_did_choose_to_manage_undefended_theses: ")

    def view_did_choose_to_manage_defended_theses(self, view):
        print(f"view_did_choose_to_manage_defended_theses: ")

    def view_did_select_displaying_data(self, view, data):
        print(f"view_did_select_displaying_data: {data}")

    def view_did_select_adding_review(self, view, data):
        print(f"view_did_select_adding_review: {data}")

    # GenerateReportViewDelegate methods
    def view_did_select_theses_assigned_to_researcher(self, view):
        print(f"view_did_select_theses_assigned_to_researcher: ")

    def view_did_select_theses_between_dates(self, view):
        print(f"view_did_select_theses_between_dates: ")

    def view_did_select_theses_on_career(self, view):
        print(f"view_did_select_theses_on_career: ")

    # OptionsMenuViewDelegate methods
    def view_did_select_option(self, view, option):
        print(f"view_did_select_option: {option}")
        self._set_up_action_view(view={
            Options.ADD_DEFENSE_VIEW: AddDefenseView,
            Options.ADD_RESEARCHER_VIEW: AddResearcherView,
            Options.ADD_REVIEW_VIEW: AddReviewView,
            Options.ADD_STUDENT_VIEW: AddStudentView,
            Options.ADD_THESIS_VIEW: AddThesisView,
            Options.GENERATE_REPORT: GenerateReportView,
            Options.MANAGE_THESES: ManageThesesView,
            Options.MODIFY_DEFENSE_VIEW: ModifyDefenseView,
            Options.MODIFY_RESEARCHER_VIEW: ModifyResearcherView,
            Options.MODIFY_STUDENT_VIEW: ModifyStudentView,
            Options.MODIFY_THESIS_VIEW: ModifyThesisView,
            Options.SEARCH_DATA: SearchDataView,
        }.get(option)(self.centralWidget(), delegate=self))
