from tkinter.ttk import Button,Entry,Radiobutton,Scrollbar,Combobox
import tkinter.messagebox as msgbox
from tkinter import END,Label,Tk,StringVar,Listbox,messagebox,SINGLE,PhotoImage
from PIL import Image,ImageTk
import io
import re
import requests
# from urllib.request import urlopen
import threading
from urllib import request, parse
import tkinter as tk
import webbrowser
from lxml import etree
from  selenium import webdriver



from tkinter import ttk
class Movie_app:
    def __init__(self):
        self.win=Tk()
        self.win.geometry('600x420')
        self.win.title(" VIP视频破解工具")
        self.creat_res()
        self.creat_radiores()
        self.config()
        self.page=1
        self.p=Pro()
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
        self.t1=StringVar()#通道
        self.t3=StringVar()#爱奇艺，优酷，PPTV
        self.La_title=Label(self.win,text="地址:")
        self.La_way=Label(self.win,text="选择视频通道:")
        # self.R_way1=Radiobutton(self.win,text="通道A",variable=self.t1,value=True)
        # self.R_way2=Radiobutton(self.win,text="通道B",variable=self.t1,value=False)
        #控件内容设置
        self.numberChosen = Combobox(self.win,width=20)
        self.numberChosen['values']=('通道一','通道二','通道三','通道四','通道五','通道六','通道七','通道八','通道九','通道十')
        self.numberChosen.config(state='readonly')
        self.numberChosen.current(1)

        self.R_aiqiyi=Radiobutton(self.win,text="爱奇艺",variable=self.t3,value="a")
        self.R_youku=Radiobutton(self.win,text="优酷",variable=self.t3,value="y")
        self.R_pptv=Radiobutton(self.win,text="PPTV",variable=self.t3,value="p")
        self.t3.set('y')
        self.B_play=Button(self.win,text="播放▶")
        self.B_uppage=Button(self.win,text="上页")
        self.B_nextpage=Button(self.win,text="下页")
        self.B_search=Button(self.win,text="搜索全站")
        # self.La_mesasge=Label(self.win,text="☜  ⇠☸⇢  ☞",bg="pink")
        self.La_page=Label(self.win,bg="#BFEFFF")
        self.S_croll=Scrollbar(self.win)
        self.L_box=Listbox(self.win,bg="#BFEFFF",selectmode=SINGLE)
        self.E_address=Entry(self.win,textvariable=self.temp)
        self.La_title.place(x=10,y=50,width=50,height=30)
        self.E_address.place(x=70,y=50,width=200,height=30)
        self.B_play.place(x=280,y=50,width=80,height=80)
        # self.R_way1.place(x=160,y=10,width=70,height=30)
        # self.R_way2.place(x=240,y=10,width=70,height=30)
        self.numberChosen.place(x=120,y=10,width=180,height=30)
        self.La_way.place(x=10,y=10,width=100,height=30)
        # self.R_aiqiyi.place(x=20,y=100,width=70,height=30)
        self.R_youku.place(x=20,y=100,width=70,height=30)
        self.R_pptv.place(x=90,y=100,width=70,height=30)
        self.B_search.place(x=252,y=140,width=100,height=30)
        # self.La_mesasge.place(x=80,y=125,width=90,height=20)
        self.L_box.place(x=10,y=180,width=252,height=230)
        self.S_croll.place(x=260,y=180,width=20,height=230)
        self.B_uppage.place(x=10,y=140,width=50,height=30)
        self.B_nextpage.place(x=180,y=140,width=50,height=30)
        self.La_page.place(x=80,y=140,width=90,height=28)

    def creat_radiores(self):
        self.movie=StringVar()#电影
        self.S_croll2=Scrollbar()#分集
        self.La_pic=Label(self.win,bg="#E6E6FA")
        self.La_movie_message=Listbox(self.win,bg="#7EC0EE")
        self.R_movie=Radiobutton(self.win,text="电影",variable=self.movie,value="m")
        self.tv=Radiobutton(self.win,text="电视剧",variable=self.movie,value="t")
        self.zhongyi=Radiobutton(self.win,text="综艺",variable=self.movie,value="z")
        self.dongman=Radiobutton(self.win,text="动漫",variable=self.movie,value="d")
        self.jilupian=Radiobutton(self.win,text="纪录片",variable=self.movie,value="j")
        self.movie.set('m')
        self.B_view=Button(self.win,text="查看")
        self.B_info=Button(self.win,text="使用说明")
        self.B_clearbox=Button(self.win,text="清空列表")
        self.B_add=Button(self.win,text="添加到播放列表")
        self.R_movie.place(x=290,y=180,width=80,height=30)
        self.B_view.place(x=290,y=330,width=70,height=30)
        self.B_add.place(x=370,y=255,width=100,height=30)
        self.B_clearbox.place(x=500,y=255,width=70,height=30)
        self.tv.place(x=290,y=210,width=80,height=30)
        self.zhongyi.place(x=290,y=240,width=80,height=30)
        self.dongman.place(x=290,y=270,width=80,height=30)
        self.jilupian.place(x=290,y=300,width=80,height=30)
        self.La_movie_message.place(x=370,y=290,width=200,height=120)
        self.La_pic.place(x=370,y=10,width=200,height=240)
        self.B_info.place(x=290,y=370,width=70,height=30)
        self.S_croll2.place(x=568,y=290,width=20,height=120)

    def show_info(self):
        msg="""
        1.输入视频播放地址，即可播放
          下拉选择可切换视频源
        2.选择视频网，选择电视剧或者电影，
          搜索全网后选择想要看得影片，点
          查看，在右方list里选择分集视频
          添加到播放列表里点选播放
        3.复制网上视频连接，点击播放即可
        4.VIP视频也可以免费播放
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


    def uppage_(self):
        print('---------上一页---------')
        self.page-=1
        print(self.page)
        if self.page<1:
            self.page=1

    def nextpage_(self):
        print('----------下一页--------')
        self.page+=1
        print(self.page)
        if self.t3=="a" or self.t3=="y":
            if self.page>30:
                self.page=30
        elif self.t3=="p":
            if self.movie=="m":
                if self.page>165:
                    self.page=165
            elif self.movie == "t":
                if self.page > 85:
                    self.page = 85
            elif self.movie == "z":
                if self.page > 38:
                    self.page = 38
            elif self.movie == "d":
                if self.page > 146:
                    self.page = 146
            elif self.movie == "j":
                if self.page > 40:
                    self.page = 40

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
        print(self.movie_dic)
        if self.La_movie_message.get(self.La_movie_message.curselection())=="":
            messagebox.showwarning(title="警告",message='请在列表选择影片')
        else:
            print("电影名字:",self.La_movie_message.get(self.La_movie_message.curselection()))
            if self.movie.get()!="m":
                self.temp.set(self.new_more_dic[self.La_movie_message.get(self.La_movie_message.curselection())])
            else:
                self.temp.set(self.movie_dic[self.La_movie_message.get(self.La_movie_message.curselection())][0])


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
        if self.movie.get()!="m":#非电影类
            self.new_more_dic=self.p.get_more_tv_urls(self.movie_dic[self.L_box.get(cur_index)][0],self.t3.get(),self.movie.get())
            print(self.new_more_dic)
            for i,fenji_url in self.new_more_dic.items():
                self.La_movie_message.insert(END, i)
        else:#电影类
            self.La_movie_message.insert(END,self.L_box.get(cur_index))
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


class Pro:
    header_ai={'Referer': 'http://www.iqiyi.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.17 Safari/537.36'

    }
    header_you={'Referer': 'http://list.youku.com/category/video','User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
    header_pp = {'Referer': 'http://list.pptv.com/',
              'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
    way=False
    def __init__(self):
        pass

    def search_movies_type(self,u_name,u_type,page):#两个参数 根据状态输出规则
        dic1 = {'m': 1, 't': 2, 'z': 6, 'd': 4, 'j': 3}
        dic2 = {'m': 96, 't': 97, 'z': 85, 'd': 100, 'j': 84}
        dic3 = {'m': 1, 't': 2, 'z': 4, 'd': 3, 'j': 210548}
        headers={}
        #爱奇艺 a/电影m:1 t:2 z:6 d:4 j:3  优酷y / m:96 t:97 z:85 d:100 j:84 pptv  p/m:1 t:2 z:4 d:3 j:210548
        url, pa_movie_title, pa_movie_url, pa_move_pic='','','',''
        url_aiqiyi='http://list.iqiyi.com/www/{}/-------------24-{}-1-iqiyi--.html'.format(dic1[u_type],page)
        url_youku='https://list.youku.com/category/show/c_{}_s_1_d_1_p_{}.html'.format(dic2[u_type],page)
        # url_pptv='http://list.pptv.com/category/type_{}.html'.format(dic3[u_type])
        url_pptv='http://list.pptv.com/channel_list.html?page={}&type={}'.format(page,dic3[u_type])
        pa_ai_movie_title = '//li[@class="qy-mod-li"]/div/div/a[@class="qy-mod-link"]/@title'
        pa_ai_movie_url = '//li[@class="qy-mod-li"]/div/div/a[@class="qy-mod-link"]/@href'
        pa_ai_movie_pic = '//li[@class="qy-mod-li"]/div/div/a[@class="qy-mod-link"]/img/@src'
        pa_you_movie_title='//div[@class="p-thumb"]/a/@title'
        pa_you_movie_url='//div[@class="p-thumb"]/a/@href'
        pa_you_movie_pic='//div[@class="p-thumb"]/img[@class="quic"]/@src'
        pa_pp_movie_title='//li/a[@class="ui-list-ct"]/@title'
        pa_pp_movie_url='//li/a[@class="ui-list-ct"]/@href'
        pa_pp_movie_pic='//li/a[@class="ui-list-ct"]/p[@class="ui-pic"]/img/@data-src2'
        if u_name=="a":#如果是爱奇艺
            url=url_aiqiyi
            pa_movie_title=pa_ai_movie_title
            pa_movie_url=pa_ai_movie_url
            pa_move_pic=pa_ai_movie_pic
            headers=self.header_ai
        elif u_name=="y":#如果是优酷
            url=url_youku
            pa_movie_title=pa_you_movie_title
            pa_movie_url=pa_you_movie_url
            pa_move_pic=pa_you_movie_pic
            headers=self.header_you

        elif u_name=="p":#如果是PPTV
            url=url_pptv
            pa_movie_title=pa_pp_movie_title
            pa_movie_url=pa_pp_movie_url
            pa_move_pic=pa_pp_movie_pic
            headers=self.header_pp

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
            urls='http:'+urls
        return urls

    def get_more_tv_urls(self,url,u_name,u_type):#获取电视剧分集链接
        tv_dic_new = {}
        if u_name == 'y':
            url=self.change_youku_link(url)
            res = requests.get(url, headers=self.header_you).text.encode(encoding='utf-8').decode('utf-8')
            html = etree.HTML(res)
            print(res)
            if u_type=="m" or u_type=="t":
                self.tv_more_title = html.xpath('//div[@class="item item-num"]/@title')
                self.tv_more_url = html.xpath('//div[@class="item item-num"]/a[@class="sn"]/@href')
            elif u_type=="d":
                self.tv_more_title = html.xpath('//div[@class="item item-txt"]/@title')
                self.tv_more_url = html.xpath('//div[@class="item item-txt"]/a[@class="sn"]/@href')
            elif u_type=="z":
                self.tv_more_title = html.xpath('//div[@class="item item-cover"]/@title')
                self.tv_more_url = html.xpath('//div[@class="item item-cover"]/a/@href')
            elif u_type == "j":
                self.tv_more_title = html.xpath('//div[@class="item item-cover current"]/@title')
                self.tv_more_url = html.xpath('//div[@class="item item-cover current"]/a/@href')
        elif u_name == 'a':
            url=self.change_youku_link(url)
            res = requests.get(url, headers=self.header_ai).text.encode(encoding='utf-8').decode('utf-8')
            html = etree.HTML(res)
            print(res)
            if u_type=="m" or u_type=="t" or u_type=='d':
                self.tv_more_title = html.xpath(
                    '//li[@class="qy-episode-num"]li/a/@title')
                self.tv_more_url = html.xpath(
                    '//li[@class="qy-episode-num"]li/a/@href')
            elif u_type=="z" or u_type=="j":
                self.tv_more_title = html.xpath('//div[@class="recoAlbumTit"]/a[1]/@title')
                self.tv_more_url = html.xpath('//div[@class="recoAlbumTit"]/a[1]/@href')
        elif u_name == 'p':
            res = requests.get(url, headers=self.header_pp).text.encode(encoding='utf-8').decode('utf-8')
            # html = etree.HTML(res)
            self.tv_more_url2 = re.compile('{"url":"(.+?)"').findall(res)
            self.tv_more_url = self.change_urlink(self.tv_more_url2)
            self.tv_more_title = ["第{}集".format(x) for x in range(1, len(self.tv_more_url) + 1)]
        for i, j in zip(self.tv_more_title, self.tv_more_url):
            tv_dic_new[i] = j
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




