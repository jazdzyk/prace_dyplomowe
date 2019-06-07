import sys

from PyQt5.Qt import QApplication

from controller.main_controller import MainController

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainController(user="Pracownik dziekanatu")
    sys.exit(app.exec_())
