__all__ = [
    "BaseView",
    "SearchDataView",
    "DisplayDataView",
    "BaseAddModifyView",
    "ManageThesesView",
    "GenerateReportView",
    "AddDefenseView",
    "AddResearcherView",
    "AddThesisView",
    "AddReviewView",
    "AddStudentView",
    "ModifyDefenseView",
    "ModifyResearcherView",
    "ModifyStudentView",
    "ModifyThesisView",
    "OptionsMenuView",
]

from view.base_view import BaseView
from view.search_data_view import SearchDataView
from view.display_data_view import DisplayDataView
from view.base_add_modify_view import BaseAddModifyView
from view.manage_theses_view import ManageThesesView
from view.generate_report_view import GenerateReportView
from view.add_defense_view import AddDefenseView
from view.add_researcher_view import AddResearcherView
from view.add_thesis_view import AddThesisView
from view.add_review_view import AddReviewView
from view.add_student_view import AddStudentView
from view.modify_defense_view import ModifyDefenseView
from view.modify_researcher_view import ModifyResearcherView
from view.modify_student_view import ModifyStudentView
from view.modify_thesis_view import ModifyThesisView
from view.options_menu_view import OptionsMenuView
