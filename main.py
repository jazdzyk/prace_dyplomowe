from controller.test_controller import TestController
from PyQt5.Qt import QApplication, QMainWindow, QWidget
from view import SearchDataView
import sys


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = TestController()

    sys.exit(app.exec_())
