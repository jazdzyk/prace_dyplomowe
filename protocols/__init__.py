__all__ = [
    "SearchDataViewDelegate",
    "AddModifyViewDelegate",
    "ManageThesesViewDelegate",
    "GenerateReportViewDelegate",
    "OptionsMenuViewDelegate"
]

from protocols.search_data_view_delegate import SearchDataViewDelegate
from protocols.add_modify_view_delegate import AddModifyViewDelegate
from protocols.manage_theses_view_delegate import ManageThesesViewDelegate
from protocols.generate_report_view_delegate import GenerateReportViewDelegate
from protocols.options_menu_view_delegate import OptionsMenuViewDelegate
from protocols.database_manager_delegate import DatabaseManagerDelegate
