import requests


def get_page(num, ip):
    if num != 10:
        ip = input('Enter IP or domain: ')
    url = f'https://api.viewdns.info/reverseip/?host={ip}&apikey=a66040ee8cbc5a56643a67b35c618ce1c8e1ec25&output=json'
    try:
        page = requests.get(url)
    except requests.RequestException as e:
        print(e)
    except:
        print('IP or domain wrong')
    else:
        json = page.json()
        for i in json['response']['domains']:
            print(i['name'])


