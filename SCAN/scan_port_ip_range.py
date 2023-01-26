from multiprocessing import Pool
import socket
from netaddr import IPRange
import itertools


def port_scan(arg):
    target, port = arg
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    try:
        s.connect((target, port))
        print(target, 'Port :', port, "is open.")
    except socket.error:
        pass
    finally:
        s.close()


if __name__ == "__main__":
    ipStart, ipEnd = input('Enter IP-IP: ').split('-')
    iprange = IPRange(ipStart, ipEnd)
    number = int(input('Number of threads: '))
    ports = [43, 80, 109, 110, 115, 118, 119, 143, 194, 220, 443, 540, 585, 591, 1112, 1433, 1443, 3128, 3197, 3306, 3899,\
         4224, 4444, 5000, 5432, 6379, 8000, 8080, 10000]
    with Pool(number) as p:
        p.map(port_scan, [[str(host), port] for host, port in list(itertools.product(iprange, ports))])