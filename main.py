import sys,os
import PySimpleGUI as sg
import regex as re
global video_suffix,subtitle_suffix,roma2Int

srcDir=""
dstDir=""
subtitle_suffix = ["ass", "srt"]
video_suffix = ["mp4", "mkv"]
roma2Int={
    "II":2,
    "III":3,
    "IV":4,
    "V":5,
    "VI":6
}

if len(sys.argv) > 1:
    src=os.path.dirname(sys.argv[1])

if len(sys.argv) > 2:
    dstDir=os.path.dirname(sys.argv[2])

class mainwindow:
    videoFiles = []
    subTitleFiles = []
    subOrg = ""
    fullName = ""
    title = ""
    season = ""
    fullName = ""
    def __init__(self,srcDir,dstDir):
        self.layout = [[sg.Text('　源目录：'), sg.InputText(srcDir, key='srcDir'),
                   sg.FolderBrowse('选择', key='chSrcDir', initial_folder=sys.path[0], enable_events=True, target='srcDir',
                                   change_submits=True)],
                    [sg.Text('目标目录：'), sg.InputText(dstDir, key='dstDir'),
                        sg.FolderBrowse('选择', key='chDstDir', initial_folder=sys.path[0], enable_events=True,
                                        target='dstDir',
                                        change_submits=True)],
                  [sg.Text('　字幕组：'), sg.InputText(key='subOrg')],
                  [sg.Text('　　标题：'), sg.InputText(key='title')],
                  [sg.Text('　　　季：'), sg.InputText(key='season')],
                  [sg.Button('解析', enable_events=True), sg.Button('生成硬链接', enable_events=True)]]

    def reset(self):
        self.subOrg = ""
        self.fullName = ""
        self.title = ""
        self.season = ""
        self.fullName = ""
        self.videoFiles.clear()
        self.subTitleFiles.clear()

    def makeLink(self,srcDir,dstDir):
        dstDir=os.path.join(dstDir, self.fullName)
        if self.videoFiles.__len__()>0:
            os.makedirs(dstDir)
        if len(self.videoFiles) != len(self.subTitleFiles):
            self.subTitleFiles=self.getOneLangSubtitleFiles()
        for file in self.videoFiles:
            episode=self.getEpisode(file)
            if episode=="":
                print('获取集数失败')
                return
            suffix=os.path.splitext(file)[-1]
            os.link(os.path.join(srcDir,file),os.path.join(dstDir,self.title+" S"+str(self.season).zfill(2)+"E"+episode.zfill(2)+suffix))
        for file in self.subTitleFiles:
            episode=self.getEpisode(file)
            if episode=="":
                print('获取集数失败')
                return
            lang=file.split(".")[-2]
            suffix=os.path.splitext(file)[-1]
            os.link(os.path.join(srcDir,file),os.path.join(dstDir,self.title+" S"+str(self.season).zfill(2)+"E"+episode.zfill(2)+"."+lang+suffix))

    def analyze(self,path: str)->None:
        if len(path)>0:
            for item in os.listdir(path):
                if os.path.splitext(item)[-1].replace(".","") in video_suffix:
                    self.videoFiles.append(item)
                elif os.path.splitext(item)[-1].replace(".","") in subtitle_suffix:
                    self.subTitleFiles.append(item)

            if self.videoFiles.__len__()>0:
                self.subOrg =self.getSubOrg(self.videoFiles[0])
                self.fullName=self.getFullName(self.videoFiles[0])
                self.title=self.getTitle(self.fullName)
                self.season=self.getSeason(self.fullName)
                self.window['subOrg'].update(self.subOrg)
                self.window['title'].update(self.title)
                self.window['season'].update(self.season)

    def getOneLangSubtitleFiles(self):
        subTitleFiles = []
        lang = []
        for i in range(0, 3):
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
        return subTitleFiles

    def getEpisode(self,fileName):
        regex = r'(?<=[\s\[\]\(\)])\d{2,3}(?=[\s\[\]\)\(])'
        episode = re.search(regex, fileName)
        if episode is not None:
            return episode.group().strip()
        return ""

    def getSubOrg(self,fileName:str)->str:
        regex='(?<=^\[).+?(?=\])'
        subOrg=re.search(regex,fileName)
        if subOrg is not None:
            return subOrg.group().strip()
        return ""

    def getFullName(self,fileName):
        regex=r'(?<=\]|\))(?<!\s+)[^\[\]\.\(\)()]+?(?=\[|\(|(\d))'
        fullName=re.search(regex,fileName)
        if fullName is not None:
            return fullName.group().strip()
        return ""

    def getTitle(self,fullName:str)->str:
        regex=r'(II|III|IV|V|VI)\s?$'
        title=re.sub(regex,"",fullName)
        if title is not None:
            return title.strip()
        return ""

    def getSeason(self,fullName:str)->str:
        if fullName.replace(" ","").__len__()>0:
            regex=r'(II|III|IV|V|VI)\s?$'
            season=re.search(regex,fullName)
            if season is not None:
                season=season.group()
                if season in roma2Int:
                    return roma2Int[season].__str__()
            return "1"
        return ""


    def start(self)->None:
        self.window = sg.Window('PT_Refine', self.layout)
        while True:
            event, values = self.window.read()
            if event == '解析':
                self.reset()
                self.analyze(values['srcDir'])
            elif event == '生成硬链接':
                self.makeLink(values['srcDir'],values['dstDir'])
                print('生成完毕')
            elif event == sg.WIN_CLOSED:
                exit(0)

if __name__=='__main__':
    window=mainwindow(srcDir,dstDir)
    window.start()








