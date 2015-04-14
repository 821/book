# -*- coding: utf-8 -*-
import requests,os,shutil,sys,threading,time,win32con
from tkinter import *
import win32clipboard as w

proxy = {'http':'http://127.0.0.1:8002'}

def tryLink(link):
	global die
	die = 0
	try:
		r = requests.get(link, proxies=proxy, stream=True, timeout=None)
	except BaseException:
		time.sleep(1)
		try:
			r = requests.get(link, proxies=proxy, stream=True, timeout=None)
		except BaseException:
			print(link)
			die = die + 1
			return
		else:
			return r
	else:
		return r

def pDown(link, Path):
	s = tryLink(link+'.png')
	if s.status_code == 200:
		with open(Path, 'wb') as fd:
			for chunk in s.iter_content(chunk_size=1024):
				fd.write(chunk)
			del s
	elif s.status_code == 404:
		tryLink(link+'.jpg')
		if s.status_code == 200:
			with open(Path, 'wb') as fd:
				for chunk in s.iter_content(chunk_size=1024):
					fd.write(chunk)
				del r
		elif s.status_code == 404:
			return True

def AttDown(Atts, ssFolder, BasicURL):
	FileExist=os.path.isfile(ssFolder+Atts+'.pdg')
	if FileExist == False:
		pDown(BasicURL+Atts,ssFolder+Atts+'.pdg')

def fowDown(ssFolder, BasicURL):
	for num in range(1, 1000):
		pgNum=str(num).zfill(3)
		ssFile=ssFolder+'fow'+pgNum+'.pdg'
		FileExist=os.path.isfile(ssFile)
		if FileExist == True:
			FileSize=os.path.getsize(ssFile)
			if FileSize == 0:
				if pDown(BasicURL+'fow'+pgNum, ssFile):
					break
		else:
			if pDown(BasicURL+'fow'+pgNum, ssFile):
				break

def tocDown(ssFolder, BasicURL):
	for num in range(1, 10000):
		pgNum=str(num).zfill(5)
		ssFile=ssFolder+'!'+pgNum+'.pdg'
		FileExist=os.path.isfile(ssFile)
		if FileExist == True:
			FileSize=os.path.getsize(ssFile)
			if FileSize == 0:
				if pDown(BasicURL+'!'+pgNum, ssFile):
					break
		else:
			if pDown(BasicURL+'!'+pgNum, ssFile):
				break

class attsDown(threading.Thread):
	def __init__(self, ssFolder, BasicURL):
		threading.Thread.__init__(self)
		self.ssFolder = ssFolder
		self.BasicURL = BasicURL

	def run(self):
		AttDown('cov001', self.ssFolder, self.BasicURL)
		AttDown('cov002', self.ssFolder, self.BasicURL)
		AttDown('bok001', self.ssFolder, self.BasicURL)
		AttDown('bok002', self.ssFolder, self.BasicURL)
		AttDown('leg001', self.ssFolder, self.BasicURL)
		AttDown('bac001', self.ssFolder, self.BasicURL)
		fowDown(self.ssFolder, self.BasicURL)
		tocDown(self.ssFolder, self.BasicURL)

class pageDown(threading.Thread):
	def __init__(self, firstpage, lastpage, ssFolder, BasicURL):
		threading.Thread.__init__(self)
		self.ssFolder = ssFolder
		self.BasicURL = BasicURL
		self.firstpage = firstpage
		self.lastpage = lastpage

	def run(self):
		for num in range(self.firstpage, self.lastpage+1):
			pgNum=str(num).zfill(6)
			ssFile=self.ssFolder+pgNum+'.pdg'
			FileExist=os.path.isfile(ssFile)
			if FileExist == True:
				FileSize=os.path.getsize(ssFile)
				if FileSize == 0:
					pDown(self.BasicURL+pgNum, ssFile)
			else:
				pDown(self.BasicURL+pgNum, ssFile)

def getBook(gzBook):
	#釋放變量
	BasicURL=gzBook[0]
	firstpage=int(gzBook[1])
	lastpage=int(gzBook[2])
	ssid=gzBook[3]
	bookname=gzBook[4]

	#文件夾
	ssFolder='F:\\ss\\'+bookname+'_'+ssid+'\\'
	FolderExist=os.path.isdir(ssFolder)
	if FolderExist == False:
		os.mkdir(r'f:/ss/'+bookname+'_'+ssid+'/')

	#生成bookinfo
	BookinfoExist=os.path.isfile(ssFolder+'Bookinfo.dat')
	if BookinfoExist == False:
		Bookinfo=open(ssFolder+'Bookinfo.dat', 'w+')
		Bookinfo.write('[General Information]'+'\n')
		Bookinfo.write('书名='+bookname+'\n')
		Bookinfo.write('作者='+'\n')
		Bookinfo.write('页数='+str(lastpage)+'\n')
		Bookinfo.write('SS号='+ssid+'\n')
		Bookinfo.write('DX号='+'\n')
		Bookinfo.write('出版日期='+'\n')
		Bookinfo.write('出版社='+'\n')
		Bookinfo.write(BasicURL+'\n')
		Bookinfo.close()

	thread1 = attsDown(ssFolder, BasicURL)
	thread2 = pageDown(firstpage, firstpage+(lastpage-firstpage)//4, ssFolder, BasicURL)
	thread3 = pageDown(firstpage+(lastpage-firstpage)//4, firstpage+(lastpage-firstpage)//4*2, ssFolder, BasicURL)
	thread4 = pageDown(firstpage+(lastpage-firstpage)//4*2, firstpage+(lastpage-firstpage)//4*3, ssFolder, BasicURL)
	thread5 = pageDown(firstpage+(lastpage-firstpage)//4*3, lastpage+1, ssFolder, BasicURL)
	thread1.start()
	thread2.start()
	thread3.start()
	thread4.start()
	thread5.start()
	thread1.join()
	thread2.join()
	thread3.join()
	thread4.join()
	thread5.join()

	if die == 0:
		shutil.move(ssFolder,'F:\\ss\\done\\'+bookname+'_'+ssid+'\\')
	else:
		print(bookname+ssid+' has '+die+' pages incomplete')


wd = Tk() # 總窗口
rows = 10 # 開 10 行

# 獲取剪貼板
def getClip():
	w.OpenClipboard()
	ty=w.GetClipboardData(win32con.CF_TEXT).decode(encoding="UTF-8")
	w.CloseClipboard()
	return ty

# 每一條的框架
class pair(object):
# 文本框
	def __init__(self,r):
		self.r = r
		self.ent = Entry(wd,width=50)
		self.ent.grid(row=self.r,column=0)
# 刪舊加新
	def newText(self):
		self.ent.delete(0,END)
		self.ent.insert(0,getClip())
# 按鈕及行爲
	def fra(self):
		but = Button(wd,text='Paste',command=(lambda:self.newText()))
		but.grid(row=self.r,column=1)

# 根據框架生成 rows 條
# 命令形如 p1 = pair(1) 和 p1.fra()
for i in range(1,rows+1):
	exec('p' + str(i) + '=pair(' + str(i) + ')')
	exec('p' + str(i) + '.fra()')

# 一串形如 p1.ent.get() 的命令
def dl():
	for i in range(1,rows+1):
		exec('getBook(p' + str(i) + '.ent.get())')

# 最終按鈕
dlB = Button(wd,text='Start Downloading',command=(lambda:dl()))
dlB.grid(row=rows+1,column=0)

wd.mainloop()