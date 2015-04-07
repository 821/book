// ==UserScript==
// @name		Se2All
// @version		1.2
// @include		*/search?Field=*
// @include		*/search?sw=*
// @include		*/search?channel=search*
// @description		顯示 ssid ，通向 BK 查詢頁及 NB ZJK, JN ZJK, GZU ZJK 返回鏈獲取頁
// @copyright		LCZ
// @license		GPLv3
// ==/UserScript==

var version = "1.2";
var date = "2015-4-7";

Se2All = {
	run: function() {
		var book1Div = document.getElementsByClassName("book1");
		var scoreDiv = document.getElementsByClassName("grade s1 hide");
		for (var i=0; i<book1Div.length; i++) {
			var ssidInput = document.getElementById("ssid"+i);
			var ssid = ssidInput.getAttribute("value");
			var urlInput = document.getElementById("url"+i);
			var url = urlInput.getAttribute("value");
			var getBK = url.replace("bookDetail.jsp?dxNumber=", "other.do?go=showmorelib&dxid=")
			var divAdd = document.createElement("div");
			divAdd.innerHTML =  ssid+' <a href="' + getBK + '&type=1">BK</a> <a href="http://cxbook.nlic.net.cn:8089/getbookread?BID='+ssid+'" target="_blank">NB</a> <a href="http://210.32.205.38:8088/getbookread?BID='+ssid+'" target="_blank">ZG</a> <a href="http://202.116.13.19:8080/GW/s/202.116.13.47/G.http-8088/getbookread?BID='+ssid+'" target="_blank">JN</a> <a href="http://210.40.8.52:4599/getbookread?BID='+ssid+'" target="_blank">GZ</a>';
			var scoreParent = scoreDiv[i].parentNode;
			scoreParent.insertBefore(divAdd, scoreDiv[i]);
		}
	}
}

try {
	Se2All.run();
}
catch (e) {
}