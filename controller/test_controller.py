from view import SearchDataView, DisplayDataView
from protocols import SearchDataViewDelegate
from PyQt5.Qt import QMainWindow, QWidget

class TestControllerMeta(type(QMainWindow), type(SearchDataViewDelegate)):
    pass


class TestController(QMainWindow, SearchDataViewDelegate, metaclass=TestControllerMeta):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        wid = QWidget(self)
        self.setCentralWidget(wid)
        test_view = DisplayDataView(wid)
        data = {
            "Temat": "Temat", "Autorzy": "Temat", "Promotor": "Temat", "Ocena promotora": "Temat",
            "Komentarz promotora": "Temat", "Recenzenci": "Temat", "Oceny recenzentów": "Temat",
            "Komentarze recenzentów": "Temat", "Słowa kluczowe": "Temat", "Kierunek studiów": "Temat",
            "Rodzaj studiów": "Temat", "Katedra": "Temat", "Wydział": "Temat", "Data obrony": "Temat",
            "Przewodniczący komisji": "Temat", "Ocena ostateczna": "Temat"
        }
        test_view.update_displayed_values(data)
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

