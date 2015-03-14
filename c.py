# -*- coding: utf-8 -*-
import http.client,urllib.request,os,re

# 鏈接要用的變量
UserInput=input("The link or BookNum: ")
FindNum=re.search(r'\d{8}',UserInput) # 原理是找到八位數字
BookNum=FindNum.group(0)
BookNum1=BookNum[:2]
BookNum2=str((int(BookNum[2:5])+1)*1000).zfill(6)
BookType=["book","anc","minguo","minguoqikan","qikan","deg","dunhuang","eng","shufa"]
BookLib=["dlib","dlib1","dlib2","dlib3","dlib4","dlib5","dlib6","newebooks7","newebooks8","newebooks9","newebooks10","newebooks11"]
Path="F:\\cadal\\"+BookNum+"\\" # 存儲用的文件夾

# 鏈接測試函數
def Check(Tested):
	Test=http.client.HTTPConnection("210.32.137.91")
	Test.request("GET", Tested)
	Response=Test.getresponse()
	if Response.status == 200:
		return True
	else:
		return False

#開始找正確鏈接
for Type in BookType:
	for Lib in BookLib:
		URIPart="/"+Lib+"/ebooks/"+Type+"/"+BookNum1+"/"+BookNum2+"/"+BookNum+"/ptiff/"
		URI=URIPart+"00000001.djvu"
		# 測試鏈接是否正確，正確就進入下載階段，不正確就試下一個
		if Check(URI):
			os.makedirs(Path, exist_ok=True) #如果文件夾已存在就不用建立了
			# Catalog.xml 一般都可下，不判斷
			CatURL="http://210.32.137.91"+"/"+Lib+"/ebooks/"+Type+"/"+BookNum1+"/"+BookNum2+"/"+BookNum+"/meta/Catalog.xml"
			DownCat=urllib.request.urlretrieve(CatURL,Path+"Catalog.xml")
			for Page in range(1,99999999):
				ThePage=str(Page).zfill(8)+".djvu" # 包含了一個把數字轉換爲字符串的動作
				FileExist=os.path.isfile(Path+ThePage) # 看看是否已經下載
				# 測試該頁是否存在，如果存在就下載，不存在說明下完了
				if FileExist == False: # 沒下就看是否存在
					if Check(URIPart+ThePage): # 沒下且服務器上有，就下載
						print("Downloading page "+str(Page))
						PageURL="http://210.32.137.91"+URIPart+ThePage
						DownPage=urllib.request.urlretrieve(PageURL,Path+str(Page).zfill(6)+".pdg") # 保存爲 pdg
					else: # 沒下且服務器上沒有在說明下完了
						print("Finish!")
						input() # 用 break 會直接跳出窗口，看不到回饋
				else: # 下過了就跳過
					pass
		else:
			pass
print("Not found!") # 看不見這一句說明沒試完所有鏈接程序就出錯跳出了。
input()