from PyQt5.Qt import QMainWindow, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QVBoxLayout, QStackedLayout, QMessageBox

from manager import DatabaseManager
from model import Students, Researchers, Theses, Review, ThesesAuthors, Keywords, ThesesKeywords, Defense
from protocols import SearchDataViewDelegate, AddModifyViewDelegate, ManageThesesViewDelegate, \
    GenerateReportViewDelegate, OptionsMenuViewDelegate, DatabaseManagerDelegate
from view import AddDefenseView, OptionsMenuView, AddResearcherView, AddReviewView, AddStudentView, AddThesisView, \
    GenerateReportView, ManageThesesView, ModifyDefenseView, ModifyResearcherView, ModifyStudentView, ModifyThesisView, \
    SearchDataView, DisplayDataView


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
        elif self._search_type == SearchType.THESES:
            view.set_table_view(self._db_manager.query(f"""
            SELECT x.tytul,
                   STRING_AGG(x.autor, ', ') AS Autorzy,
                   x.promotor AS Promotor,
                   x.recenzenci AS Recenzenci
            FROM (
                SELECT DISTINCT PD.tytul,
                                CONCAT(S.imie, ' ', S.nazwisko) autor,
                                CONCAT(PN.imie, ' ', PN.nazwisko) promotor,
                                STRING_AGG(CONCAT(PNR.imie, ' ', PNR.nazwisko), ', ') recenzenci
                FROM AutorzyPracy AP
                     LEFT JOIN PraceDyplomowe PD on AP.id_praca = PD.id_praca
                     LEFT JOIN Studenci S on AP.id_student = S.id_student
                     LEFT JOIN PracownicyNaukowi PN on PD.id_promotor = PN.id_pracownikNaukowy
                     LEFT JOIN Recenzja R on AP.id_praca = R.id_praca
                     LEFT JOIN PracownicyNaukowi PNR on R.id_recenzujacy = PNR.id_pracownikNaukowy
                GROUP BY PD.tytul, CONCAT(S.imie, ' ', S.nazwisko), CONCAT(PN.imie, ' ', PN.nazwisko)
            ) x
            GROUP BY x.tytul, x.promotor, x.recenzenci
            HAVING CONCAT(x.tytul, ' ', STRING_AGG(x.autor, ', '), ' ', x.promotor, ' ', x.recenzenci) 
                LIKE '%{search_query_text}%'
            """))

    def view_did_choose_to_display_students(self, view):
        print(f"view_did_choose_to_display_students: ")
        self._search_type = SearchType.STUDENTS
        view.set_detailed_view_enabled(False)

    def view_did_choose_to_display_researchers(self, view):
        print(f"view_did_choose_to_display_researchers: ")
        self._search_type = SearchType.RESEARCHERS
        view.set_detailed_view_enabled(False)

    def view_did_choose_to_display_theses(self, view):
        print(f"view_did_choose_to_display_theses: ")
        self._search_type = SearchType.THESES
        view.set_detailed_view_enabled(True)

    def view_did_toggle_search_range_option(self, view, search_range_option):
        print(f"view_did_toggle_search_range_option: {search_range_option}")
        view.set_detailed_view_enabled(search_range_option == SearchDataView._SearchRangeOption.THESES)

    def view_wants_to_display_detailed_data(self, view, selected_row):
        print(f"view_wants_to_display_detailed_data: {selected_row}")
        detailed_display_view = DisplayDataView(self.centralWidget())
        self._set_up_action_view(detailed_display_view)
        data = {}
        data["Temat"] = selected_row[0]
        data["Autorzy"] = "\n".join(s.lstrip().rstrip() for s in selected_row[1].split(","))
        data["Promotor"] = selected_row[2]
        data["Recenzenci"] = "\n".join(s.lstrip().rstrip() for s in selected_row[3].split(","))
        data["Ocena promotora"] = str(self._db_manager.query(f"""
        SELECT ocenaPromotora FROM PraceDyplomowe PD
            LEFT JOIN PracownicyNaukowi PN on PD.id_promotor = PN.id_pracownikNaukowy
        WHERE PD.tytul = '{data["Temat"]}' AND CONCAT(PN.imie, ' ', PN.nazwisko) = '{data["Promotor"]}'
        """)[0][0])
        data["Oceny recenzentów"] = "\n".join(str(grade[0]) for grade in self._db_manager.query(f"""
                SELECT ocena FROM Recenzja
                LEFT JOIN PraceDyplomowe PD on Recenzja.id_praca = PD.id_praca
                LEFT JOIN PracownicyNaukowi PN on Recenzja.id_recenzujacy = PN.id_pracownikNaukowy
                WHERE PD.tytul = '{data["Temat"]}' 
                    AND CONCAT(PN.imie, ' ', PN.nazwisko) 
                        IN ({str(", ".join(f"'{s.lstrip().rstrip()}'" for s in selected_row[3].split(",")))})
                """))
        data["Komentarz promotora"] = self._db_manager.query(f"""
        SELECT komentarzPromotora FROM PraceDyplomowe PD
            LEFT JOIN PracownicyNaukowi PN on PD.id_promotor = PN.id_pracownikNaukowy
        WHERE PD.tytul = '{data["Temat"]}' AND CONCAT(PN.imie, ' ', PN.nazwisko) = '{data["Promotor"]}'
        """)[0][0]
        data["Komentarze recenzentów"] = "\n".join(str(grade[0]) for grade in self._db_manager.query(f"""
                SELECT tekstRecenzji FROM Recenzja
                LEFT JOIN PraceDyplomowe PD on Recenzja.id_praca = PD.id_praca
                LEFT JOIN PracownicyNaukowi PN on Recenzja.id_recenzujacy = PN.id_pracownikNaukowy
                WHERE PD.tytul = '{data["Temat"]}' 
                    AND CONCAT(PN.imie, ' ', PN.nazwisko) 
                        IN ({str(", ".join(f"'{s.lstrip().rstrip()}'" for s in selected_row[3].split(",")))})
                """))
        data["Słowa kluczowe"] = ", ".join(keyword[0] for keyword in self._db_manager.query(f"""
        SELECT SK.slowoKluczowe FROM SlowaKluczowePracy
            LEFT JOIN PraceDyplomowe PD on SlowaKluczowePracy.id_praca = PD.id_praca
            LEFT JOIN SlowaKluczowe SK on SlowaKluczowePracy.id_slowoKluczowe = SK.id_slowoKluczowe
        WHERE PD.tytul = '{data["Temat"]}'
        """))
        data["Kierunek studiów"] = self._db_manager.query(f"""
        SELECT nazwaKierunku FROM KierunekStudiow
            LEFT JOIN PraceDyplomowe PD on KierunekStudiow.id_kierunek = PD.id_kierunekStudiow
        WHERE PD.tytul = 'Implementacja algorytmu do generacji mikrostruktur 2D, 3D'
        """)[0][0]
        data["Rodzaj studiów"] = self._db_manager.query(f"""
        SELECT nazwaRodzaju FROM RodzajStudiow
            LEFT JOIN KierunekStudiow KS on RodzajStudiow.id_rodzajStudiow = KS.id_rodzajStudiow
            LEFT JOIN PraceDyplomowe PD on KS.id_kierunek = PD.id_kierunekStudiow
        WHERE PD.tytul = 'Implementacja algorytmu do generacji mikrostruktur 2D, 3D'
        """)[0][0]
        data["Katedra"] = self._db_manager.query(f"""
        SELECT nazwaKatedry FROM Katedra
            LEFT JOIN KierunekStudiow KS on Katedra.id_Katedra = KS.id_katedra
            LEFT JOIN PraceDyplomowe PD on KS.id_kierunek = PD.id_kierunekStudiow
        WHERE PD.tytul = 'Implementacja algorytmu do generacji mikrostruktur 2D, 3D'
        """)[0][0]
        data["Wydział"] = self._db_manager.query(f"""
        SELECT nazwaWydzialu FROM Wydzial
            LEFT JOIN Katedra K on Wydzial.id_Wydzial = K.id_Wydzial
            LEFT JOIN KierunekStudiow KS on K.id_Katedra = KS.id_katedra
            LEFT JOIN PraceDyplomowe PD on KS.id_kierunek = PD.id_kierunekStudiow
        WHERE PD.tytul = 'Implementacja algorytmu do generacji mikrostruktur 2D, 3D'
        """)[0][0]
        data["Data obrony"] = str(self._db_manager.query(f"""
        SELECT data FROM Obrona
            LEFT JOIN PraceDyplomowe PD on Obrona.id_praca = PD.id_praca
        WHERE PD.tytul = 'Implementacja algorytmu do generacji mikrostruktur 2D, 3D'
        """)[0][0]).split(" ")[0]
        data["Przewodniczący komisji"] = self._db_manager.query(f"""
        SELECT CONCAT(PN.imie, ' ', PN.nazwisko) FROM KomisjaDyplomowa
            LEFT JOIN PracownicyNaukowi PN on KomisjaDyplomowa.id_przewodniczacy = PN.id_pracownikNaukowy
            LEFT JOIN Obrona O on KomisjaDyplomowa.id_komisja = O.id_komisja
            LEFT JOIN PraceDyplomowe PD on O.id_praca = PD.id_praca
        WHERE PD.tytul = 'Implementacja algorytmu do generacji mikrostruktur 2D, 3D'
        """)[0][0]
        data["Ocena ostateczna"] = "\n".join(str(grade[0]) for grade in self._db_manager.query(f"""
        SELECT ocenaKoncowa FROM AutorzyPracy
            LEFT JOIN PraceDyplomowe PD on AutorzyPracy.id_praca = PD.id_praca
        WHERE PD.tytul = 'Implementacja algorytmu do generacji mikrostruktur 2D, 3D'
        """))
        for key in data:
            print(data[key])
        detailed_display_view.update_displayed_values(data)

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
    def view_did_select_theses_assigned_to_researcher(self, view, researcher):
        print(f"view_did_select_theses_assigned_to_researcher: {researcher}")
        view.set_table_view(self._db_manager.query(f"""
            SELECT x.tytul,
                   STRING_AGG(x.autor, ', ') AS Autorzy,
                   x.recenzent AS Recenzent
                   ,x.ocena,
                   x.tekstRecenzji
            FROM (
                SELECT DISTINCT PD.tytul,
                                CONCAT(S.imie, ' ', S.nazwisko) autor,
                                CONCAT(PNR.imie, ' ', PNR.nazwisko) recenzent,
                                R.ocena,
                                R.tekstRecenzji
                FROM AutorzyPracy AP
                     LEFT JOIN PraceDyplomowe PD on AP.id_praca = PD.id_praca
                     LEFT JOIN Studenci S on AP.id_student = S.id_student
                     LEFT JOIN PracownicyNaukowi PN on PD.id_promotor = PN.id_pracownikNaukowy
                     LEFT JOIN Recenzja R on AP.id_praca = R.id_praca
                     LEFT JOIN PracownicyNaukowi PNR on R.id_recenzujacy = PNR.id_pracownikNaukowy
            ) x
            GROUP BY x.tytul, x.recenzent, x.ocena, x.tekstRecenzji
            HAVING x.recenzent = '{researcher}'
            """))

    def view_did_select_theses_between_dates(self, view, date1, date2):
        print(f"view_did_select_theses_between_dates: {date1}, {date2}")
        view.set_table_view(self._db_manager.query(f"""
            SELECT x.tytul,
                   STRING_AGG(x.autor, ', ') AS Autorzy,
                   x.recenzent AS Recenzent
                   ,x.ocena,
                   x.tekstRecenzji
            FROM (
                SELECT DISTINCT PD.tytul,
                                CONCAT(S.imie, ' ', S.nazwisko) autor,
                                CONCAT(PNR.imie, ' ', PNR.nazwisko) recenzent,
                                R.ocena,
                                R.tekstRecenzji,
                                O.data
                FROM AutorzyPracy AP
                     LEFT JOIN PraceDyplomowe PD on AP.id_praca = PD.id_praca
                     LEFT JOIN Studenci S on AP.id_student = S.id_student
                     LEFT JOIN PracownicyNaukowi PN on PD.id_promotor = PN.id_pracownikNaukowy
                     LEFT JOIN Recenzja R on AP.id_praca = R.id_praca
                     LEFT JOIN PracownicyNaukowi PNR on R.id_recenzujacy = PNR.id_pracownikNaukowy
                     LEFT JOIN Obrona O on PD.id_praca = O.id_praca
            ) x
            GROUP BY x.tytul, x.recenzent, x.ocena, x.tekstRecenzji, x.data
            HAVING x.data >= '{date1}' AND x.data <= '{date2}'
            """))

    def view_did_select_theses_on_career(self, view, career):
        print(f"view_did_select_theses_on_career: {career}")
        view.set_table_view(self._db_manager.query(f"""
        SELECT x.tytul,
               STRING_AGG(x.autor, ', ') AS Autorzy,
               x.recenzent AS Recenzent
               ,x.ocena,
               x.tekstRecenzji
        FROM (
            SELECT DISTINCT PD.tytul,
                            CONCAT(S.imie, ' ', S.nazwisko) autor,
                            CONCAT(PNR.imie, ' ', PNR.nazwisko) recenzent,
                            R.ocena,
                            R.tekstRecenzji,
                            KS.nazwaKierunku
            FROM AutorzyPracy AP
                 LEFT JOIN PraceDyplomowe PD on AP.id_praca = PD.id_praca
                 LEFT JOIN Studenci S on AP.id_student = S.id_student
                 LEFT JOIN PracownicyNaukowi PN on PD.id_promotor = PN.id_pracownikNaukowy
                 LEFT JOIN Recenzja R on AP.id_praca = R.id_praca
                 LEFT JOIN PracownicyNaukowi PNR on R.id_recenzujacy = PNR.id_pracownikNaukowy
                 LEFT JOIN KierunekStudiow KS on PD.id_kierunekStudiow = KS.id_kierunek
        ) x
        GROUP BY x.tytul, x.recenzent, x.ocena, x.tekstRecenzji, x.nazwaKierunku
        HAVING x.nazwaKierunku = '{career}'
            """))

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
