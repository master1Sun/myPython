from tkinter.ttk import Button,Entry,Radiobutton,Scrollbar,Combobox
import tkinter.messagebox as msgbox
from tkinter import END,Label,Tk,StringVar,Listbox,messagebox,SINGLE,PhotoImage
from PIL import Image,ImageTk
import io
import re
import requests
import threading
from urllib import request, parse
import tkinter as tk
import webbrowser
from lxml import etree
from  selenium import webdriver
import random


class Movie_app:
    def __init__(self):
        self.win=Tk()
        self.win.title(" VIP视频破解工具")
        self.creat_res()
        self.creat_radiores()
        self.config()
        self.page=1
        self.p=Pro()
        self.win.resizable(0,0) #防止用户调整尺寸
        curWidth = 600
        curHight = 520
        # 获取屏幕宽度和高度
        scn_w, scn_h = self.win.maxsize()
        # 计算中心坐标
        cen_x = (scn_w - curWidth) / 2
        cen_y = (scn_h - curHight) / 2
        # 设置窗口初始大小和位置
        size_xy = '%dx%d+%d+%d' % (curWidth, curHight, cen_x, cen_y)
        self.win.geometry(size_xy)
        self.win.mainloop()


    def creat_res(self):
        #Menu菜单
        menu = tk.Menu(self.win)
        self.win.config(menu = menu)
        moviemenu = tk.Menu(menu,tearoff = 0)
        menu.add_cascade(label = '友情链接', menu = moviemenu)
        downmenu = tk.Menu(menu,tearoff = 0)
        #各个网站链接
        moviemenu.add_command(label = '网易公开课',command = lambda :webbrowser.open('http://open.163.com/'))
        moviemenu.add_command(label = '腾讯视频',command = lambda :webbrowser.open('http://v.qq.com/'))
        moviemenu.add_command(label = '搜狐视频',command = lambda :webbrowser.open('http://tv.sohu.com/'))
        moviemenu.add_command(label = '芒果TV',command = lambda :webbrowser.open('http://www.mgtv.com/'))
        moviemenu.add_command(label = '爱奇艺',command = lambda :webbrowser.open('http://www.iqiyi.com/'))
        moviemenu.add_command(label = 'PPTV',command = lambda :webbrowser.open('http://www.bilibili.com/'))
        moviemenu.add_command(label = '优酷',command = lambda :webbrowser.open('http://www.youku.com/'))
        moviemenu.add_command(label = '乐视',command = lambda :webbrowser.open('http://www.le.com/'))
        moviemenu.add_command(label = '土豆',command = lambda :webbrowser.open('http://www.tudou.com/'))
        moviemenu.add_command(label = 'A站',command = lambda :webbrowser.open('http://www.acfun.tv/'))
        moviemenu.add_command(label = 'B站',command = lambda :webbrowser.open('http://www.bilibili.com/'))

        self.temp=StringVar()#url地址
        self.temp2=StringVar()
        self.search=StringVar()#搜索
        self.t1=StringVar()#通道
        self.t3=StringVar()#爱奇艺，优酷，PPTV
        self.La_title=Label(self.win,text="第三方视频地址:")
        self.La_way=Label(self.win,text="选择视频解码通道:")
        self.La_mc=Label(self.win,text="关键字搜索:")
        #控件内容设置
        self.numberChosen = Combobox(self.win,width=20)
        self.numberChosen['values']=('通道一','通道二','通道三','通道四','通道五','通道六','通道七','通道八','通道九','通道十')
        self.numberChosen.config(state='readonly')
        self.numberChosen.current(0)

        self.B_play=Button(self.win,text="播放▶")
        self.B_searchSimple=Button(self.win,text="关键字搜索")
        self.B_uppage=Button(self.win,text="上页")
        self.B_nextpage=Button(self.win,text="下页")
        self.B_search=Button(self.win,text="搜索全站")
        self.La_page=Label(self.win,bg="#BFEFFF")
        self.S_croll=Scrollbar(self.win)
        self.L_box=Listbox(self.win,bg="#BFEFFF",selectmode=SINGLE)
        self.E_address=Entry(self.win,textvariable=self.temp)
        self.E_search=Entry(self.win,textvariable=self.search)
        self.label_explain = Label(self.win, fg = 'red', font = ('楷体',12), text = '\n注意：支持大部分主流视频网站的视频播放！\n此软件仅用于交流学习，请勿用于任何商业用途！\n在上面输入框输入现在主流视频网站网页地址\n点击播放弹出浏览器可以解码播放')
        self.label_explain.place(x=10,y=90,width=360,height=90)
        self.La_title.place(x=1,y=50,width=90,height=30)
        self.E_address.place(x=100,y=50,width=200,height=30)
        self.B_play.place(x=310,y=50,width=60,height=30)
        self.La_way.place(x=10,y=10,width=100,height=30)
        self.numberChosen.place(x=120,y=10,width=180,height=30)
        self.E_search.place(x=90,y=200,width=160,height=30)
        self.B_searchSimple.place(x=280,y=200,width=80,height=30)
        self.La_mc.place(x=10,y=200,width=70,height=30)
        self.B_search.place(x=252,y=240,width=100,height=30)
        self.L_box.place(x=10,y=280,width=252,height=230)
        self.S_croll.place(x=260,y=280,width=20,height=230)
        self.B_uppage.place(x=10,y=240,width=50,height=30)
        self.B_nextpage.place(x=180,y=240,width=50,height=30)
        self.La_page.place(x=80,y=240,width=90,height=28)

    def creat_radiores(self):
        self.movie=StringVar()#电影
        self.S_croll2=Scrollbar()#分集
        self.La_pic=Label(self.win,bg="#E6E6FA")
        self.La_movie_message=Listbox(self.win,bg="#7EC0EE")
        self.R_movie=Radiobutton(self.win,text="电影",variable=self.movie,value="m")
        self.tv=Radiobutton(self.win,text="电视剧",variable=self.movie,value="t")
        self.zhongyi=Radiobutton(self.win,text="综艺",variable=self.movie,value="z")
        self.dongman=Radiobutton(self.win,text="动漫",variable=self.movie,value="d")
        self.jilupian=Radiobutton(self.win,text="排行榜",variable=self.movie,value="j")
        self.movie.set('m')
        self.B_view=Button(self.win,text="查看")
        self.B_info=Button(self.win,text="使用说明")
        self.B_clearbox=Button(self.win,text="清空列表")
        self.B_add=Button(self.win,text="打开浏览器观看")
        self.R_movie.place(x=290,y=280,width=80,height=30)
        self.B_view.place(x=290,y=430,width=70,height=30)
        self.B_add.place(x=370,y=255,width=100,height=30)
        self.B_clearbox.place(x=500,y=255,width=70,height=30)
        self.tv.place(x=290,y=310,width=80,height=30)
        self.zhongyi.place(x=290,y=340,width=80,height=30)
        self.dongman.place(x=290,y=370,width=80,height=30)
        self.jilupian.place(x=290,y=400,width=80,height=30)
        self.La_movie_message.place(x=370,y=290,width=200,height=220)
        self.La_pic.place(x=370,y=10,width=200,height=240)
        self.B_info.place(x=290,y=470,width=70,height=30)
        self.S_croll2.place(x=568,y=290,width=20,height=220)

    def show_info(self):
        msg="""
        1.输入视频播放地址，即可播放
          下拉选择可切换视频源
        2.选择视频网，选择电视剧或者电影，
          搜索全网后选择想要看得影片，点
          查看，在右方list里选择分集视频
          添加到播放列表里点选播放
        3.复制网上视频连接
          点击播放即可（VIP视频也可以免费播放）
        4.此软件仅用于交流学习
          请勿用于任何商业用途！
        5.此软件内容来源于互联网
          此软件不承担任何由于内容的合法性及
          健康性所引起的争议和法律责任。
        6.欢迎大家对此软件内容侵犯版权等
          不合法和不健康行为进行监督和举报
        """
        messagebox.showinfo(title="使用说明",message=msg)

    def config(self):
        self.t1.set(True)
        self.B_play.config(command=self.play_url_movie)
        self.B_search.config(command=self.search_full_movie)
        self.B_info.config(command=self.show_info)
        self.S_croll.config(command=self.L_box.yview)
        self.L_box['yscrollcommand']=self.S_croll.set
        self.S_croll2.config(command=self.La_movie_message.yview)
        self.La_movie_message['yscrollcommand']=self.S_croll2.set
        self.B_view.config(command=self.view_movies)
        self.B_add.config(command=self.add_play_list)
        self.B_clearbox.config(command=self.clear_lisbox2)
        self.B_uppage.config(command=self.uppage_)
        self.B_nextpage.config(command=self.nextpage_)
        self.B_searchSimple.config(command=self.searchSimple)

    def uppage_(self):
        print('---------上一页---------')
        self.page-=1
        print(self.page)
        if self.page<1:
            self.page=1
        self.search_full_movie()
    def nextpage_(self):
        print('----------下一页--------')
        self.page+=1
        print(self.page)
        self.search_full_movie()

    def clear_lisbox(self):
        self.L_box.delete(0,END)

    def clear_lisbox2(self):
        self.La_movie_message.delete(0,END)

    def search_full_movie(self):
        print("-----search----")
        self.La_page.config(text="当前页:{}".format(self.page))
        self.clear_lisbox()
        try:
            movie_url, movie_title, movie_src_pic=self.p.get_movie_res(self.t3.get(),self.movie.get(),self.page)
            self.movie_dic={}
            for i,j,k in zip(movie_title,movie_url,movie_src_pic):
                self.movie_dic[i]=[j,k]
            for title in movie_title:
                self.L_box.insert(END,title)
            print(self.movie_dic)
            return self.movie_dic
        except:
            messagebox.showerror(title='警告',message='请选择电影或者电视剧')

    def add_play_list(self):
        print('---------playlist----------')
        # print(self.movie_dic)
        if self.La_movie_message.get(self.La_movie_message.curselection())=="":
            messagebox.showwarning(title="警告",message='请在列表选择影片')
        else:
            print("电影名字:",self.La_movie_message.get(self.La_movie_message.curselection()))
            # self.temp.set('http://www.133kp.com' + self.new_more_dic[self.La_movie_message.get(self.La_movie_message.curselection())])
            webbrowser.open('http://www.133kp.com' + self.new_more_dic[self.La_movie_message.get(self.La_movie_message.curselection())])


    def view_pic(self,pic_url):
        print('--------viewpic---------')
        pa_url_check=r'//.+[.]jpg'
        if re.match(pa_url_check,pic_url):
            print("ok")
            pic_url="http:"+pic_url
        print(pic_url)
        data=requests.get(pic_url).content
        # data=urlopen(pic_url).read()
        io_data=io.BytesIO(data)
        self.img=Image.open(io_data)
        self.u=ImageTk.PhotoImage(self.img)
        self.La_pic.config(image=self.u)

    def view_movies(self):
        print("--------viewmovie----------")
        self.clear_lisbox2()
        cur_index=self.L_box.curselection()
        print(self.L_box.get(cur_index))
        self.new_more_dic=self.p.get_more_tv_urls(self.movie_dic[self.L_box.get(cur_index)][0],self.t3.get(),self.movie.get())
        print(self.new_more_dic)
        for i,fenji_url in self.new_more_dic.items():
            self.La_movie_message.insert(END, i)
        self.view_pic(self.movie_dic[self.L_box.get(self.L_box.curselection())][1])#加载图片

    def play_url_movie(self):
        print("--------ok-----------")
        # print(type(self.t1.get()),self.t1.get())
        if self.temp.get()=="":
            messagebox.showwarning(title="警告",message="请先输入视频地址")
        else:
            if self.numberChosen.get()!="":
                self.p.play_movie(self.temp.get(),self.numberChosen.get())
            else:
                messagebox.showwarning(title='警告',message='请选择通道')
    def searchSimple(self):
        if self.search.get()=="":
            messagebox.showwarning(title="警告",message="请先输入搜索关键字")
        else:    
            self.clear_lisbox()  
            url = 'https://www.133kp.com//index.php?m=vod-search&wd={}'.format(self.search.get())
            res=requests.get(url=url,headers=self.p.header).content.decode('utf-8')
            html=etree.HTML(res)
            movie_size=html.xpath('//input[@class="pagego"]/@size')
            list = [] 
            for s in range(0, int(movie_size[0])):
                url = 'https://www.133kp.com/vod-search-pg-{}-wd-{}.html'.format(s+1,self.search.get())
                list.append(self.p.simpleSearch(url)) 
            # movie_url, movie_title, movie_src_pic=self.p.simpleSearch(self.search.get())
            self.movie_dic={}
            i = 0
            for b in list:
                for i,j,k in zip(b[0],b[1],b[2]):
                    self.movie_dic[i]=[j,re.findall(r'[(](.*?)[)]', k)[0]]
                for title in b[0]:
                    self.L_box.insert(END,title)
            print(self.movie_dic)


class Pro:
    header={'Referer': 'https://www.133kp.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.17 Safari/537.36'
    }
    way=False
    def __init__(self):
        pass

    def simpleSearch(self,url):
        headers=self.header
        pa_movie_title = '//div[@class="hy-video-details active clearfix"]/div/dl/dd/div/h3/a/text()'
        pa_movie_url = '//div[@class="hy-video-details active clearfix"]/div/dl/dt/a/@href'
        pa_move_pic = '//div[@class="hy-video-details active clearfix"]/div/dl/dt/a/attribute::style'
        res=requests.get(url=url,headers=headers).content.decode('utf-8')
        html=etree.HTML(res)
        movie_url=html.xpath(pa_movie_url)
        movie_title=html.xpath(pa_movie_title)
        movie_src_pic=html.xpath(pa_move_pic)
        return movie_title,movie_url,movie_src_pic

    def search_movies_type(self,u_name,u_type,page):#两个参数 根据状态输出规则
        dic3 = {'m': 1, 't': 2, 'z': 4, 'd': 3, 'j': 'label-top-pg-1'}
        headers={}
        if u_type=='j':
            url = 'https://www.133kp.com/{}.html'.format(dic3[u_type])
        else:    
            url = 'https://www.133kp.com/vod-list-id-{}-pg-{}-order--by-time-class--year--letter--area--lang-.html'.format(dic3[u_type],page)
        headers=self.header
        pa_ai_movie_title = '//a[@class="videopic lazy"]/@title'
        pa_ai_movie_url = '//a[@class="videopic lazy"]/@href'
        pa_ai_movie_pic = '//a[@class="videopic lazy"]/@data-original'
        pa_movie_title=pa_ai_movie_title
        pa_movie_url=pa_ai_movie_url
        pa_move_pic=pa_ai_movie_pic
        return url,pa_movie_title,pa_movie_url,pa_move_pic,headers


    def get_movie_res(self,u_name,u_type,page):#输出电影名 链接 图片
        url, pa_movie_title, pa_movie_url, pa_move_pic,headers=self.search_movies_type(u_name,u_type,page)
        res=requests.get(url=url,headers=headers).content.decode('utf-8')
        # print(res)
        html=etree.HTML(res)
        movie_url=html.xpath(pa_movie_url)
        movie_title=html.xpath(pa_movie_title)
        movie_src_pic=html.xpath(pa_move_pic)
        print(len(movie_title),movie_title)
        print(len(movie_url),movie_url)
        print(len(movie_src_pic),movie_src_pic)
        return movie_url,movie_title,movie_src_pic

    def change_urlink(self,lis):
        for i in range(len(lis)):
            if '\\' in lis[i]:
                lis[i] = lis[i].replace('\\', '')
        # print(lis)
        return lis

    def change_youku_link(self,urls):
        pa_link='//.+[.]html'
        if re.match(pa_link,urls):
            urls='http://www.133kp.com'+urls
        return urls

    def get_more_tv_urls(self,url,u_name,u_type):#获取电视剧分集链接
        tv_dic_new = {}
        # url=self.change_youku_link(url)
        url='http://www.133kp.com'+url
        res = requests.get(url, headers=self.header).text.encode(encoding='utf-8').decode('utf-8')
        html = etree.HTML(res)
        print(res)
        self.tv_more_title = html.xpath('//div[@class="panel clearfix"]/div/ul/li/a/@title')
        self.tv_more_url = html.xpath('//div[@class="panel clearfix"]/div/ul/li/a/@href')

        for i, j in zip(self.tv_more_title, self.tv_more_url):
            tv_dic_new[i+str( random.randint(0,10000))] = j
        print(len(self.tv_more_title), self.tv_more_title)
        print(len(self.tv_more_url), self.tv_more_url)
        print(tv_dic_new)
        return tv_dic_new

    def url_change(self,url,flag):
        #视频解析网站地址
        if flag == '通道一':
           port = 'https://jiexi.071811.cc/jx.php?url={}'
        elif flag== '通道二':
           port = 'https://jx.618g.com/?url={}'
        elif flag == '通道三':
           port = 'http://vip.jlsprh.com/?url={}'
        elif flag == '通道四':
           port = 'http://www.vipjiexi.com/yun.php?url={}'
        elif flag == '通道五':
           port = 'http://jx.drgxj.com/?url={}'
        elif flag == '通道六':
           port = 'http://jx.du2.cc/?url={}'
        elif flag == '通道七':
           port = 'https://vip.mpos.ren/v/?url={}'
        elif flag == '通道八':
           port = 'http://jx.cesms.cn/?url={}'
        elif flag == '通道九':
           port = 'https://660e.com/?url={}'
        else:
           port = 'http://j.zz22x.com/jx/?url={}'

        new_url=port.format(url)
        return new_url


    def play_movie(self,url,flag):
        play_url=self.url_change(url,flag)
        print('播放地址:',play_url)
        webbrowser.open(play_url)
        # web = webdriver.Chrome()
        # web.get(play_url)


if __name__ == '__main__':
    m=Movie_app()


