# -*- coding: utf-8 -*-
import os,sys,codecs

#生成多少個 fow 和 ! 好呢？
fowtry=30

def getBook(gzBook):
#釋放變量
	BasicURL=gzBook[0]
	firstpage=int(gzBook[1])
	lastpage=int(gzBook[2])
	ssno=gzBook[3]
	bookname=gzBook[4]

#文件夾
	ssFolder="F:\\ss\\"+bookname+"_"+ssno+"\\"
	FolderExist=os.path.isdir(ssFolder)
	if FolderExist == False:
		os.mkdir(r'f:/ss/'+bookname+'_'+ssno+'/')

#生成bookinfo
	BookinfoExist=os.path.isfile(ssFolder+"Bookinfo.dat")
	if BookinfoExist == False:
		Bookinfo=open(ssFolder+"Bookinfo.dat", "w+")
		Bookinfo.write("[General Information]"+"\n\r")
		Bookinfo.write("书名="+bookname+"\n\r")
		Bookinfo.write("作者="+"\n\r")
		Bookinfo.write("页数="+str(lastpage)+"\n\r")
		Bookinfo.write("SS号="+ssno+"\n\r")
		Bookinfo.write("DX号="+"\n\r")
		Bookinfo.write("出版日期="+"\n\r")
		Bookinfo.write("出版社="+"\n\r")
		Bookinfo.write(BasicURL+"\n\r")
		Bookinfo.close()

#創建bat
	batExist=os.path.isfile('add.bat')
	if batExist == True:
		os.remove('add.bat')
		addbat=codecs.open('add.bat', 'wb', 'utf-8_sig')
	else:
		addbat=codecs.open('add.bat', 'wb', 'utf-8_sig')

#封面書名版權
	addbat.write('uget --folder="'+'F:\\ss\\'+bookname+'_'+ssno+'" --filename=bok001.pdg --proxy-type=1 --proxy-host=127.0.0.1 --proxy-port=8002 '+BasicURL+'bok001.png\n\r')
	addbat.write('uget --folder="'+'F:\\ss\\'+bookname+'_'+ssno+'" --filename=leg001.pdg --proxy-type=1 --proxy-host=127.0.0.1 --proxy-port=8002 '+BasicURL+'leg001.png\n\r')
	addbat.write('uget --folder="'+'F:\\ss\\'+bookname+'_'+ssno+'" --filename=cov001.pdg --proxy-type=1 --proxy-host=127.0.0.1 --proxy-port=8002 '+BasicURL+'cov001.jpg\n\r')
	addbat.write('uget --folder="'+'F:\\ss\\'+bookname+'_'+ssno+'" --filename=cov002.pdg --proxy-type=1 --proxy-host=127.0.0.1 --proxy-port=8002 '+BasicURL+'cov002.jpg\n\r')
	addbat.write('uget --folder="'+'F:\\ss\\'+bookname+'_'+ssno+'" --filename=bok001.pdg --proxy-type=1 --proxy-host=127.0.0.1 --proxy-port=8002 '+BasicURL+'bok001.jpg\n\r')
	addbat.write('uget --folder="'+'F:\\ss\\'+bookname+'_'+ssno+'" --filename=leg001.pdg --proxy-type=1 --proxy-host=127.0.0.1 --proxy-port=8002 '+BasicURL+'leg001.jpg\n\r')

#正文
	for num in range(firstpage,lastpage+1):
		pNum=str(num).zfill(6)
		addbat.write('uget --folder="'+'F:\\ss\\'+bookname+'_'+ssno+'" --filename='+pNum+'.pdg --proxy-type=1 --proxy-host=127.0.0.1 --proxy-port=8002 '+BasicURL+pNum+'.png\n\r')
	for num in range(firstpage,lastpage+1):
		pNum=str(num).zfill(6)
		addbat.write('uget --folder="'+'F:\\ss\\'+bookname+'_'+ssno+'" --filename='+pNum+'.pdg --proxy-type=1 --proxy-host=127.0.0.1 --proxy-port=8002 '+BasicURL+pNum+'.jpg\n\r')

#目錄前言
	for num in range(1, fowtry+1):
		iNum=str(num).zfill(5)
		fNum=str(num).zfill(3)
		addbat.write('uget --folder="'+'F:\\ss\\'+bookname+'_'+ssno+'" --filename=!'+iNum+'.pdg --proxy-type=1 --proxy-host=127.0.0.1 --proxy-port=8002 '+BasicURL+'!'+iNum+'.png\n\r')
		addbat.write('uget --folder="'+'F:\\ss\\'+bookname+'_'+ssno+'" --filename=fow'+fNum+'.pdg --proxy-type=1 --proxy-host=127.0.0.1 --proxy-port=8002 '+BasicURL+'fow'+fNum+'.png\n\r')
	for num in range(1, fowtry+1):
		iNum=str(num).zfill(5)
		fNum=str(num).zfill(3)
		addbat.write('uget --folder="'+'F:\\ss\\'+bookname+'_'+ssno+'" --filename=!'+iNum+'.pdg --proxy-type=1 --proxy-host=127.0.0.1 --proxy-port=8002 '+BasicURL+'!'+iNum+'.jpg\n\r')
		addbat.write('uget --folder="'+'F:\\ss\\'+bookname+'_'+ssno+'" --filename=fow'+fNum+'.pdg --proxy-type=1 --proxy-host=127.0.0.1 --proxy-port=8002 '+BasicURL+'fow'+fNum+'.jpg\n\r')

	os.system("add.bat")

#與bat對接
def main():
	getBook(sys.argv[1:])

if __name__ == "__main__":
	main()