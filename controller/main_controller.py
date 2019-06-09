from PyQt5.Qt import QMainWindow, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QVBoxLayout, QStackedLayout, QMessageBox

from manager import DatabaseManager
from model import Students, Researchers, Theses, Review, ThesesAuthors, Keywords, ThesesKeywords, Defense
from protocols import SearchDataViewDelegate, AddModifyViewDelegate, ManageThesesViewDelegate, \
    GenerateReportViewDelegate, OptionsMenuViewDelegate, DatabaseManagerDelegate
from view import AddDefenseView, OptionsMenuView, AddResearcherView, AddReviewView, AddStudentView, AddThesisView, \
    GenerateReportView, ManageThesesView, ModifyDefenseView, ModifyResearcherView, ModifyStudentView, ModifyThesisView, \
    SearchDataView


class MainControllerMeta(type(QMainWindow), type(SearchDataViewDelegate)):
    pass


Options = OptionsMenuView.Options
SearchType = SearchDataView.SearchType


class MainController(QMainWindow, SearchDataViewDelegate, AddModifyViewDelegate, ManageThesesViewDelegate,
                     GenerateReportViewDelegate, OptionsMenuViewDelegate, DatabaseManagerDelegate,
                     metaclass=MainControllerMeta):

    def __init__(self, user, parent=None):
        QMainWindow.__init__(self, parent)
        self._db_manager = DatabaseManager.instance()
        self._db_manager.set_delegate(self)
        self._user = user
        self._search_type = SearchType.STUDENTS
        self.setCentralWidget(QWidget(self))
        self._set_up_ui()
        self.showMaximized()

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
        if self._search_type == SearchType.STUDENTS:
            view.set_table_view(self._db_manager.query(f"""
            SELECT imie, nazwisko, telefon, email FROM Studenci
            WHERE CONCAT(imie, ' ', nazwisko) LIKE '%{search_query_text}%'
            """), column_count=4)
        elif self._search_type == SearchType.RESEARCHERS:
            view.set_table_view(self._db_manager.query(f"""
            SELECT PN.imie, PN.nazwisko, PN.telefon, PN.email, SN.nazwaStopniaNaukowego FROM PracownicyNaukowi PN
                INNER JOIN StopienNaukowy SN on PN.id_stopienNaukowy = SN.id_stopienNaukowy
            WHERE CONCAT(PN.imie, ' ', PN.nazwisko, ' ', SN.nazwaStopniaNaukowego) LIKE '%{search_query_text}%'
            """), column_count=5)

    def view_did_choose_to_display_students(self, view):
        print(f"view_did_choose_to_display_students: ")
        self._search_type = SearchType.STUDENTS

    def view_did_choose_to_display_researchers(self, view):
        print(f"view_did_choose_to_display_researchers: ")
        self._search_type = SearchType.RESEARCHERS

    def view_did_choose_to_display_theses(self, view):
        print(f"view_did_choose_to_display_theses: ")
        self._search_type = SearchType.THESES

    def view_did_toggle_search_range_option(self, view, search_range_option):
        print(f"view_did_toggle_search_range_option: {search_range_option}")

    def view_wants_to_display_detailed_data(self, view, selected_row):
        print(f"view_wants_to_display_detailed_data: {selected_row}")

    # AddModifyViewDelegate methods
    def view_did_press_add_button(self, view, data):
        print(f"view_did_press_add_button: {data}")
        if isinstance(view, AddStudentView):
            self._db_manager.add(Students(id_student=data["Numer indeksu"], imie=data["Imię"],
                                          nazwisko=data["Nazwisko"], telefon=data["Telefon"], email=data["Email"]))
        elif isinstance(view, AddResearcherView):
            id_stopien_naukowy = self._db_manager.query(f"""
            SELECT id_stopienNaukowy FROM StopienNaukowy
            WHERE nazwaStopniaNaukowego = '{data["Stopień naukowy"]}'
            """)[0][0]
            id_katedra = self._db_manager.query(f"""
            SELECT id_Katedra FROM Katedra
            WHERE nazwaKatedry = '{data["Katedra"]}'
            """)[0][0]
            self._db_manager.add(Researchers(imie=data["Imię"], nazwisko=data["Nazwisko"], telefon=data["Telefon"],
                                             email=data["Email"], id_stopienNaukowy=id_stopien_naukowy,
                                             id_katedra=id_katedra))
        elif isinstance(view, AddThesisView):
            id_promotor = self._db_manager.query(f"""
            SELECT id_pracownikNaukowy FROM PracownicyNaukowi
            WHERE CONCAT(imie, ' ', nazwisko) = '{data["Promotor"]}'
            """)[0][0]
            id_kierunek_studiow = self._db_manager.query(f"""
            SELECT id_kierunek FROM KierunekStudiow
            WHERE nazwaKierunku = '{data["Kierunek studiów"]}'
            """)[0][0]
            self._db_manager.add(Theses(tytul=data["Temat"], id_promotor=id_promotor,
                                        id_kierunekStudiow=id_kierunek_studiow))
            id_praca = self._db_manager.query(f"""
            SELECT id_praca FROM PraceDyplomowe
            WHERE tytul = '{data["Temat"]}' 
                AND id_kierunekStudiow = {id_kierunek_studiow} 
                AND id_promotor = {id_promotor}
            """)[0][0]
            for reviewer in data["Recenzenci"]:
                id_recenzujacy = self._db_manager.query(f"""
                SELECT id_pracownikNaukowy FROM PracownicyNaukowi
                WHERE CONCAT(imie, ' ', nazwisko) = '{reviewer}'
                """)[0][0]
                self._db_manager.add(Review(id_praca=id_praca, id_recenzujacy=id_recenzujacy))
            for author in data["Autorzy"]:
                id_author = self._db_manager.query(f"""
                SELECT id_student FROM Studenci
                WHERE CONCAT(imie, ' ', nazwisko) = '{author}'
                """)[0][0]
                self._db_manager.add(ThesesAuthors(id_student=id_author, id_praca=id_praca))
            for word in data["Słowa kluczowe"].split(","):
                word = word.lstrip().rstrip()
                id_slowo_kluczowe = self._db_manager.query(f"""
                SELECT id_slowoKluczowe FROM SlowaKluczowe
                WHERE slowoKluczowe = '{word}'
                """)
                if not id_slowo_kluczowe:
                    self._db_manager.add(Keywords(slowoKluczowe=word))
                    id_slowo_kluczowe = self._db_manager.query(f"""
                    SELECT id_slowoKluczowe FROM SlowaKluczowe
                    WHERE slowoKluczowe = '{word}'
                    """)

                self._db_manager.add(ThesesKeywords(id_slowoKluczowe=id_slowo_kluczowe[0][0], id_praca=id_praca))
        elif isinstance(view, AddDefenseView):
            id_praca = self._db_manager.query(f"""
            SELECT id_praca FROM PraceDyplomowe
            WHERE tytul = '{data["Praca dyplomowa"]}'
            """)[0][0]
            id_komisja = self._db_manager.query(f"""
            SELECT KD.id_komisja FROM KomisjaDyplomowa KD
                INNER JOIN PracownicyNaukowi PN on KD.id_przewodniczacy = PN.id_pracownikNaukowy
            WHERE CONCAT(PN.imie, ' ', PN.nazwisko) = '{data["Przewodniczący komisji"]}'
            """)[0][0]
            id_lokalizacja = self._db_manager.query(f"""
            SELECT id_lokalizacja FROM Lokalizacja
            WHERE CONCAT(budynek, ', ', sala) = '{data["Miejsce obrony"]}'
            """)
            self._db_manager.add(Defense(data=data["Data obrony"], id_praca=id_praca, id_komisja=id_komisja,
                                         id_lokalizacja=id_lokalizacja))

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

    # DatabaseManagerDelegate methods
    def manager_reports_error(self, error):
        print(f"manager_reports_error: {error}")
        message_box = QMessageBox()
        message_box.setIcon(QMessageBox.Critical)
        message_box.setWindowTitle("Error!")
        message_box.setText(error.statement)
        message_box.setStandardButtons(QMessageBox.Ok)
