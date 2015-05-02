from tkinter import *
import clipboard,os

rows = 7

wd = Tk()
wd.title('更名器')

class pair(object):
	def __init__(self,r,buttext):
		self.r = r
		self.ent = Entry(wd,width=30)
		self.ent.grid(row=self.r,column=0)
		self.buttext = buttext
	def newText(self):
		self.ent.delete(0,END)
		self.ent.insert(0,clipboard.paste())
	def fra(self):
		but = Button(wd, text=self.buttext,command=self.newText)
		but.grid(row=self.r,column=1)

p1 = pair(1,'路徑')
p1.fra()
p2 = pair(2,'文件')
p2.fra()
p3 = pair(3,'書名')
p3.fra()
p4 = pair(4,'作者')
p4.fra()
p5 = pair(5,'出版')
p5.fra()
p6 = pair(6,'年份')
p6.fra()


def renameit():
	old = p1.ent.get() + '\\' + p2.ent.get() + '.zip'
	new = p1.ent.get() + '\\' + p3.ent.get() + ' ' + p4.ent.get() + ' ' + p5.ent.get() + ' ' + p6.ent.get() + '.zip'

	os.rename(old, new)

but = Button(wd,text='Rename',command=renameit)
but.grid(row=rows+1,column=0)

wd.update()
wd.mainloop()