import requests
from colorama import Fore

url = ['https://www.rk-ny.org/whatsnew.php?id=1', 'https://www.genecards.org/cgi-bin/carddisp.pl?gene=ID1', \
       'http://www.meggieschneider.com/php/detail.php?id=1', 'https://kodamo.org/product.php?id=1']

for i in url:
    res = requests.get(i+"'", allow_redirects=False)
    if res.status_code == 200:
        print(i+"'",   Fore.GREEN, '==> Vulnerable!', Fore.RESET,)
    else:
        print(i+"'",   Fore.RED, '==> Not vulnerable!', Fore.RESET,)