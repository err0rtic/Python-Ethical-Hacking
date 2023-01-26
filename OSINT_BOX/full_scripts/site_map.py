import requests
from bs4 import BeautifulSoup


def get_page_data(html):
    res = BeautifulSoup(html.text, 'lxml')
    line = res.find_all("loc")
    for i in line:
        print(i.text)


def check(url):
    if url[-1] == '/':
        page = requests.get(url + 'sitemap.xml')
    else:
        page = requests.get (url + '/sitemap.xml')
    if page.status_code == 200:
        get_page_data(page)
    else:
        print('File "sitemap.xml" not found!')


def main(num, domain):
    if num != 10:
        url = input ('Enter host [https://site.com]: ')
    url = 'https://' + domain
    try:
        check(url)
    except requests.RequestException as e:
        print(e)
    except requests.ConnectionError as e:
        print(e)
    except:
        print('Error')

