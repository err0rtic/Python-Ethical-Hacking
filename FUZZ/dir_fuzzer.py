import requests
import sys
import os
import argparse
from multiprocessing import Pool
from colorama import Fore
import re
import time
import base64
import urllib.parse

DOMAIN = ""
DIRS = []
counter = 1

parser = argparse.ArgumentParser(description='Example: \n python3 fuzzer.py -u https://site.com/FUZZ \
-w /home/root/wordlists/directory-list-2.3-medium.txt -e .php -t 10', usage='Script options')
parser.add_argument('-u',  type=str, help='Enter domain  https://site.com')
parser.add_argument('-w',  type=str, help='Name and path of the wordlist')
parser.add_argument('-t',  type=int, default=1,  help='Count Thread')
parser.add_argument('-e',  type=str, default='/', help='Extensions example -e .txt ')
parser.add_argument('-b64', help='FUZZ in base64', action="store_true")
parser.add_argument('-uenc', help='FUZZ in URLENCODE', action="store_true")
parser.add_argument('-head',  type=str, default='!', help='Name and path of the wordlist',)
args = parser.parse_args()


def greetings():
    """The function displays the user's greeting"""
    print(Fore.GREEN, '''
╔═══╗╔══╗╔═══╗     ╔═══╗╔╗─╔╗╔════╗╔════╗╔═══╗╔═══╗
╚╗╔╗║╚╣║╝║╔═╗║     ║╔══╝║║─║║╚══╗═║╚══╗═║║╔══╝║╔═╗║
─║║║║─║║─║╚═╝║     ║╚══╗║║─║║──╔╝╔╝──╔╝╔╝║╚══╗║╚═╝║
─║║║║─║║─║╔╗╔╝     ║╔══╝║║─║║─╔╝╔╝──╔╝╔╝─║╔══╝║╔╗╔╝
╔╝╚╝║╔╣║╗║║║╚╗     ║║───║╚═╝║╔╝═╚═╗╔╝═╚═╗║╚══╗║║║╚╗
╚═══╝╚══╝╚╝╚═╝     ╚╝───╚═══╝╚════╝╚════╝╚═══╝╚╝╚═╝
          ''', Fore.RESET)


def check_wordlist_file(path_to_wordlist):
    """The function checks for the existence of a file with a dictionary"""
    if not os.path.isfile(path_to_wordlist.replace("\'", "")):
        print(f"{path_to_wordlist}\nDictionary file not found.")
        sys.exit(0)
    fill_dirs_from_file(path_to_wordlist)


def check_site_annotaion(hostname):
    global DOMAIN
    """The function checks if there is a connection with the host"""
    hostname = re.findall(r'[a-z]+://[a-z.]+[a-z]{2,3}/', hostname)
    try:
        response = requests.get(hostname[0], headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit \
                                            537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"}, timeout=1)
        response.raise_for_status()
        if response.status_code == 200:
            print('Available')
    except (requests.exceptions.HTTPError, requests.exceptions.Timeout) as e:
        print('ERROR: %s' % e)
    DOMAIN = hostname[0]


def check_args_qnt(args_qnt):
    """The function checks the number of arguments"""
    if len(args_qnt) == 1:
        parser.print_help()
        sys.exit(0)


def check_app_keys():
    """The function checks the validity of the arguments"""
    # Number of arguments
    check_args_qnt(sys.argv)
    # Dictionary File Availability
    check_wordlist_file(args.w)
    # Host Availability
    check_site_annotaion(args.u)
    print(f"\nWe work with the site: {DOMAIN} \nNumber of running threads: {args.t} \nPath to dictionary: {args.w}\
    \nFile extensions: { 'Not set' if args.e[0] == '/' else args.e}")


def fill_dirs_from_file(dirs_file):
    """The function reads a file with folder addresses into a list"""
    with open(dirs_file, "r") as reader:
        for line in reader.readlines():
            DIRS.append(line.replace('\n', args.e+'\n'))
    print("\nDictionary strings loaded: " + str(len(DIRS)) + "\n")


def result_file(counter, len_dirs, host_code, target_url):
    """Function of writing results to a file"""
    with open('fuzz.txt', 'a') as file:
        file.write(f"{counter:0>8} of {len_dirs}\t{host_code}\t{target_url}\n")


def print_result(host_code, target_url, counter):
    if host_code == 404:
        print('\r', f"{counter:0>8} of {len(DIRS)}\t{Fore.RED}{host_code}{Fore.RESET}\t{target_url}", end=' '*30)
    else:
        result_file(counter, len(DIRS), host_code, target_url)
        if 400 <= host_code < 500:
            print('\r', f"{counter:0>8} of {len(DIRS)}\t{Fore.RED}{host_code}{Fore.RESET}\t{target_url}", ' '*30)
        if host_code == 200:
            print('\r', f"{counter:0>8} of {len(DIRS)}\t{Fore.YELLOW}{host_code}{Fore.RESET}\t{target_url}", ' '*30)
        if 300 <= host_code < 400:
            print('\r', f"{counter:0>8} of {len(DIRS)}\t{Fore.BLUE}{host_code}{Fore.RESET}\t{target_url}", ' '*30)


def get_site_dirs(DIR):
    """Directory checking function"""
    global counter
    if args.b64 == True:
        target_url = args.u.replace('FUZZ', base64.b64encode(DIR.strip().encode("UTF-8")).decode("UTF-8"))
    elif args.uenc == True:
        target_url = args.u.replace('FUZZ', urllib.parse.quote(DIR.strip()))
    else:
        target_url = args.u.replace('FUZZ', DIR.strip())
    try:
        if args.head != '!':
            headers = {elem.split(':')[0].strip(): elem.split(':')[1].strip() for elem in args.head.split(', ')}
            host_answer = requests.get(target_url, allow_redirects=False, headers=headers)
        else:
            host_answer = requests.get(target_url, allow_redirects=False)
        host_code = host_answer.status_code
        print_result(host_code, target_url, counter)
        counter += 1
    except:
        time.sleep(1)


if __name__ == "__main__":
    greetings()
    check_app_keys()
    with Pool(args.t) as p:
        try:
            p.map(get_site_dirs, DIRS)
        except KeyboardInterrupt:
            print(Fore.RED + '  ERROR: manually stop Ctrl+C')







