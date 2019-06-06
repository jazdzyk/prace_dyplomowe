from view import AddStudentView
from protocols import AddModifyViewDelegate


class ModifyStudentView(AddStudentView):
    def __init__(self, parent, delegate: AddModifyViewDelegate = None):
        AddStudentView.__init__(self, parent, delegate=delegate)
