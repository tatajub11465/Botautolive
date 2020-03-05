import sys, os, shlex, subprocess
import random
import string
import threading
import time
from queue import Queue
import platform

import requests
from colorama import Fore, init

os.system('clear')

intro = """  ▒▄█▀▀█░▐█▀█▒▐█▒▐▀
  ▒▀▀█▄▄░▐█──▒▐██▌░
  ▒█▄▄█▀░▐█▄█▒▐█▒▐▄
"""
text = "\n {}YouTube : Scriptking SCK \n {}กดใลค์ กดติดตาม ให้กำลังใจด้วยน่า\n {}BOT V.2"
print(intro)
print(text)
if platform.system() == "Windows": #checking OS
    clear = "cls"
else:
    clear = "clear"

token = input("\n\033[01;33m\033[01;32m[BOTAUTOLIVE]\033[01;33m\033[01;34m└╼\033[01;36m 🆔 > : ")
url= "https://m.youtube.com/watch?v=" + token
url2 = "https://s.youtube.com/api/stats/watchtime?ns=yt&el=detailpage&cpn=AiWtf2fjIwVS2MeQ&docid=" + token + "&ver=2&cmt=7926.045&ei=igGSXce3IM2NgAfasp-ABg&fmt=133&fs=0&rt=1096.007&of=L_224b5BokWsQ5UWgAws_w&euri&lact=2837&live=dvr&cl=271684942&state=playing&vm=CAEQABgEKhhJc0gwZ2w0QmFfbTBWSXlWNm9ITmRRPT0&volume=100&c=MWEB&cver=2.20190928.07.00&cplayer=UNIPLAYER&cbrand=apple&cbr=Safari%20Mobile&cbrver=12.1.15E148&cmodel=iphone&cos=iPhone&cosver=12_2&cplatform%20=MOBILE&delay=5&hl=ru_RU&cr=DE&rtn=1396&afmt=140&lio=1556394045.182&idpj=&ldpj=&rti=1096&muted=0&st=7626.045&et=7926.045 "
class main(object):
    def __init__(self):
        self.combolist = Queue()
        self.Writeing = Queue()
        self.printing = []
        self.botted = 0
        self.combolen = self.combolist.qsize()

    def printservice(self): #print screen
        while True:
            if True:
                os.system(clear)
                print(Fore.LIGHTCYAN_EX + intro + Fore.LIGHTMAGENTA_EX)
                print(
                    Fore.LIGHTCYAN_EX + f"บอททำงานไปทั้งหมด:{self.botted}\n")
                for i in range(len(self.printing) - 10, len(self.printing)):
                    try:
                        print(self.printing[i])
                    except (ValueError, Exception):
                        pass
                time.sleep(0.5)
a = main()
class proxy():

    def update(self):
        while True:
            url = "http://sck-shop.cf/New/proxy+2020.txt"
            r = requests.get(url)

            self.splited = r.text.split("\r\n") #scraping and splitting proxies
            time.sleep(600)
    
    def get_proxy(self):
        random1 = random.choice(self.splited) #choose a random proxie
        return random1
    def FormatProxy(self):
	    proxyOutput = {'https':self.get_proxy()}
	    return proxyOutput

    def __init__(self):
        self.splited = []
        threading.Thread(target=self.update).start()
        time.sleep(3)

proxy1 = proxy()
def bot():
    while True:

        


        headers={
        "Host": "m.youtube.com",
        "Accept-Encoding": "gzip, deflategzip, deflate, brgzip, deflate, br",
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Language": "th-TH,th;q=0.9,en;q=0.8",
        "Connection": "close"
        }

        try:
            s = requests.session()
            s.get(url,headers=headers,proxies=proxy1.FormatProxy()) #stream request
            s.get(url2,headers=headers,proxies=proxy1.FormatProxy()) #api request

            a.botted += 1
        except:
            pass

time.sleep(7)
maxthreads = int(input("\n\033[01;33m\033[01;32m[ใส่เทรด 500-1000]\033[01;33m\033[01;34m└╼\033[01;36m >>ใส่Portที่ต้องการ:"))

threading.Thread(target=a.printservice).start()
num = 0
while num < maxthreads :
    num += 1
    threading.Thread(target=bot).start()


threading.Thread(target=bot).start()
