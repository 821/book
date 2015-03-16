// ==UserScript==
// @name		GoodGZ
// @version		1.1
// @include		http://210.40.8.52:4599/getbookread?BID=*
// @description		修整自建庫返回鏈
// @copyright		LCZ
// @license		GPLv3
// ==/UserScript==

var version = "1.1";
var date = "2015-03-17";

var getLink = document.getElementsByTagName('body')[0].innerHTML.toString();
if (/book/.test(getLink)) {
	var decodeLink = decodeURIComponent(unescape(getLink));
	var goodLink = decodeLink.replace(/190\.236\.97\.144/, "210.40.8.52:8001");
	var firstpage = parseInt(goodLink.match(/\d{5}\.png/));
	var lastpage = parseInt(goodLink.match(/pages=\d+/)[0].replace(/pages=/, ""));
	var ssid= goodLink.match(/BID=\d{8}/)[0].replace(/BID=/, "");
	var bookname = goodLink.match(/bookname=[^&]+&/)[0].replace(/bookname=/, "").replace(/&/, "");
	var urlpart = goodLink.replace(/.+url=/, "").replace(/.{6}\.png.+/, "");
	document.write('gz1.py "'+urlpart+'" "'+firstpage+'" "'+lastpage+'" "'+ssid+'" "'+bookname+'"');
}