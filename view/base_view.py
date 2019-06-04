from PyQt5.QtWidgets import QVBoxLayout, QLabel
from PyQt5.QtGui import QColor, QFont


class BaseView(QVBoxLayout):
    def __init__(self, parent=None):
        QVBoxLayout.__init__(self, parent)
        self._set_up_default_header_bar()

    @property
    def _title(self):
        return self.__header_label.text()

    @_title.setter
    def _title(self, value):
        self.__header_label.setText(value)

    @property
    def _header_background_color(self):
        return self.__header_background_color

    @_header_background_color.setter
    def _header_background_color(self, value):
        self.__header_background_color = value
        self.__update_header_bar_stylesheet(background_color=value)

    @property
    def _header_color(self):
        return self.__header_color

    @_header_color.setter
    def _header_color(self, value):
        self.__header_color = value
        self.__update_header_bar_stylesheet(color=value)

    def _set_up_general(self):
        raise NotImplementedError

    def _set_up_ui(self):
        raise NotImplementedError

    def _set_up_default_header_bar(self):
        self.__header_label = QLabel()
        self._title = "BaseView: default header's title"
        self.__header_color = QColor(255, 255, 255)
        self.__header_background_color = QColor(166, 148, 148)
        self.__update_header_bar_stylesheet()
        self.__update_header_bar_font(size=36)

        self.addWidget(self.__header_label)

    def _add_widgets(self, widgets):
        self._add_widgets_to_layout(widgets, self)

    def _add_layouts(self, layouts):
        self._add_layouts_to_layout(layouts, self)

    @staticmethod
    def _add_widgets_to_layout(widgets, layout):
        for widget in widgets:
            layout.addWidget(widget)

    @staticmethod
    def _add_layouts_to_layout(layouts, parent_layout):
        for layout in layouts:
            parent_layout.addLayout(layout)

    def __update_header_bar_stylesheet(self, **kwargs):
        color: QColor = kwargs.get("color", self._header_color)
        background_color: QColor = kwargs.get("background_color", self._header_background_color)
        self.__header_label.setStyleSheet(f"""
        color: rgb({color.red()}, {color.green()}, {color.blue()});
        background-color: rgb({background_color.red()}, {background_color.green()}, {background_color.blue()});
        """)

    def __update_header_bar_font(self, size, bold=False):
        font = QFont()
        font.setPointSize(size)
        font.setBold(bold)
        self.__header_label.setFont(font)
