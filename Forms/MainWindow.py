from UI.mainwindow import *
import config
from Analyzer.RegexAnalyzer import RegexAnalyzer


class MainWindow(QtWidgets.QMainWindow, Ui_AnimePT_Refine):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        settings = config.getConfig()
        self.textField_srcDir.setText(settings.srcDir)
        self.textField_dstDir.setText(settings.dstDir)
        self.textField_subtitleDir.setText(settings.subtitleDir)
        self.buttonConnect()

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instace'):
            cls.instance = super(MainWindow, cls).__new__(cls)
        return cls.instance

    def buttonConnect(self) -> None:
        self.btn_srcDir.clicked.connect(lambda: self.onBtn_changeDirClicked(self.textField_srcDir))
        self.btn_dstDir.clicked.connect(lambda: self.onBtn_changeDirClicked(self.textField_dstDir))
        self.btn_subtitle.clicked.connect(lambda: self.onBtn_changeDirClicked(self.textField_subtitleDir))
        self.btn_anazlyze.clicked.connect(self.onBtn_analyzeClicked)
        self.btn_makeLink.clicked.connect(self.onBtn_makeLinkClicked)

    def closeEvent(self, event):
        config.saveConfig(config.Settings(self.textField_srcDir.text(), self.textField_dstDir.text(),
                                          self.textField_subtitleDir.text()))
        event.accept()

    @staticmethod
    def onBtn_changeDirClicked(textfield: QtWidgets.QLineEdit) -> None:
        textfield.setText(QtWidgets.QFileDialog.getExistingDirectory(None, "Choose Folder", textfield.text()))

    def onBtn_analyzeClicked(self) -> None:
        analyzer = RegexAnalyzer(self.textField_srcDir.text())
        self.textField_fansub.setText(analyzer.fansub)
        self.textField_title.setText(analyzer.title)
        self.textField_season.setText(analyzer.season)

    def onBtn_makeLinkClicked(self) -> None:
        pass
