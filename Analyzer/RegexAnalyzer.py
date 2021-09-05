from Analyzer.BaseAnalyzer import BaseAnalyzer
import regex as re


class RegexAnalyzer(BaseAnalyzer):
    __fansubRegex: re.Regex = r'(?<=^\[).+?(?=\])'
    __fullNameRegex: re.Regex = r'(?<=\]|\))(?<!\s+)[^\[\]\.\(\)()]+?(?=\[|\(|(\d))'
    __romanRegex: re.Regex = r'(IX|IV|V?I{1,3})'
    __episodeRegex: re.Regex = r'(?<=[\s\[\]\(\)])\d{2,3}(?=[\s\[\]\)\(])'

    def _analyze(self):
        if (self.videoFileArr.__len__() > 0):
            fileName = self.videoFileArr[0]
            self.fansub = RegexAnalyzer._getFansub(fileName)
            self.fullName = RegexAnalyzer._getFullName(fileName)
            self.title = RegexAnalyzer._getTitle(self.fullName)
            self.season = RegexAnalyzer._getSeason(self.fullName)

    @staticmethod
    def _getTitle(fullName: str) -> str:
        title = re.sub(RegexAnalyzer.__romanRegex, "", fullName)
        return title.strip()

    @staticmethod
    def _getSeason(fullName: str) -> str:
        if fullName.replace(" ", "").__len__() > 0:
            season = re.search(RegexAnalyzer.__romanRegex, fullName)
            if season is not None:
                season = RegexAnalyzer._romanToInt(season.group())
                if (season == 0):
                    return ""
                else:
                    return season.__str__()
            return "1"
        return ""

    @staticmethod
    def _getFansub(fileName: str) -> str:
        subOrg = re.search(RegexAnalyzer.__fansubRegex, fileName)
        if subOrg is not None:
            return subOrg.group().strip()
        return ""

    @staticmethod
    def _getFullName(fileName: str) -> str:
        fullName = re.search(RegexAnalyzer.__fullNameRegex, fileName)
        if fullName is not None:
            return fullName.group().strip()
        return ""
