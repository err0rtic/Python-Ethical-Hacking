import pygeoip
import re


def geo_ip(num, ip):
    if num != 10:
        while True:
            ip = input("Enter ip: ")
            if check := re.findall(r"^(?:\d{1,3}\.?\b){4}$", ip):
                break
            else:
                print('The entered ip contains an error in the name')
    gi = pygeoip.GeoIP('GeoIPCity.dat')
    try:
        city = gi.record_by_addr(ip)
    except pygeoip.GeoIPError as e:
        print(f'Error ip, error raised is {e}')
    finally:
        if city == None:
            print(f'Dont info for ip {ip}')
        else:
            for key in city:
                if city[key] is None or city[key] == 0:
                    continue
                else:
                    print(key, city[key], sep=" : ")
