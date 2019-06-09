import typing

from PyQt5.QtCore import QAbstractTableModel, QModelIndex, Qt


class ThesesTableModel(QAbstractTableModel):
    def __init__(self, data, parent=None):
        QAbstractTableModel.__init__(self, parent=parent)
        self._titles, self._authors, self._promotors, self._reviewers = self.__prepare_data(data)

    def rowCount(self, parent: QModelIndex = ...) -> int:
        return len(self._titles)

    def columnCount(self, parent: QModelIndex = ...) -> int:
        return 4

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = ...) -> typing.Any:
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return [
                "Temat",
                "Autorzy",
                "Promotor",
                "Recenzenci",
            ][section]

    def data(self, index: QModelIndex, role: int = ...) -> typing.Any:
        if role == Qt.TextAlignmentRole:
            return Qt.AlignLeft | Qt.AlignVCenter
        elif role == Qt.DisplayRole:
            return [
                self._titles[index.row()],
                self._authors[index.row()],
                self._promotors[index.row()],
                self._reviewers[index.row()]
            ][index.column()]

    def __prepare_data(self, data):
        titles, authors, promotors, reviewers = {}, {}, {}, {}
        for index, row in enumerate(data):
            titles[index] = row[0]
            authors[index] = row[1]
            promotors[index] = row[2]
            reviewers[index] = row[3]
        return titles, authors, promotors, reviewers
