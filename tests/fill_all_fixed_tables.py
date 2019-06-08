import os

from model import StudiesType, Faculty, AcademicDepartment, UniversityCourse, DefenseLocalization

os.chdir("/home/kuba/PycharmProjects/prace_dyplomowe/")
from manager import DatabaseManager

if __name__ == '__main__':
    db_manager = DatabaseManager.instance()
    db_manager.add_many([
        Degree(nazwaStopniaNaukowego="doktor"),
        Degree(nazwaStopniaNaukowego="doktor inżynier"),
        Degree(nazwaStopniaNaukowego="doktor habilitowany"),
        Degree(nazwaStopniaNaukowego="doktor habilitowany inżynier"),
        Degree(nazwaStopniaNaukowego="profesor nadzwyczajny"),
        Degree(nazwaStopniaNaukowego="profesor")
    ])
    db_manager.add_many([
        StudiesType(nazwaRodzaju="inżynierskie"),
        StudiesType(nazwaRodzaju="licencjackie"),
        StudiesType(nazwaRodzaju="magisterskie"),
        StudiesType(nazwaRodzaju="podyplomowe")
    ])
    db_manager.add_many([
        Faculty(nazwaWydzialu="Elektrotechniki, Automatyki, Informatyki i Inżynierii Biomedycznej"),
        Faculty(nazwaWydzialu="Energetyki i Paliw"),
        Faculty(nazwaWydzialu="Fizyki i Informatyki Stosowanej"),
        Faculty(nazwaWydzialu="Geodezji Górniczej i Inżynierii Środowiska"),
        Faculty(nazwaWydzialu="Geologii, Geofizyki i Ochrony Środowiska"),
        Faculty(nazwaWydzialu="Górnictwa i Geoinżynierii"),
        Faculty(nazwaWydzialu="Humanistyczny"),
        Faculty(nazwaWydzialu="Informatyki, Elektroniki i Telekomunikacji"),
        Faculty(nazwaWydzialu="Inżynierii Materiałowej i Ceramiki"),
        Faculty(nazwaWydzialu="Inżynierii Metali i Informatyki Przemysłowej"),
        Faculty(nazwaWydzialu="Inżynierii Mechanicznej i Robotyki"),
        Faculty(nazwaWydzialu="Metali Nieżelaznych"),
        Faculty(nazwaWydzialu="Matematyki Stosowanej"),
        Faculty(nazwaWydzialu="Odlewnictwa"),
        Faculty(nazwaWydzialu="Wiertnictwa, Nafty i Gazu"),
        Faculty(nazwaWydzialu="Zarządzania")
    ])
    db_manager.add_many([
        AcademicDepartment(nazwaKatedry="Automatyki i Robotyki", id_Wydzial=2),
        AcademicDepartment(nazwaKatedry="Biocybernetyki i Inżynierii Biomedycznej", id_Wydzial=2),
        AcademicDepartment(nazwaKatedry="Elektrotechniki i Elektroenergetyki", id_Wydzial=2),
        AcademicDepartment(nazwaKatedry="Energoelektroniki i Automatyki Systemów Przetwarzania Energii", id_Wydzial=2),
        AcademicDepartment(nazwaKatedry="Informatyki Stosowanej", id_Wydzial=2),
        AcademicDepartment(nazwaKatedry="Metrologii i Elektroniki", id_Wydzial=2),
        AcademicDepartment(nazwaKatedry="Technologii Paliw", id_Wydzial=3),
        AcademicDepartment(nazwaKatedry="Chemii Węgla i Nauk o Środowisku", id_Wydzial=3),
        AcademicDepartment(nazwaKatedry="Zrównoważonego Rozwoju Energetycznego", id_Wydzial=3),
        AcademicDepartment(nazwaKatedry="Podstawowych Problemów Energetyki", id_Wydzial=3),
        AcademicDepartment(nazwaKatedry="Energetyki Wodorowej", id_Wydzial=3),
        AcademicDepartment(nazwaKatedry="Energetyki Jądrowej", id_Wydzial=3),
        AcademicDepartment(nazwaKatedry="Maszyn Cieplnych i Przepływowych", id_Wydzial=3),
        AcademicDepartment(nazwaKatedry="Fizyki Ciała Stałego", id_Wydzial=4),
        AcademicDepartment(nazwaKatedry="Fizyki Materii Skondensowanej", id_Wydzial=4),
        AcademicDepartment(nazwaKatedry="Fizyki Medycznej i Biofizyki", id_Wydzial=4),
        AcademicDepartment(nazwaKatedry="Informatyki Stosowanej i Fizyki Komputerowej", id_Wydzial=4),
        AcademicDepartment(nazwaKatedry="Oddziaływań i Detekcji Cząstek", id_Wydzial=4),
        AcademicDepartment(nazwaKatedry="Zastosowań Fizyki Jądrowej", id_Wydzial=4),
        AcademicDepartment(nazwaKatedry="Geomatyki", id_Wydzial=5),
        AcademicDepartment(nazwaKatedry="Ochrony Terenów Górniczych, Geoinformatyki i Geodezji Górniczej", id_Wydzial=5),
        AcademicDepartment(nazwaKatedry="Geoinformacji, Fotogrametrii i Teledetekcji Środowiska", id_Wydzial=5),
        AcademicDepartment(nazwaKatedry="Geodezji Inżynieryjnej i Budownictwa", id_Wydzial=5),
        AcademicDepartment(nazwaKatedry="Kształtowania i Ochrony Środowiska", id_Wydzial=5),
        AcademicDepartment(nazwaKatedry="Geodezji Zintegrowanej i Kartografii", id_Wydzial=5),
    ])
    db_manager.add_many([
        UniversityCourse(nazwaKierunku="automatyka i robotyka", id_rodzajStudiow=1, id_katedra=1),
        UniversityCourse(nazwaKierunku="komputerowe systemy sterowania", id_rodzajStudiow=3, id_katedra=1),
        UniversityCourse(nazwaKierunku="inteligentne systemy sterowania", id_rodzajStudiow=3, id_katedra=1),
        UniversityCourse(nazwaKierunku="informatyka w sterowaniu i zarządzaniu", id_rodzajStudiow=3, id_katedra=1),
        UniversityCourse(nazwaKierunku="cyber-physical systems", id_rodzajStudiow=3, id_katedra=1),
        UniversityCourse(nazwaKierunku="inżynieria biomedyczna", id_rodzajStudiow=1, id_katedra=2),
        UniversityCourse(nazwaKierunku="informatyka i elektronika medyczna", id_rodzajStudiow=3, id_katedra=2),
        UniversityCourse(nazwaKierunku="inżynieria biomateriałów", id_rodzajStudiow=3, id_katedra=2),
        UniversityCourse(nazwaKierunku="biomechanika i robotyka", id_rodzajStudiow=3, id_katedra=2),
        UniversityCourse(nazwaKierunku="bionanotechnologie", id_rodzajStudiow=3, id_katedra=2),
        UniversityCourse(nazwaKierunku="informatyka", id_rodzajStudiow=1, id_katedra=5),
        UniversityCourse(nazwaKierunku="inżynieria oprogramowania i systemów", id_rodzajStudiow=3, id_katedra=5),
        UniversityCourse(nazwaKierunku="grafika komputerowa", id_rodzajStudiow=3, id_katedra=5),
        UniversityCourse(nazwaKierunku="systems modelling and intelligent data analysis", id_rodzajStudiow=3, id_katedra=5),
        UniversityCourse(nazwaKierunku="inżynieria oprogramowania", id_rodzajStudiow=4, id_katedra=5),
        UniversityCourse(nazwaKierunku="nowoczesna grafika komputerowa", id_rodzajStudiow=4, id_katedra=5),
        UniversityCourse(nazwaKierunku="zarządzanie projektami informatycznymi", id_rodzajStudiow=4, id_katedra=5),
        UniversityCourse(nazwaKierunku="programowanie aplikacji webowych", id_rodzajStudiow=4, id_katedra=5),
        UniversityCourse(nazwaKierunku="elektrotechnika", id_rodzajStudiow=1, id_katedra=3),
        UniversityCourse(nazwaKierunku="automatyka przemysłowa i automatyka budynków", id_rodzajStudiow=3, id_katedra=4),
        UniversityCourse(nazwaKierunku="elektroenergetyka", id_rodzajStudiow=3, id_katedra=3),
        UniversityCourse(nazwaKierunku="energoelektronika i napęd elektryczny", id_rodzajStudiow=3, id_katedra=4),
        UniversityCourse(nazwaKierunku="pomiary technologiczne i biomedyczne", id_rodzajStudiow=3, id_katedra=6),
        UniversityCourse(nazwaKierunku="smart grids technology platforms", id_rodzajStudiow=3, id_katedra=4),
        UniversityCourse(nazwaKierunku="inżynieria elektryczna w pojazdach samochodowych", id_rodzajStudiow=3, id_katedra=4),
        UniversityCourse(nazwaKierunku="mikroelektronika w technice i medycynie", id_rodzajStudiow=1, id_katedra=6),
        UniversityCourse(nazwaKierunku="mikroelektronika w technice i medycynie", id_rodzajStudiow=3, id_katedra=6),
    ])
    db_manager.add_many([
        DefenseLocalization(sala="08", budynek="B1"),
        DefenseLocalization(sala="121", budynek="B1"),
        DefenseLocalization(sala="315", budynek="B1"),
        DefenseLocalization(sala="14", budynek="C3"),
        DefenseLocalization(sala="228", budynek="B8"),
        DefenseLocalization(sala="24", budynek="B2"),
        DefenseLocalization(sala="123", budynek="B2"),
        DefenseLocalization(sala="411", budynek="B6"),
        DefenseLocalization(sala="316", budynek="B6"),
        DefenseLocalization(sala="217", budynek="B7"),
        DefenseLocalization(sala="507", budynek="D1"),
        DefenseLocalization(sala="506", budynek="D1"),
        DefenseLocalization(sala="602", budynek="D8"),
        DefenseLocalization(sala="603", budynek="D8"),
        DefenseLocalization(sala="808", budynek="D8"),
        DefenseLocalization(sala="809", budynek="D8"),
        DefenseLocalization(sala="810", budynek="D8"),
        DefenseLocalization(sala="811", budynek="D8"),
        DefenseLocalization(sala="015", budynek="B4"),
        DefenseLocalization(sala="111", budynek="B4"),
        DefenseLocalization(sala="02", budynek="B3"),
    ])
