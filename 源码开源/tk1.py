from tkinter import *
import tkinter.font as tf
from PIL import Image, ImageTk



def point():
    #创建子窗口
    top=Toplevel()
    top.title("操作指南")
    frame_tk=Frame(top)
    Label(frame_tk,text="上：W",width=32,bg="white").pack()
    Label(frame_tk,text="下：S",width=32,bg="white").pack()
    Label(frame_tk,text="左：A",width=32,bg="white").pack()
    Label(frame_tk,text="右：D",width=32,bg="white").pack()
    Label(frame_tk,text="全屏：F11",width=32,bg="white").pack()
    Label(frame_tk,text="暂停：Enter",width=32,bg="white").pack()
    Label(frame_tk,text="全屏导弹：Space",width=32,bg="white").pack()
    frame_tk.pack(fill=X)
def introduce():
    top=Toplevel()
    top.title("游戏介绍")
    text=Text(top,height=38,width=55)
    ft = tf.Font(family='微软雅黑',size=12)
    ft2= tf.Font(family='宋体',size=10)
    text.tag_config('tag',font =ft,foreground = '#336699') #设置tag即插入文字的大小,颜色等
    text.tag_config('tag_1',font = ft2)
    text.insert(END,"                                 游戏介绍\n\n","tag")
    text.insert(END,"游戏的基本设定\n","tag1")
    text.insert(END,"1.敌方共有大中小3款飞机，分为高中低三种速度\n\n","tag1")
    text.insert(END,"2.消灭小飞机需要1发子弹,中飞机需要8发，大飞机需要20发子弹\n\n","tag1")
    text.insert(END,"3.每消灭一架小飞机得1000分，中飞机6000分,大飞机10000分\n\n","tag1")
    text.insert(END,"4.每个20秒有一个随机的道具补给，分为两种道具，全屏炸弹和双倍子弹\n\n","tag1")
    text.insert(END,"5.全屏炸弹最多只能存放3枚，双倍子弹可以维持18秒钟的效果\n\n","tag1")
    text.insert(END,"6.游戏将根据分数来逐步提高难度，难度的提高表现为飞机数量的增多以及速度的加快\n\n","tag1")
    text.insert(END,"7.我方有三次机会，每次被敌人消灭，新诞生的飞机会有3秒钟的安全期\n\n","tag1")
    text.insert(END,"8.游戏结束后会显示历史最高分数\n\n","tag1")
    text.insert(END,"9.总共有八关，挑战分数为100w ，希望有人达成(划掉)\n（有人玩就是最大的鼓励了 嘤嘤嘤）\n\n\n\n\n\n","tag1")
    text.pack(padx=30,pady=30)
    text.insert(END,"                     人生如逆旅，我亦是行人","tag")




#插入更新记录
def Insert(title_str,str):
    ft = tf.Font(family='微软雅黑',size=12)
    ft2= tf.Font(family='宋体',size=10)
    text.tag_config('tag',font =ft,foreground = '#336699') #设置tag即插入文字的大小,颜色等
    text.tag_config('tag_1',font = ft2)

    text.insert(END,title_str+"\n",'tag')
    text.insert(END,str+"\n\n\n",'tag_1')

def set():
    top=Toplevel()
    top.title("设置")
    frame_tk=Frame(top)
    Label(frame_tk,text="待开发",width=32,height=5,bg="white").pack()
    frame_tk.pack(fill=X)


root=Tk()
root.title("更新纪录")

photo=PhotoImage(file=r".\images\1.gif")
frame1=Frame(root)
Label(frame1,text="更新日志",bg="white",width=61,height=6,font=20).pack(side=LEFT)
Label(frame1,image=photo,bg="white").pack(side=RIGHT,fill=Y)
frame1.pack(fill=X)

text=Text(root,height=40)

#text及滚动条绑定
scroll=Scrollbar(root)
scroll.pack(side=RIGHT,fill=Y)
text.config(yscrollcommand=scroll.set)
scroll.config(command=text.yview)
text.pack(pady=5)

frame=Frame(root,width=50)
Button(frame,text="操作说明",command=point).pack(side=RIGHT,pady=10,padx=10)
Button(frame,text="游戏介绍",command=introduce).pack(side=RIGHT,pady=10,padx=10)
Button(frame,text="设置",command=set).pack(side=LEFT,padx=10,pady=10)
Button(frame,text="开始游戏",command=root.destroy).pack(padx=100)
frame.pack(fill=X)

Insert("version-0.1  2020.4.3","界面创建，实现了飞机的移动、、以及全屏功能（F11） 全屏会有若干秒的卡顿\n修复了界面拉伸后卡在飞机屏幕外的bug")
Insert("version-0.2  2020.4.16","加入了小中大型飞机的敌机，实现其移动，后续待开发与改进\n添加bgm与音效")
Insert("version-0.3  2020.4.17","加入飞机子弹的射击，以及对子弹的碰撞检测\n敌机显示血条，同时加入敌机被击时的特效\n适度调整了音效声音大小")
Insert("version-0.4  2020.4.20","调整了帧率使游戏更平滑，添加了分数系统，击落敌机增加分数\n重新安装了pygame 修复了pygame无法打开的bug")
Insert("version-0.5  2020.4.21","添加了暂停功能，点击右上角图标或者按下空格使用")
Insert("version-0.6  2020.4.22","添加了补给包，不同的补给可以实现不同的效果，包括全屏炸弹以及双倍子弹\n解决了普通子弹与双倍子弹之间切换异常的bug")
Insert("version-0.7  2020.4.22+","左下角显示剩余生命数量，复活提供无敌时间,以及无敌效果内剩余时间的提示\n读取玩家最高分，同时增加 重新开始 or 结束游戏 的选项")
Insert("version-1.0  2020.4.23","调整了游戏难度，包括敌机速度，数量，以及补给发放时间，同时显示关卡信息\n完成了飞机大战的基础内容")
Insert("version-?  ?","从别后，忆相逢。几回魂梦与君同。今宵剩把银缸照，犹恐相逢是梦中")


mainloop()
