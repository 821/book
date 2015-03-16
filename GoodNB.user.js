// ==UserScript==
// @name		GoodNB
// @version		1.1
// @include		http://cxbook.nlic.net.cn:8089/getbookread?BID=*
// @description	修整 NB ZJK 返回鏈
// @copyright		LCZ
// @license		GPLv3
// ==/UserScript==

var version = "1.1";
var date = "2015-03-16";

var getLink = document.getElementsByTagName('body')[0].innerHTML.toString();
if (/book/.test(getLink)) {
	var decodeLink = decodeURIComponent(unescape(getLink));
	var goodLink = decodeLink.replace(/rd=\d+/, "rd=95AA94A1A19D60A09E9B9560A097A66095A07017837839846632").replace(/sdwen.+BID=/,"ssnum=").replace(/\&ReadMode.+/, "");
	document.write(goodLink);
}
else return;