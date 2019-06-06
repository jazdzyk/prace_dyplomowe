from view import AddThesisView
from protocols import AddModifyViewDelegate


class ModifyThesisView(AddThesisView):
    def __init__(self, parent, delegate: AddModifyViewDelegate = None):
        AddThesisView.__init__(self, parent, delegate=delegate)
