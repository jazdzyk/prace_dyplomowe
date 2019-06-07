from view import SearchDataView, DisplayDataView, ManageThesesView, GenerateReportView
from protocols import SearchDataViewDelegate, AddModifyViewDelegate, ManageThesesViewDelegate, \
    GenerateReportViewDelegate
from PyQt5.Qt import QMainWindow, QWidget


class MainControllerMeta(type(QMainWindow), type(SearchDataViewDelegate)):
    pass


class MainController(QMainWindow, SearchDataViewDelegate, AddModifyViewDelegate, ManageThesesViewDelegate, GenerateReportViewDelegate,
                     metaclass=MainControllerMeta):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        wid = QWidget(self)
        self.setCentralWidget(wid)
        test_view = GenerateReportView(wid, delegate=self)
        wid.setLayout(test_view)
        self.showMaximized()

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

    def view_did_press_add_button(self, view, data):
        print(f"view_did_press_add_button: {data}")

    def view_did_press_modify_button(self, view, data):
        print(f"view_did_press_modify_button: {data}")

    def view_did_choose_to_manage_undefended_theses(self, view):
        print(f"view_did_choose_to_manage_undefended_theses: ")

    def view_did_choose_to_manage_defended_theses(self, view):
        print(f"view_did_choose_to_manage_defended_theses: ")

    def view_did_select_displaying_data(self, view, data):
        print(f"view_did_select_displaying_data: {data}")

    def view_did_select_adding_review(self, view, data):
        print(f"view_did_select_adding_review: {data}")

    def view_did_select_theses_assigned_to_researcher(self, view):
        print(f"view_did_select_theses_assigned_to_researcher: ")

    def view_did_select_theses_between_dates(self, view):
        print(f"view_did_select_theses_between_dates: ")

    def view_did_select_theses_on_career(self, view):
        print(f"view_did_select_theses_on_career: ")

