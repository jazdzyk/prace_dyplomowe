from view import BaseAddView


class AddStudentView(BaseAddView):
    def __init__(self, parent):
        BaseAddView.__init__(self, parent)
