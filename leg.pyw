import clipboard,requests,re,os,shutil
from tkinter import *

def download():
	url = clipboard.paste()
	r = requests.get(url)
	data = r.text
	jpgPath = re.compile(r'(?<=jpgPath:")[0-9a-zA-Z\/]+(?=")')
	strf = jpgPath.search(str(data)).group()
	title = re.compile(u'(?<=<title>)[^<]+(?=</title>)')
	bookname = title.search(str(data)).group()
	ss = re.compile(r'(?<=ssid:.)\d{8}')
	ssid = ss.search(str(data)).group()
	legurl="http://img.duxiu.com" + strf+"leg001?zoom=2"
	legreq = requests.get(legurl, stream=True)
	if legreq.status_code == 200:
		ssFolder="F:/ss/" + bookname + "_" + ssid + "/"
		FolderExist=os.path.isdir(ssFolder)
		if FolderExist == False:
			os.mkdir(r'F:/ss/' + bookname + '_' + ssid + '/')
		legpath=ssFolder + "leg001.pdg"
		with open(legpath, 'wb') as pdg:
			for chunk in legreq.iter_content(chunk_size=1024):
				pdg.write(chunk)
		shutil.move(ssFolder,"F:/ss/leg/" + bookname + "_" + ssid + "/")
		ent.delete(0,END)
		ent.insert(0, 'Finish')
	else:
		ent.delete(0,END)
		ent.insert(0, 'No leg')

wd = Tk()
wd.title('版權頁')
but = Button(wd,text='Download',command=download)
but.grid(row=0,column=0)
ent = Entry(wd,width=20)
ent.grid(row=1,column=0)
wd.update()
wd.mainloop()
