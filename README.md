# AnimePT_Refine 
为了使Plex、Emby、Jeffylin等媒体服务器能够刮削到正确的元信息，同时不影响正常的PT保种，而产生的小工具
现处于Demo阶段
# 工作原理
使用正则表达式提取出文件名的信息，再通过硬链接(为了节省空间)的方法制作出一个符合命名规范的副本

# Notice
使用前先执行下发代码安装依赖
```angular2html
pip install -r requirements.txt
```

源文件夹和目标文件夹需要处于同一分区