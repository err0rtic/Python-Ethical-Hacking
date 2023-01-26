import requests


def get_page_data(html):
    res = html.text
    print(res)


def check(url):
    head = {"User-Agent": "Mozilla/5.0 (X11; Linux x86 64) AppLewebkit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
    if url[-1] == '/':
        page = requests.get (url + 'robots.txt', headers=head)
    else:
        page = requests.get(url + '/robots.txt', headers=head)
    if page.status_code != 404:
        get_page_data(page)
    else:
        print('File "robots .txt" not found!')


def main(num, domain):
    if num != 10:
        url = input('Enter url [https://site.com]: ')
    url = 'https://' + domain
    try:
        check(url)
    except requests.RequestException as e:
        print(e)
    except requests.ConnectionError as e:
        print(e)
    except:
        print('Error')

