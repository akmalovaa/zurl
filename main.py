import sys
import subprocess

uri = (sys.argv[1].replace("zurl:", "")).replace("/", "")
zargs = uri.split('%20')

try:
    ipaddr = zargs[1]
except:
    ipaddr = '127.0.0.1'
    print('NO IP ADDRESS')
    print('Pls read manual Akmalov.com')
    input('Press any key to exit')
    sys.exit()


try:
    login = zargs[2]
except:
    login = 'admin'

try:
    password = zargs[3]
except:
    password = ''


def zurl (args):
    if args == 'w':
        subprocess.run(['winbox.exe', ipaddr, login, password])
    if args == 'rdp':
        subprocess.call(f'mstsc /v:{ipaddr}')
    if args == 'ssh':
        subprocess.run(['putty.exe', ipaddr])
    if args == 'vnc':
        subprocess.run(['vncviewer.exe', ipaddr])
    sys.exit()


zurl(zargs[0])
