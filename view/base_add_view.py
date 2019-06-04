from view import BaseAddModifyView


class BaseAddView(BaseAddModifyView):
    def __init__(self, parent, title_suffix):
        BaseAddModifyView.__init__(self, parent,
                                   title_prefix="Modyfikacja",
                                   title_suffix=title_suffix)
