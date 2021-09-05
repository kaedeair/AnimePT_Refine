from Analyzer.BaseAnalyzer import BaseAnalyzer

symbolDict = {
    '(': ')',
    '[': ']',
    '{': '}'
}


class SymbolAnalyzer(BaseAnalyzer):

    def _analyze(self):
        pass

    @staticmethod
    def splitBySymbol(fileName: str) -> list:
        stack = []
        result = []
        tmp = ""
        for string in fileName:
            if string in symbolDict.keys():
                stack.append(symbolDict[string])
                if len(stack) > 1:
                    tmp += string
                else:
                    if len(tmp) > 0:
                        result.append(tmp)
                        tmp = ""
            elif string in symbolDict.values():
                symbol = stack.pop()
                if symbol != string:
                    raise "symbol not match!"
                if len(stack) > 0:
                    tmp += string
                else:
                    result.append(SymbolAnalyzer.splitBySymbol(tmp))
                    tmp = ""
            else:
                tmp += string
        if len(tmp) > 0:
            result.append(tmp)
        if len(result) == 1:
            return result.pop()
        return result
