import sys, os
import Forms.MainWindow as MainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTranslator
if __name__ == '__main__':
    app = QApplication(sys.argv)
    translator = QTranslator()
    translator.load('./language/zh_CN.qm')
    app.installTranslator(translator)
    mainWindow = MainWindow.MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
