# -*- coding: utf-8 -*-
import requests,os,shutil,sys

proxy = {'http':'http://127.0.0.1:8002'}

#代理下載，先試 png ，再試 jpg ，服務器不存在文件時返回 True 以便跳出循環。
def pDown(cLink, cPath):
	r = requests.get(cLink+".png", proxies=proxy, stream=True)
	if r.status_code == 200:
		with open(cPath, 'wb') as fd:
			for chunk in r.iter_content(chunk_size=1024):
				fd.write(chunk)
	else:
		r = requests.get(cLink+".jpg", proxies=proxy, stream=True)
		if r.status_code == 200:
			with open(cPath, 'wb') as fd:
				for chunk in r.iter_content(chunk_size=1024):
					fd.write(chunk)
		else:
			return True

def AttDown(Atts, ssFolder, BasicURL):
	FileExist=os.path.isfile(ssFolder+Atts+".pdg")
	if FileExist == False:
		pDown(BasicURL+Atts,ssFolder+Atts+".pdg")

def getBook(gzBook):
	#釋放變量
	BasicURL=gzBook[0]
	firstpage=int(gzBook[1])
	lastpage=int(gzBook[2])
	ssid=gzBook[3]
	bookname=gzBook[4]

	#文件夾
	ssFolder="F:\\ss\\"+bookname+"_"+ssid+"\\"
	FolderExist=os.path.isdir(ssFolder)
	if FolderExist == False:
		os.mkdir(r'f:/ss/'+bookname+'_'+ssid+'/')

	#生成bookinfo
	BookinfoExist=os.path.isfile(ssFolder+"Bookinfo.dat")
	if BookinfoExist == False:
		Bookinfo=open(ssFolder+"Bookinfo.dat", "w+")
		Bookinfo.write("[General Information]"+"\n")
		Bookinfo.write("书名="+bookname+"\n")
		Bookinfo.write("作者="+"\n")
		Bookinfo.write("页数="+str(lastpage)+"\n")
		Bookinfo.write("SS号="+ssid+"\n")
		Bookinfo.write("DX号="+"\n")
		Bookinfo.write("出版日期="+"\n")
		Bookinfo.write("出版社="+"\n")
		Bookinfo.write(BasicURL+"\n")
		Bookinfo.close()

	#封面書名版權
	AttDown("cov001", ssFolder, BasicURL)
	AttDown("cov002", ssFolder, BasicURL)
	AttDown("bok001", ssFolder, BasicURL)
#	AttDown("bok002", ssFolder, BasicURL)
	AttDown("leg001", ssFolder, BasicURL)

	#目錄
	for num in range(1, 1000):
		pgNum=str(num).zfill(5)
		ssFile=ssFolder+"!"+pgNum+".pdg"
		FileExist=os.path.isfile(ssFile)
		if FileExist == True:
			FileSize=os.path.getsize(ssFile)
			if FileSize == 0:
				if pDown(BasicURL+"!"+pgNum, ssFile):
					break
		else:
			if pDown(BasicURL+"!"+pgNum, ssFile):
				break

	#前言
	for num in range(1, 1000):
		pgNum=str(num).zfill(3)
		ssFile=ssFolder+"fow"+pgNum+".pdg"
		FileExist=os.path.isfile(ssFile)
		if FileExist == True:
			FileSize=os.path.getsize(ssFile)
			if FileSize == 0:
				if pDown(BasicURL+"fow"+pgNum, ssFile):
					break
		else:
			if pDown(BasicURL+"fow"+pgNum, ssFile):
				break

	#正文
	for num in range(firstpage, lastpage+1):
		pgNum=str(num).zfill(6)
		ssFile=ssFolder+pgNum+".pdg"
		FileExist=os.path.isfile(ssFile)
		if FileExist == True:
			FileSize=os.path.getsize(ssFile)
			if FileSize == 0:
				pDown(BasicURL+pgNum, ssFile)
				if num == lastpage:
					shutil.move(ssFolder,"F:\\ss\\done\\"+bookname+"_"+ssid+"\\")
					print(bookname+ssid)
			else:
				if num == lastpage:
					shutil.move(ssFolder,"F:\\ss\\done\\"+bookname+"_"+ssid+"\\")
					print(bookname+ssid)
		else:
			pDown(BasicURL+pgNum, ssFile)
			if num == lastpage:
				shutil.move(ssFolder,"F:\\ss\\done\\"+bookname+"_"+ssid+"\\")
				print(bookname+ssid)

#與bat對接
def main():
	getBook(sys.argv[1:])

if __name__ == "__main__":
	main()