# ZURL (Zabbix URL)
open winbox on the zabbix map

simple python code for open winbox,ssh,vnc,rdp on the map.

**Manual:**
1. Install dir -> C:\zurl

2. Run  C:\zurl\zurl.reg 

3. Zabbix server add "zurl" valid_uri
edit defines.inc.php 
nano /usr/share/zabbix/include/defines.inc.php
Ctrl+W - find: ZBX_URI_VALID_SCHEMES - add zurl - Save and Exit


4. Zabbix -> map -> host - add URLS format
zurl://**x** ipaddress login password

>Where **x**
>>w - winbox.exe;

>>rdp - mstsc;

>>vnc - vncviewer.exe;

>>ssh - putty.exe;

**example:** zurl://w 192.168.88.1 admin 12345 (open winbox 192.168.88.1 username:admin password:12345)


I used pyinstaller to create exe file. Windows Defender doesn't trust me. You can convert exe to py yourself or add it to an exception in windows defender
