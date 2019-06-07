from view import SearchDataView, DisplayDataView, ManageThesesView
from protocols import SearchDataViewDelegate, AddModifyViewDelegate, ManageThesesViewDelegate
from PyQt5.Qt import QMainWindow, QWidget


class TestControllerMeta(type(QMainWindow), type(SearchDataViewDelegate)):
    pass


class TestController(QMainWindow, SearchDataViewDelegate, AddModifyViewDelegate, ManageThesesViewDelegate,
                     metaclass=TestControllerMeta):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        wid = QWidget(self)
        self.setCentralWidget(wid)
        test_view = ManageThesesView(wid, delegate=self)
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
