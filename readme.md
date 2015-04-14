## General
1. 懶得每次敲那麼多字，所以用短文件名。
2. 測試都是實際下載中發生的，很多 bug 沒測到一點都不奇怪。
3. Environment: Python 3.4, Chrome + TamperMonkey.

## a.py
1. 用於補版權。
2. 塡 md 和 readDetail 卽用。當然也可以把 md 部分註釋起來，單用 VPN 。
3. 當 md 支持時，亦可用於長春、大連等。
4. 自動根據 DX 生成標準文件夾，下載時文件夾放在 F:\\ss\\ ，完成後移入 F:\\ss\\leg\\ 。
5. 結合 bat 卽爲批量。
6. 需要 PycURL 。

## v.py
1. 用於補版權。
2. 可用於長春、大連等， VPN 下亦支持 DX 。
3. 自動根據 DX 生成標準文件夾，下載時文件夾放在 F:\\ss\\ ，完成後移入 F:\\ss\\leg\\ 。
4. 結合 bat 卽爲批量。

## c.py
1. 用於下載 CADAL 。
2. CADAL 原因，不是每本書都能下載。
3. 自動在 F:\\cadal\\ 生成八位數文件夾。
4. 文件名自動改成僞 pdg 形式。
5. 要用目錄還要結合 DjVuToy 1.23 。
6. 沒與 bat 相接是因爲 CADAL 用得很少，畢竟不如 CX 淸晰。

## gz1.py
1. Function: downloading GZU ZJK books with multithreads.
2. GZU VPN is required.
3. Standard folders will be generated in F:\\ss\\, and move to F:\\ss\\done\\ if downloads are completed without error.

## gz2.py
1. 用於下載 GZU ZJK 。
2. 需要 Unicode 版 uGet 。
3. 需要 GZU VPN 帳號。
4. 自動生成標準文件夾。
5. 可以結合 bat 來批量。
6. 廢 link 很多，要在 uGet 手動刪除。
7. 當前默認嘗試前言和目錄到 30 頁。對於辭書通常不夠，要手動改。

## gz3.py
1. Download functions come from gz1.py.
2. Add GUI for the script.

## hl.py
1. 用於尋找 ECUST 號。
2. 衹是個最簡單的示範腳本，體現了 Requests 模塊在相關領域的優越性。

## DX2All.user.js
1. Show ssid and links to BK index, NB ZJK, ZG ZJK, JN ZJK, GZU ZJK in bookDetail pages.
2. Cookie and VPN/EZ are required.

## Se2All.user.js
1. Show ssid and links to BK index, NB ZJK, ZG ZJK, JN ZJK, GZU ZJK in search pages.
2. Cookie and VPN/EZ are required.

## GoodNB.user.js
Function: rectify NB ZJK response links.

## GoodGZ.user.js
Function: rectify GZU ZJK response links for gz1.py.

## GoodZG.user.js
Function: rectify ZG ZJK response links.