## General
1. 懶得每次敲那麼多字，所以用短文件名。
2. 測試都是實際下載中發生的，很多 bug 沒測到一點都不奇怪。
3. .py 衹測試最新穩定版 Python （目前爲 3.4 ）， .js 衹測試 Chrome Stable + Tampermonkey 。
4. 本人系統爲 Windows ， 64 bit 。至於是 7 還是 8 則看重裝時的隨機因素。

## a.py
1. 用於補版權。
2. 塡 md 和 readDetail 卽用。當然也可以把 md 部分註釋起來，單用 VPN 。
3. 當 md 支持時，亦可用於長春、大連等。
4. 自動根據 DX 生成標準文件夾，下載時文件夾放在 F:\\ss\\ ，完成後移入 F:\\ss\\leg\\ 。
5. 結合 bat 卽爲批量。
6. 需要 PycURL 。

## c.py
1. 用於下載 CADAL 。
2. CADAL 原因，不是每本書都能下載。
3. 自動在 F:\\cadal\\ 生成八位數文件夾。
4. 文件名自動改成僞 pdg 形式。
5. 要用目錄還要結合 DjVuToy 1.23 。
6. 沒與 bat 相接是因爲 CADAL 用得很少，畢竟不如 CX 淸晰。

## gz0.py
1. 用於下載 GZU ZJK 。
2. 需要 PycURL ——因爲 GZ VPN 的本地代理和 urllib 不兼容。
3. 需要 GZU VPN 帳號。
4. 自動生成標準文件夾，下載時文件夾放在 F:\\ss\\ ，完成後移入 F:\\ss\\done\\ 。
5. 可以結合 bat 來批量。
6. 經常出問題自動跳出，所以比較適合補頁。

## gz1.py
1. 用於下載 GZU ZJK 。
2. 需要 uGet 1.99 以上版本，設好 path 或將腳本放置於 uGet 之 bin 文件夾。此版或以上 uGet 均爲 Unicode 程序，而舊版則需要把所生成之 bat 轉爲 GBK 編碼方可使用。
3. 需要 GZU VPN 帳號。
4. 自動生成標準文件夾。
5. 可以結合 bat 來批量。
6. 廢 link 很多，要在 uGet 手動刪除。
7. 當前默認嘗試前言和目錄到 30 頁。對於辭書通常不夠，要手動改。

## DX2All.user.js
1. 用於在 bookDetail 頁中顯示 ssid ，通向 BK 查詢頁及 NB ZJK, JN ZJK, GZU ZJK 返回鏈獲取頁。
2. 亦可用於長春、大連等，支持 EZ 和 SSLVPN 模式。
3. 沒有登入相應機構 VPN 或 EZ 時，有的獲取頁打不開。
4. 登入 VPN 而沒登入 ZJK 時，有的獲取頁是空白的。

## Se2All.user.js
1. 用於在普通搜索頁中顯示 ssid ，通向 BK 查詢頁及 NB ZJK, JN ZJK, GZU ZJK 返回鏈獲取頁。
2. 亦可用於長春、大連等，支持 EZ 和 SSLVPN 模式。
3. 沒有登入相應機構 VPN 或 EZ 時，有的獲取頁打不開。
4. 登入 VPN 而沒登入 ZJK 時，有的獲取頁是空白的。

## GoodNB.user.js
1. 用於修正 NB ZJK 返回鏈。
2. 需要 NB VPN 。

## GoodGZ.user.js
1. 用於修正 GZU ZJK 返回鏈，以運用於 gz1.py
2. 需要 GZU VPN 。