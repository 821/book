import os, pycurl, re, sys, shutil

md=":"
login=":"
def dxDown(url, fullpath):
	c=pycurl.Curl() # 縮寫一下
	c.setopt(c.FOLLOWLOCATION, True) # 允許重定向
	c.setopt(pycurl.USERAGENT, b"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)") # 模擬瀏覽器
	c.setopt(pycurl.URL, url) # 訪問指定網址
	c.setopt(pycurl.COOKIEJAR, 'cookie.txt') # 把 cookie 存到文件
	c.setopt(pycurl.COOKIEFILE, "cookie.txt") # 用文件掛 cookie
	f = open(fullpath, 'wb') # 定義一個文件
	c.setopt(c.WRITEDATA, f) # 指定返回信息的寫入文件，或作 c.setopt(c.WRITEFUNCTION, f.write)
	c.perform() # 獲得服務器返回信息
	f.close()
	if c.getinfo(pycurl.HTTP_CODE) != 200:
		os.remove(fullpath)
		print("Failed!")

def getAtt(DXurl,md,login):
	g = open("temp.txt", 'wb')
	d=pycurl.Curl()
	d.setopt(d.FOLLOWLOCATION, True)
	d.setopt(pycurl.PROXY, md) # 掛代理
	d.setopt(pycurl.PROXYUSERPWD, login) # 代理的用戶名密碼
	d.setopt(pycurl.USERAGENT, b"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)")
	d.setopt(pycurl.URL, DXurl)
	d.setopt(pycurl.COOKIEJAR, 'dxcookie.txt')
	d.setopt(pycurl.COOKIEFILE, "dxcookie.txt")
	d.setopt(d.WRITEFUNCTION, g.write)
	d.perform()
	d.close()
	g.close()
	data=open("temp.txt","rU",encoding='UTF-8').read()
	jpgPath=re.compile(r'(?<=jpgPath:")[0-9a-zA-Z\/]+(?=")')
	strf=jpgPath.search(str(data)).group()
	title=re.compile(u'(?<=<title>)[^<]+(?=</title>)')
	bookname=title.search(str(data)).group()
	ss=re.compile(r'(?<=ssid:.)\d{8}')
	ssid=ss.search(str(data)).group()
	legurl="http://img.duxiu.com"+strf+"leg001?zoom=2"
	ssFolder="F:\\ss\\"+bookname+"_"+ssid+"\\"
	FolderExist=os.path.isdir(ssFolder)
	if FolderExist == False:
		os.mkdir(r'f:/ss/'+bookname+'_'+ssid+'/')
	legpath=ssFolder+"leg001.pdg"
	dxDown(legurl,legpath)
	shutil.move(ssFolder,"F:\\ss\\leg\\"+bookname+"_"+ssid+"\\")
	os.remove("temp.txt")
	os.remove("cookie.txt")
	os.remove("dxcookie.txt")

def main():
	getAtt(sys.argv[1],md,login)
if __name__ == "__main__":
	main()