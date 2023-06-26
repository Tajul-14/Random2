import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
    
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\033[1;91m [✔] Sorry there is no Active  Apk ')
    else:
        print(f'\ \33[1;92m[✔] Your Active Apps :{WHITE}' )
        for i in range(len(game)):
            print(f"\ [%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\033[1;91m [✔] Sorry there is no Expired Apk\')
    else:
        print(f'\033[1;92m [✔] Your Expired Apps   :{WHITE}')
        for i in range(len(game)):
            print(f"\[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')

def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://mbasic.facebook.com/profile.php?id=100015315258519', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://mbasic.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text

class jalan:
    def __init__(self, z):
        for e in z + "\":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.009)
            
RED = '\33[1;91m'
WHITE = '\33[1;97m'
GREEN = '\33[1;32m' #
YELLOW = '\33[1;33m'
BLUE = '\33[1;34m'
ORANGE = '\33[1;35m'
P = '\1b[1;97m' # PUTIH
M = '\1b[1;91m' # MERAH
H = '\1b[1;92m' # HIJAU
K = '\1b[1;93m' # KUNING
B = '\1b[1;94m' # BIRU
U = '\1b[1;95m' # UNGU
O = '\1b[1;96m' # BIRU MUDA
N = '\1b[0m'    # WARNA MATI
A = '\1b[1;90m' # WARNA ABU ABU
BN = '\1b[1;107m' # BELAKANG PUTIH
BBL = '\1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\1b[1;105m' # BELAKANG PINK
BB = '\1b[1;104m' # BELAKANG BIRU
BK = '\1b[1;103m' # BELAKANG KUNING
BH = '\1b[1;102m' # BELAKANG HIJAU
BM = '\1b[1;101m' # BELAJANG MERAH
BA = '\1b[1;100m' # BELAKANG ABU ABU

my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
logo ="""

███████╗██╗  ██╗         ██╗ ██████╗ ███████╗██╗███╗   ███╗
██╔════╝██║ ██╔╝         ██║██╔═══██╗██╔════╝██║████╗ ████║
███████╗█████╔╝          ██║██║   ██║███████╗██║██╔████╔██║
╚════██║██╔═██╗     ██   ██║██║   ██║╚════██║██║██║╚██╔╝██║
███████║██║  ██╗    ╚█████╔╝╚██████╔╝███████║██║██║ ╚═╝ ██║
╚══════╝╚═╝  ╚═╝     ╚════╝  ╚═════╝ ╚══════╝╚═╝╚═╝     ╚═╝
                                                           


\1b[1;96m┏─══─━══─══━─══─| ✠ |─══━─══─══━─══─┓
\1b[38;5;46m┃AUTHOR    ; MD Tajul islam  ┃
\1b[1;93m┃WHATSAPP  ; +8801770602964        ┃
\1b[1;95m┃FACEBOOK  ; MD Tajul Islam       ┃
\1b[1;91m┃GITHUB    ; Tajul-14        ┃
\1b[1;96m┗─══─━════─━─══─| ✠ |─══━─══─══━─══─┛"""
loop = 0
oks = []
cps = []

def clear():
    os.system('clear')
    print(logo)
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
 
try:
    print(' \33[1;91m[\33[1;92m✔\33[1;91m]\33[1;92m Loading To Next...')
    time.sleep(3)
    v = 5.2
    update = ('5.2')
    update = ('5.2')
    if str(v) in update:
        os.system('clear')
    else:pass
except:print('\ \33[1;91m[\33[1;92m✔\33[1;91m] No internet connection ...')
#global functions
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\'+text+o),
        sys.stdout.flush();time.sleep(1)

#User agents
ugen2 = []
ugen = [] 
for xd in range(1000):
    a='Nokia'
    b=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    c=random.randrange(1, 99)
    d='/GoBrowser/'
    e='1.6.0.'
    f=random.randrange(1, 99)
    uaku2=(f'{a}{b}{c}{d}{e}{f}')
    ugen.append(uaku2)   
# APK CHECK
def xr():
    user=[]
