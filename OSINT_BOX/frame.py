import full_scripts.host_ip as add
import full_scripts.site_location as geo
import full_scripts.whois_ip as wh
import full_scripts.nslookup_ip as ns
import full_scripts.dns_mx_record as dmr
import full_scripts.reverse_dns as redns
import full_scripts.robots_txt as rob
import full_scripts.site_map as map
import full_scripts.reverse_ip_lookup as rev_look
import re
import contextlib
from colorama import Fore


arg_dict = {
    0: ('Exit the program', exit), 1: ('Host IP', add.addres), 2: ('Site location', geo.geo_ip),
    3: ('Whois', wh.who), 4: ('Nslookup', ns.ns_look), 5: ('Dns MX-Record', dmr.mx_check),
    6: ('Reverse DNS', redns.rev_dns), 7: ('robots.txt', rob.main), 8: ('sitemap.xml', map.main),
    9: ('Reverse ip lookup', rev_look.get_page), 10: ('All', 'All')
}

logo = Fore.GREEN + r'''
  ___  ____ ___ _   _ _____   ____   _____  __
 / _ \/ ___|_ _| \ | |_   _| | __ ) / _ \ \/ /
| | | \___ \| ||  \| | | |   |  _ \| | | \  / 
| |_| |___) | || |\  | | |   | |_) | |_| /  \ 
 \___/|____/___|_| \_| |_|   |____/ \___/_/\_\
''' + Fore.RESET


def all_action(num):
    while input_str := input('\nEnter ip or URL : '):
        if check := re.findall(r"^(?:\d{1,3}\.?\b){4}$", input_str):
            with open("info.txt", "w") as o:
                with contextlib.redirect_stdout(o):
                    dict_ip = [2, 6, 9]
                    for i in dict_ip:
                        print('-'*35, arg_dict[i][0], '-'*35, sep='\n')
                        arg_dict[i][1](num, check[0])
            break
        elif check := re.findall(r'[a-z]+://([A-Za-z_0-9.-]+).*', input_str):
            dict_domain = [3, 4, 5, 7, 8, 9]
            with open("check_domain.txt", "w") as o:
                with contextlib.redirect_stdout(o):
                    print('-'*35, arg_dict[1][0], '-'*35, sep='\n')
                    ip, domain = arg_dict[1][1](num, check[0])
                    for i in dict_domain:
                        print('-'*35, arg_dict[i][0], '-'*35, sep='\n')
                        arg_dict[i][1](num, domain)
                    print('-'*35, arg_dict[2][0], '-'*35, sep='\n')
                    arg_dict[2][1](num, ip)
                    print('-'*35, arg_dict[6][0], '-'*35, sep='\n')
                    arg_dict[6][1](num, ip)
            break
        else:
            print('The entered url or ip contains an error in the name')


def menu_action():
    print(logo)
    for key, (name, _) in arg_dict.items():
        print(Fore.GREEN, '\t', str(key) + '.', name, Fore.RESET)


if __name__ == "__main__":
    menu_action()
    while True:
        try:
            num = (int(input('\nEnter the option number: ')))
        except ValueError:
            print("Error, you entered the wrong number\n")
        else:
            if 1 <= num <= 10:
                if num == 10:
                    all_action(num)
                    print('Done!')
                    break
                else:
                    print('-'*35, arg_dict[num][0], '-'*35, sep='\n')
                    arg_dict[num][1](num, '')
            elif num == 0:
                break
            else:
                print('Error! You entered not a number or a number in the range')
    print('\nThe program is complete')

