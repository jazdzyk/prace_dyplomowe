from view import BaseAddModifyView


class BaseModifyView(BaseAddModifyView):
    def __init__(self, parent, title_suffix):
        BaseAddModifyView.__init__(self, parent,
                                   title_prefix="Modyfikacja",
                                   title_suffix=title_suffix)
