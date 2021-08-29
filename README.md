# AnimePT_Refine 
为了使Plex、Emby、Jeffylin等媒体服务器能够刮削到正确的元信息，同时不影响正常的PT保种，而产生的小工具 现处于Demo阶段

# 工作原理

使用正则表达式提取出文件名的信息，再通过硬链接(为了节省空间)的方法制作出一个符合命名规范的副本

# Notice

1.使用前先执行下发代码安装依赖

```angular2html
pip install -r requirements.txt
```

2.初次使用需要生成UI模块

```angular2html
python UpdateUI.py
```

3.安装中文翻译需要ts文件和QtLinguist工具

例如：

```angular2html
cd UI
pylupdate5  mainwindow.py -ts ../language/zh_CN.ts
```

使用QtLinguist发布功能得到qm文件，在main.py里更改文件路径即可生效

源文件夹和目标文件夹需要处于同一分区