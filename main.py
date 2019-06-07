import sys

from PyQt5.Qt import QApplication

from controller.test_controller import TestController

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = TestController()
    sys.exit(app.exec_())
