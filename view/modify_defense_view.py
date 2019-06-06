from view import AddDefenseView
from protocols import AddModifyViewDelegate


class ModifyDefenseView(AddDefenseView):
    def __init__(self, parent, delegate: AddModifyViewDelegate = None):
        AddDefenseView.__init__(self, parent, delegate=delegate)
