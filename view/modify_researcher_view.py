from view import AddResearcherView
from protocols import AddModifyViewDelegate


class ModifyResearcherView(AddResearcherView):
    def __init__(self, parent, delegate: AddModifyViewDelegate = None):
        AddResearcherView.__init__(self, parent, delegate=delegate)
