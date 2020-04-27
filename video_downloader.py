# -*- coding:utf-8 -*-
from tkinter.filedialog import askdirectory
from urllib import request, parse
from bs4 import BeautifulSoup

import tkinter.messagebox as msgbox
import tkinter as tk
import webbrowser
import re
import os
import types
import time

import shutil
import requests,threading
from urllib.request import urlretrieve
from pyquery import PyQuery as pq
from multiprocessing import Pool

from tkinter import ttk
"""
类说明:爱奇艺、优酷等实现在线观看以及视频下载的类

Parameters:
	width - tkinter主界面宽
	height - tkinter主界面高

Returns:
	无

Modify:
	2017-05-09
"""
class APP:
	def __init__(self, width = 500, height = 300):
		self.w = width
		self.h = height
		self.title = ' VIP视频破解助手下载器版'
		self.root = tk.Tk(className=self.title)
		self.url = tk.StringVar()
		self.v = tk.IntVar()
		self.v.set(1)
		self.progress = 0
		#Frame空间
		frame_1 = tk.Frame(self.root)
		frame_2 = tk.Frame(self.root)
		frame_3 = tk.Frame(self.root)
		frame_4 = tk.Frame(self.root)
		frame_5 = tk.Frame(self.root)
		#Menu菜单
		menu = tk.Menu(self.root)
		self.root.config(menu = menu)
		filemenu = tk.Menu(menu,tearoff=0)
		moviemenu = tk.Menu(menu,tearoff = 0)
		menu.add_cascade(label = '友情链接', menu = moviemenu)

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

		#控件内容设置
		group = tk.Label(frame_1,text = '请选择一个视频播放通道：', padx = 10, pady = 10)
		self.numberChosen = ttk.Combobox(frame_1,width=20,textvariable=self.v)
		self.numberChosen['values']=('通道一','通道二','通道三','通道四','通道五','通道六','通道七','通道八','通道九','通道十')
		self.numberChosen.config(state='readonly')
		self.numberChosen.current(1)

		label1 = tk.Label(frame_2, text = "请输入视频链接：")
		entry = tk.Entry(frame_2, textvariable = self.url, highlightcolor = 'Fuchsia', highlightthickness = 1,width = 45)
		label2 = tk.Label(frame_3, text = " ")
		play = tk.Button(frame_3, text = "播放", font = ('楷体',12), fg = 'Purple', width = 2, height = 1, command = self.video_play)
		label3 = tk.Label(frame_3, text = " ")
		download = tk.Button(frame_3, text = "下载", font = ('楷体',12), fg = 'Purple', width = 2, height = 1, command = self.download_wmxz)


		label_explain = tk.Label(frame_4, fg = 'red', font = ('楷体',12), text = '\n注意：支持大部分主流视频网站的视频播放！\n此软件仅用于交流学习，请勿用于任何商业用途！')
		label_warning = tk.Label(frame_4, fg = 'blue', font = ('楷体',12),text = '\n建议：将Chrome内核浏览器设置为默认浏览器\n')


		label_tip = tk.Label(frame_5, fg = 'green', font = ('楷体',10),text = '如果要下载视频，请把程序放在文件夹下运行\n点击下载视频会进入后台下载，界面不展示下载进程\n进度条走动表示可以正常点击')
		self.progressbar = ttk.Progressbar(frame_5, orient = "horizontal", length=300, mode="determinate", value=0,maximum=100,variable=self.progress)




		#控件布局
		frame_1.pack()
		frame_2.pack()
		frame_3.pack()
		frame_4.pack()
		frame_5.pack()
		group.grid(row = 0, column = 0)
		self.numberChosen.grid(row = 0, column = 1)
		label1.grid(row = 0, column = 0)
		entry.grid(row = 0, column = 1)
		label2.grid(row = 0, column = 2)
		play.grid(row = 0, column = 2,ipadx = 35, ipady = 7)
		label3.grid(row = 0, column = 4)
		download.grid(row = 0, column = 9,ipadx = 10, ipady = 5)
		label_explain.grid(row = 1, column = 0)
		label_warning.grid(row = 2, column = 0)
		label_tip.grid(row = 0, column = 0)
		self.progressbar.grid(row = 1, column = 0)
		self.progressbar.start()
	"""
	函数说明:jsonp解析

	Parameters:
		_jsonp - jsonp字符串

	Returns:
		_json - json格式数据

	Modify:
		2017-05-11
	"""
	def loads_jsonp(self, _jsonp):
		try:
			_json = json.loads(re.match(".*?({.*}).*",_jsonp,re.S).group(1))
			return _json
		except:
			raise ValueError('Invalid Input')

	"""
	函数说明:视频播放

	Parameters:
		self

	Returns:
		无

	Modify:
		2017-05-09
	"""
	"""
	 <option value="https://jiexi.071811.cc/jx.php?url=">石头解析</option>
      <option value="http://jx.598110.com/?url=" selected>一号</option>
      <option value="http://vip.jlsprh.com/?url=">二号</option>
      <option value="http://jx.618ge.com/?url=">三号</option>
      <option value="http://jx.drgxj.com/?url=">四号</option>
      <option value="http://jx.du2.cc/?url=">五号</option>
      <option value="https://vip.mpos.ren/v/?url=">人人解析</option>
      <option value="http://jx.618g.com/?url=">618G</option>
      <option value="http://jx.cesms.cn/?url=">大亨影院解析</option>
      <option value="https://660e.com/?url=">乐乐云</option>
      <option value="https://www.administratorw.com/admin.php?url=">无名小站</option>
      <option value="https://yun.odflv.com/?url=">ODFLV</option>
      <option value="http://api.baiyug.vip/index.php?url=">百域阁</option>
      <option value="http://goudidiao.com/?url=">够低调</option>
      <option value="https://jx.maoyun.tv/index.php?id=">猫云</option>
      <option value="http://www.1717yun.com/jx/vip/index.php?url=">1717云</option>
      <option value="http://api.xfsub.com/index.php?url=">旋风解析</option>
      <option value="http://q.z.vip.totv.72du.com/?url=">VIP看看</option>
      <option value="http://jx.api.163ren.com/vod.php?url=">163人</option>
      <option value="http://www.0335haibo.com/tong.php?url=">CKFLV</option> 
      <option value="http://www.wmxz.wang/video.php?url=">无名小站2</option>
      <option value="http://www.vipjiexi.com/yun.php?url=">眼睛会下雨</option>
      <option value="https://hhh.qqplayer.cn/beac.php?url=">人人发布</option>
      <option value="http://j.zz22x.com/jx/?url=">花园解析</option>
      <option value="http://api.nepian.com/ckparse/?url=">那片解析</option>
      <option value="https://vip.bljiex.com/?v=">BL解析</option>
	  """
	def video_play(self):
		#视频解析网站地址
		if self.numberChosen.get() == '通道一':
			port = 'https://jiexi.071811.cc/jx.php?url='
		elif self.numberChosen.get() == '通道二':
			port = 'https://jx.618g.com/?url='
		elif self.numberChosen.get() == '通道三':
			port = 'http://vip.jlsprh.com/?url='
		elif self.numberChosen.get() == '通道四':
			port = 'http://www.vipjiexi.com/yun.php?url='
		elif self.numberChosen.get() == '通道五':
			port = 'http://jx.drgxj.com/?url='
		elif self.numberChosen.get() == '通道六':
			port = 'http://jx.du2.cc/?url='
		elif self.numberChosen.get() == '通道七':
			port = 'https://vip.mpos.ren/v/?url='
		elif self.numberChosen.get() == '通道八':
			port = 'http://jx.cesms.cn/?url='
		elif self.numberChosen.get() == '通道九':
			port = 'https://660e.com/?url='
		else:
			port = 'http://j.zz22x.com/jx/?url='
		#正则表达是判定是否为合法链接
		if re.match(r'^https?:/{2}\w.+$', self.url.get()):
			#链接获取
			ip = self.url.get()
			#链接加密
			ip = parse.quote_plus(ip)
			#获取time、key、url
			get_url = port + '%s' % ip 
			#请求之后立刻打开
			webbrowser.open(get_url)
		else:
			msgbox.showerror(title='错误',message='视频链接地址无效，请重新输入！')

	"""
	函数说明:视频下载，通过无名小站抓包(已经无法使用)

	Parameters:
		self

	Returns:
		无

	Modify:
		2017-06-15
	"""
	def download_wmxz(self):	
		if re.match(r'^https?:/{2}\w.+$', self.url.get()):
    			#视频链接获取
			ip = self.url.get()
			#视频链接加密
			ip = parse.quote_plus(ip)
			msgbox.showerror(title='点击成功',message='视频会进入后台下载，切勿重复点击！')
			# video_down(ip)
			t = threading.Thread(target=video_down, args=[ip]) 
			t.setDaemon(True)   # 守护--就算主界面关闭，线程也会留守后台运行（不对!）
			t.start()           # 启动	
		else:
			msgbox.showerror(title='错误',message='视频链接地址无效，请重新输入！')



	"""
	函数说明:tkinter窗口居中

	Parameters:
		self

	Returns:
		无

	Modify:
		2017-05-09
	"""
	def center(self):
		ws = self.root.winfo_screenwidth()
		hs = self.root.winfo_screenheight()
		x = int( (ws/2) - (self.w/2) )
		y = int( (hs/2) - (self.h/2) )
		self.root.geometry('{}x{}+{}+{}'.format(self.w, self.h, x, y))

	"""
	函数说明:loop等待用户事件

	Parameters:
		self

	Returns:
		无

	Modify:
		2017-05-09
	"""
	def loop(self):
		self.root.resizable(False, False)	#禁止修改窗口大小
		self.center()						#窗口居中
		self.root.mainloop()




class video_down():
    def __init__(self,url):
        # 拼接全民解析url
        self.api='https://jx.618g.com'
        self.get_url = 'https://jx.618g.com/?url=' + url
        #设置UA模拟浏览器访问
        self.head = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
        #设置多线程数量
        self.thread_num=32
        #当前已经下载的文件数目
        self.i = 0
        # 调用网页获取
        html = self.get_page(self.get_url)
        if html:
            # 解析网页
            self.parse_page(html)
    def get_page(self,get_url):
        try:
            print('正在请求目标网页....',get_url)
            response=requests.get(get_url,headers=self.head)
            if response.status_code==200:
                #print(response.text)
                print('请求目标网页完成....\n 准备解析....')
                self.head['referer'] = get_url
                return response.text
        except Exception:
            print('请求目标网页失败，请检查错误重试')
            return None

    def parse_page(self,html):
        print('目标信息正在解析........')
        doc=pq(html)
        self.title=doc('head title').text()
        print(self.title)
        url = doc('#player').attr('src')[17:]
        html=self.get_m3u8_1(url).strip()
        #self.url = url + '800k/hls/index.m3u8'
        self.url = url[:-10] +html
        print(self.url)
        print('解析完成，获取缓存ts文件.........')
        self.get_m3u8_2(self.url)
    def get_m3u8_1(self,url):
        try:
            response=requests.get(url,headers=self.head)
            html=response.text
            print('获取ts文件成功，准备提取信息')
            return html[-20:]
        except Exception:
            print('缓存文件请求错误1，请检查错误')

    def get_m3u8_2(self,url):
        try:
            response=requests.get(url,headers=self.head)
            html=response.text
            print('获取ts文件成功，准备提取信息')
            self.parse_ts_2(html)
        except Exception:
            print('缓存文件请求错误2，请检查错误')
    def parse_ts_2(self,html):
        pattern=re.compile('.*?(.*?).ts')
        self.ts_lists=re.findall(pattern,html)
        print('信息提取完成......\n准备下载...')
        self.pool()
    def pool(self):
        print('经计算需要下载%d个文件' % len(self.ts_lists))
        self.ts_url = self.url[:-10]
        if self.title not in os.listdir():
            os.makedirs(self.title)
        print('正在下载...所需时间较长，请耐心等待..')
        #开启多进程下载
        # pool=Pool(1)
        # pool.map(self.save_ts,[ts_list for ts_list in self.ts_lists])
        # pool.close()
        # pool.join()
        for ts_list in self.ts_lists:
            self.save_ts(ts_list)  	  			
        print('下载完成')
        self.ts_to_mp4()
    def ts_to_mp4(self):
        print('ts文件正在进行转录mp4......')
        str='copy /b '+self.title+'\*.ts '+self.title+'.mp4'
        os.system(str)
        filename=self.title+'.mp4'
        if os.path.isfile(filename):
            print('转换完成，祝你观影愉快')
            shutil.rmtree(self.title)

    def save_ts(self,ts_list):
        try:
            ts_urls = self.ts_url + '{}.ts'.format(ts_list)
            self.i += 1
            print('当前进度%d/%d'%(self.i,len(self.ts_lists)))
            urlretrieve(url=ts_urls, filename=self.title + '/{}.ts'.format(ts_list))
        except Exception:
            print('保存文件出现错误')




if __name__ == '__main__':
	app = APP()			#实例化APP对象
	app.loop()			#loop等待用户事件




