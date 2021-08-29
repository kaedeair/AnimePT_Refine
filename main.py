import sys, os
import Forms.MainWindow as MainWindow
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow.MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
