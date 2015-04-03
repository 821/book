// ==UserScript==
// @name		DX2All
// @version		1.2
// @include		*.com/bookDetail.jsp?dxNumber=*
// @description		顯示 ssid ，通向 BK 查詢頁及 NB, ZG, JN, GZU 等 ZJK 返回鏈獲取頁
// @copyright		LCZ
// @license		GPLv3
// ==/UserScript==

var version = "1.2";
var date = "2015-4-4";

var getBK = location.href.replace("bookDetail.jsp?dxNumber=", "other.do?go=showmorelib&dxid=")
var ssidfavDiv = document.getElementById("ssidfav");
var ssid = ssidfavDiv.getAttribute("value");
var divAdd = document.createElement("div");
divAdd.innerHTML = ssid+' <a href="' + getBK + '&type=1">BK</a> <a href="http://cxbook.nlic.net.cn:8089/getbookread?BID='+ssid+'" target="_blank">NB</a> <a href="http://210.32.205.38:8088/getbookread?BID='+ssid+'" target="_blank">ZG</a>' + ' ' + '<a href="http://202.116.13.19:8080/GW/s/202.116.13.47/G.http-8088/getbookread?BID='+ssid+'" target="_blank">JN</a>' + ' ' + '<a href="http://210.40.8.52:4599/getbookread?BID='+ssid+'" target="_blank">GZ</a>';
var grade1Div = document.getElementById("frameshow");
var grade1Parent = grade1Div.parentNode;
grade1Parent.insertBefore(divAdd, grade1Div);