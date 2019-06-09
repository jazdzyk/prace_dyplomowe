import typing

from PyQt5.QtCore import QAbstractTableModel, QModelIndex, Qt


class PeopleTableModel(QAbstractTableModel):
    def __init__(self, data, column_count, parent=None):
        QAbstractTableModel.__init__(self, parent=parent)
        self._column_count = column_count
        self._names, self._surnames, self._phone_numbers, self._emails, self._degrees = self.__prepare_data(data)

    def rowCount(self, parent: QModelIndex = ...) -> int:
        return len(self._names)

    def columnCount(self, parent: QModelIndex = ...) -> int:
        return self._column_count

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = ...) -> typing.Any:
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return [
                "Imię",
                "Nazwisko",
                "Telefon",
                "Email",
                "Stopień naukowy"
            ][section]

    def data(self, index: QModelIndex, role: int = ...) -> typing.Any:
        if role == Qt.TextAlignmentRole:
            return Qt.AlignLeft | Qt.AlignVCenter
        elif role == Qt.DisplayRole:
            return [
                self._names[index.row()],
                self._surnames[index.row()],
                self._phone_numbers[index.row()],
                self._emails[index.row()],
                self._degrees.get(index.row())
            ][index.column()]

    def __prepare_data(self, data):
        names, surnames, phone_numbers, emails, degrees = {}, {}, {}, {}, {}
        for index, row in enumerate(data):
            names[index] = row[0]
            surnames[index] = row[1]
            phone_numbers[index] = row[2]
            emails[index] = row[3]
            if self._column_count == 5:
                degrees[index] = row[4]
        return names, surnames, phone_numbers, emails, degrees
