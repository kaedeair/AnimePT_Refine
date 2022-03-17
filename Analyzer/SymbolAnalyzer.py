from Analyzer.BaseAnalyzer import BaseAnalyzer

symbolDict = {
    '(': ')',
    '[': ']',
    '{': '}'
}


class SplitArgument:
    def __init__(self, fileName: str):
        self.fileName = fileName
        self.offset = 0
        self.stack = []

class SymbolAnalyzer(BaseAnalyzer):

    def _analyze(self):
        pass

    @staticmethod
    def splitBySymbol(fileName: str) -> list:
        args = SplitArgument(fileName)
        return SymbolAnalyzer.__split(args)

    @staticmethod
    def __split(args: SplitArgument) -> list:
        result = []
        tmp = ""
        while args.offset < len(args.fileName):
            string = args.fileName[args.offset]
            if string in symbolDict.keys():
                args.stack.append(symbolDict[string])
                if len(tmp) > 0:
                    result.append(tmp.strip())
                    tmp = ""
                args.offset += 1
                result.append(SymbolAnalyzer.__split(args))
            elif string in symbolDict.values():
                symbol = args.stack.pop()
                if symbol != string:
                    raise "symbol not match!"
                break
            else:
                tmp += string
            args.offset += 1
        if len(tmp) > 0:
            result.append(tmp.strip())
        return result

    def _getFansub(fileName: str) -> str:
        pass

    def _getFullName(fileName: str) -> str:
        pass

    def _getSeason(fullName: str) -> str:
        pass

    def _getTitle(fullName: str) -> str:
        pass
