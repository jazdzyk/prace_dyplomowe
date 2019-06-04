from view import BaseModifyView


class ModifyStudentView(BaseModifyView):
    def __init__(self, parent):
        BaseModifyView.__init__(self, parent)
