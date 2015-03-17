# -*- coding: utf-8 -*-
import http.cookiejar,urllib.request,re,os,sys,shutil

def getAtt(url):
	# 允許 cookie
	cookie = http.cookiejar.CookieJar()
	cookieProc = urllib.request.HTTPCookieProcessor(cookie)
	opener = urllib.request.build_opener(cookieProc)
	urllib.request.install_opener(opener)

	# 僞裝 IE ，取回頁面
	header = {'User-Agent':'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)'}
	req = urllib.request.Request(url, headers=header)
	uopen = urllib.request.urlopen(req)
	resp = uopen.read()
	t = open('temp.txt', 'wb')
	t.write(resp)
	t.close()

	# 取得各種變量
	data=open("temp.txt","rU",encoding='UTF-8').read()
	jpgPath=re.compile(r'(?<=jpgPath:")[0-9a-zA-Z\/]+(?=")')
	strf=jpgPath.search(str(data)).group()
	title=re.compile(u'(?<=<title>)[^<]+(?=</title>)')
	bookname=title.search(str(data)).group()
	ss=re.compile(r'(?<=ssid:.)\d{8}')
	ssid=ss.search(str(data)).group()

	# 構造鏈接和文件夾
	legurl="http://img.duxiu.com"+strf+"leg001?zoom=2"
	ssFolder="F:\\ss\\"+bookname+"_"+ssid+"\\"
	FolderExist=os.path.isdir(ssFolder)
	if FolderExist == False:
		os.mkdir(r'f:/ss/'+bookname+'_'+ssid+'/')
	legpath=ssFolder+"leg001.pdg"

	# 下載
	urllib.request.urlretrieve(legurl,legpath)
	os.remove("temp.txt")
	shutil.move(ssFolder,"F:\\ss\\leg\\"+bookname+"_"+ssid+"\\")

def main():
	getAtt(sys.argv[1])
if __name__ == "__main__":
	main()