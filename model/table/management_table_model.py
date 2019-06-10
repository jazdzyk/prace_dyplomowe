import typing

from PyQt5.QtCore import QAbstractTableModel, QModelIndex, Qt


class ManagementTableModel(QAbstractTableModel):
    def __init__(self, data, parent=None):
        QAbstractTableModel.__init__(self, parent=parent)
        self._titles, self._authors, self._promotors, self._grades, self._comments, self._final_grades = self.__prepare_data(data)

    def rowCount(self, parent: QModelIndex = ...) -> int:
        return len(self._titles)

    def columnCount(self, parent: QModelIndex = ...) -> int:
        return 6

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = ...) -> typing.Any:
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return [
                "Temat",
                "Autorzy",
                "Promotor",
                "Ocena",
                "Komentarz",
                "Ocena końcowa"
            ][section]

    def data(self, index: QModelIndex, role: int = ...) -> typing.Any:
        if role == Qt.TextAlignmentRole:
            return Qt.AlignLeft | Qt.AlignVCenter
        elif role == Qt.DisplayRole:
            return [
                self._titles[index.row()],
                self._authors[index.row()],
                self._promotors[index.row()],
                self._grades[index.row()],
                self._comments[index.row()],
                self._final_grades[index.row()]
            ][index.column()]

    def __prepare_data(self, data):
        titles, authors, promotors, grades, comments, final_grades = {}, {}, {}, {}, {}, {}
        for index, row in enumerate(data):
            titles[index] = row[0]
            authors[index] = row[1]
            promotors[index] = row[2]
            grades[index] = str(row[3])
            comments[index] = row[4]
            final_grades[index] = str(row[5])
        return titles, authors, promotors, grades, comments, final_grades
