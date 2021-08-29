from PyQt5.QtCore import QSettings

_settings = QSettings('config.ini', QSettings.IniFormat)


class Settings():
    srcDir = ""
    dstDir = ""
    subtitleDir = ""

    def __init__(self, srcDir="", dstDir="", subtitleDir=""):
        self.srcDir = srcDir
        self.dstDir = dstDir
        self.subtitleDir = subtitleDir


def getConfig() -> Settings:
    settings = Settings()
    settings.srcDir = _settings.value("Config/srcDir", "", str)
    settings.dstDir = _settings.value("Config/dstDir", "", str)
    settings.subtitleDir = _settings.value("Config/subtitleDir", "", str)
    return settings


def saveConfig(settings: Settings):
    for k, v in settings.__dict__.items():
        if (v != ''):
            _settings.setValue("Config/" + k, v)
