# ZURL (Zabbix URL)
open winbox on the zabbix map

simple python code for open winbox,ssh,vnc,rdp on the map.

**Manual:**
1. copy folder "tools" dir -> C:\tools

2. Zabbix server add "zurl" valid_uri
edit defines.inc.php 
nano /usr/share/zabbix/include/defines.inc.php
Ctrl+W - find: ZBX_URI_VALID_SCHEMES - add zurl - Save and Exit

3. Run zurl.reg 

4. Zabbix->map->host - add URLS format
zurl://**x** ipaddress login password

>Where **x**
>>w - winbox.exe;

>>rdp - mstsc;

>>vnc - vncviewer.exe;

>>ssh - putty.exe;


I used pyinstaller to create exe file. Windows Defender doesn't trust me. You can convert exe to py yourself or add it to an exception in windows defender
