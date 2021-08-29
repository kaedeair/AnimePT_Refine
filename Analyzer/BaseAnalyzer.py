import abc, os


class BaseAnalyzer(metaclass=abc.ABCMeta):
    srcDir = ""
    fansub = ""
    fullName = ""
    title = ""
    season = ""
    subtitle_suffix = ["ass", "srt"]
    video_suffix = ["mp4", "mkv"]
    videoFileArr = []
    subtitleFileArr = []

    def __init__(self, srcDir: str):
        self.srcDir = srcDir
        self.addFile()
        self._analyze()

    def addFile(self):
        if len(self.srcDir) > 0:
            for item in os.listdir(self.srcDir):
                if os.path.splitext(item)[-1].replace(".", "") in BaseAnalyzer.video_suffix:
                    self.videoFileArr.append(item)
                elif os.path.splitext(item)[-1].replace(".", "") in BaseAnalyzer.subtitle_suffix:
                    self.subtitleFileArr.append(item)

    @abc.abstractmethod
    def _analyze(self):
        pass

    @staticmethod
    def _romanToInt(roman: str) -> int:
        result = 0
        romanDict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        for i in range(len(roman) - 1):
            if romanDict[roman[i]] < romanDict[roman[i + 1]]:
                result -= romanDict[roman[i]]
            else:
                result += romanDict[roman[i]]
        result += romanDict[roman[-1]]
        return result

    @staticmethod
    @abc.abstractmethod
    def _getFansub(fileName: str) -> str:
        pass

    @staticmethod
    @abc.abstractmethod
    def _getFullName(fileName: str) -> str:
        pass

    @staticmethod
    @abc.abstractmethod
    def _getTitle(fullName: str) -> str:
        pass

    @staticmethod
    @abc.abstractmethod
    def _getSeason(fullName: str) -> str:
        pass
