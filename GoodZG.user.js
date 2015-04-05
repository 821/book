// ==UserScript==
// @name           GoodZG
// @namespace      821.github.io
// @version        1.0
// @include        http://210.32.205.38:8088/getbookread?BID=*
// @description    修整自建庫返回鏈
// @license        GPLv3; http://www.gnu.org/copyleft/gpl.html
// ==/UserScript==

var version = "1.0";
var date = "2015-04-05";

var getlink = document.getElementsByTagName('body')[0].innerHTML.toString();
if (/book/.test(getlink)) {
	var decodelink = decodeURIComponent(unescape(getlink));
	document.write(decodelink);
}
else return;