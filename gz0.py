# -*- coding: gb18030 -*-
import pycurl,os,shutil,getopt,sys

#�������d����ԇ png ����ԇ jpg ���������������ļ��r���� True �Ա�����ѭ�h��
def pDown(cLink, cPath):
	f = open(cPath, 'wb');
	c = pycurl.Curl();
	c.setopt(pycurl.PROXY, "http://127.0.0.1:8002");
	c.setopt(pycurl.URL, cLink+".png");
	c.setopt(c.WRITEFUNCTION, f.write);
	c.perform();
	if c.getinfo(pycurl.HTTP_CODE) == 200:
		f.close();
		return False
	else:
		f = open(cPath, 'wb');
		c.setopt(pycurl.URL, cLink+".jpg");
		c.setopt(c.WRITEFUNCTION, f.write);
		c.perform();
		if c.getinfo(pycurl.HTTP_CODE) == 200:
			f.close();
			return False
		else:
			f.close();
			os.remove(cPath)
			return True

def AttDown(Atts, ssFolder, BasicURL):
	FileExist=os.path.isfile(ssFolder+Atts+".pdg")
	if FileExist == False:
		pDown(BasicURL+Atts,ssFolder+Atts+".pdg")

def getBook(gzBook):
	#ጷ�׃��
	BasicURL=gzBook[0]
	firstpage=int(gzBook[1])
	lastpage=int(gzBook[2])
	ssno=gzBook[3]
	bookname=gzBook[4]

	#�ļ��A
	ssFolder="F:\\ss\\"+bookname+"_"+ssno+"\\"
	FolderExist=os.path.isdir(ssFolder)
	if FolderExist == False:
		os.mkdir(r'f:/ss/'+bookname+'_'+ssno+'/')

	#����bookinfo
	BookinfoExist=os.path.isfile(ssFolder+"Bookinfo.dat")
	if BookinfoExist == False:
		Bookinfo=open(ssFolder+"Bookinfo.dat", "w+")
		Bookinfo.write("[General Information]"+"\n")
		Bookinfo.write("����="+bookname+"\n")
		Bookinfo.write("����="+"\n")
		Bookinfo.write("ҳ��="+str(lastpage)+"\n")
		Bookinfo.write("SS��="+ssno+"\n")
		Bookinfo.write("DX��="+"\n")
		Bookinfo.write("��������="+"\n")
		Bookinfo.write("������="+"\n")
		Bookinfo.write(BasicURL+"\n")
		Bookinfo.close()

	#����������
	AttDown("cov001", ssFolder, BasicURL)
	AttDown("cov002", ssFolder, BasicURL)
	AttDown("bok001", ssFolder, BasicURL)
#	AttDown("bok002", ssFolder, BasicURL)
	AttDown("leg001", ssFolder, BasicURL)

	#Ŀ�
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

	#ǰ��
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

	#����
	for num in range(firstpage, lastpage+1):
		pgNum=str(num).zfill(6)
		ssFile=ssFolder+pgNum+".pdg"
		FileExist=os.path.isfile(ssFile)
		if FileExist == True:
			FileSize=os.path.getsize(ssFile)
			if FileSize == 0:
				pDown(BasicURL+pgNum, ssFile)
				if num == lastpage:
					print(bookname+ssno)
			if FileSize == 1163:
				os.remove(ssFile)
				pDown(BasicURL+pgNum, ssFile)
				if num == lastpage:
					shutil.move(ssFolder,"F:\\ss\\done\\"+bookname+"_"+ssno+"\\")
					print(bookname+ssno)
			else:
				if num == lastpage:
					shutil.move(ssFolder,"F:\\ss\\done\\"+bookname+"_"+ssno+"\\")
					print(bookname+ssno)
		else:
			pDown(BasicURL+pgNum, ssFile)
			if num == lastpage:
				shutil.move(ssFolder,"F:\\ss\\done\\"+bookname+"_"+ssno+"\\")
				print(bookname+ssno)

#�cbat����
def main():
	getBook(sys.argv[1:])

if __name__ == "__main__":
	main()