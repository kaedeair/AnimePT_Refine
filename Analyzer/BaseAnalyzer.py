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
    subtitleDir = ""

    def __init__(self, srcDir: str):
        self.srcDir = srcDir
        self.addFile()
        self._analyze()

    def addFile(self):
        if len(self.srcDir) > 0:
            rootDir = []
            for item in os.listdir(self.srcDir):
                filePath = os.path.join(self.srcDir, item)
                if os.path.isdir(filePath):
                    rootDir.append(filePath)
                elif os.path.splitext(filePath)[-1].replace(".", "") in BaseAnalyzer.video_suffix:
                    self.videoFileArr.append(item)
                elif os.path.splitext(filePath)[-1].replace(".", "") in BaseAnalyzer.subtitle_suffix:
                    self.subtitleFileArr.append(item)
            if len(self.subtitleFileArr) == 0:
                self._searchSubtitleDir(rootDir)
            else:
                self.subtitleDir = self.srcDir
            self.__getOneTypeSubtitleFiles()

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

    def _searchSubtitleDir(self, rootDir: str) -> str:
        for folder in rootDir:
            folderPath = os.path.join(rootDir, folder)
            for item in os.listdir(folderPath):
                filePath = os.path.join(rootDir, folder, item)
                if os.path.isdir(filePath):
                    result = BaseAnalyzer._searchSubtitleDir(filePath)
                    if result != "":
                        return result
                elif os.path.splitext(filePath)[-1].replace(".", "") in BaseAnalyzer.subtitle_suffix:
                    self.subtitleFileArr.append(filePath)
            if len(self.subtitleFileArr) > 0:
                return folderPath
        return ""

    def __getOneTypeSubtitleFiles(self) -> None:
        subTitleFiles = []
        lang = []
        arrLen = len(self.subtitleFileArr)
        for i in range(0, arrLen if arrLen < 3 else 3):
            try:
                langTag = self.subTitleFiles[i].split('.')[-2]
                if langTag == 'zh':
                    lang.insert(1, langTag)
                    break
                elif langTag == 'sc':
                    lang.insert(0, langTag)
                    break
                elif langTag == 'tc':
                    lang.insert(2, langTag)
                    break
                elif langTag == 'chs':
                    lang.insert(0, langTag)
                    break
                elif langTag == 'cht':
                    lang.insert(2, langTag)
                    break
                assert lang.count() != 0
            except:
                print("不能识别字幕文件!")
                return
        for subTitleFile in self.subTitleFiles:
            if subTitleFile.split('.')[-2] == lang[0]:
                subTitleFiles.append(subTitleFile)
        self.subtitleFileArr = subTitleFiles
