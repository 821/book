// ==UserScript==
// @name		DX2ZJK
// @version		1.1
// @include		*.com/bookDetail.jsp?dxNumber=*
// @description		從介紹頁跳轉到返回鏈獲取頁
// @copyright		LCZ
// @license		GPLv3
// ==/UserScript==

var version = "1.1";
var date = "2015-3-16";

var getBK = location.href.replace("bookDetail.jsp?dxNumber=", "other.do?go=showmorelib&dxid=")
var ssidfavDiv = document.getElementById("ssidfav");
var ssid = ssidfavDiv.getAttribute("value");
var divAdd = document.createElement("div");
divAdd.innerHTML = ssid+' <a href="' + getBK + '" rel="external">BK</a> <a href="http://cxbook.nlic.net.cn:8089/getbookread?BID='+ssid+'" target="_blank">NB</a>' + ' ' + '<a href="http://202.116.13.19:8080/GW/s/202.116.13.47/G.http-8088/getbookread?BID='+ssid+'" target="_blank">JN</a>' + ' ' + '<a href="http://210.40.8.52:4599/getbookread?BID='+ssid+'" target="_blank">GZ</a>';
var grade1Div = document.getElementById("frameshow");
var grade1Parent = grade1Div.parentNode;
grade1Parent.insertBefore(divAdd, grade1Div);