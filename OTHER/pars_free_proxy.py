import requests
from bs4 import BeautifulSoup


def what_page(html):
    soup = BeautifulSoup(html.text, 'lxml')
    line =soup.find('div', class_="pager").find_all('a')
    result = []
    for i in line:
        result.append(int(i.text))
    return max(result)


def get_page(html):
        soup = BeautifulSoup(html.text, 'lxml')
        line =soup.find("tbody").find_all('tr')
        for i in line:
            val = i.find_all('td')
            print(f'{val[1].text}:{val[2].text}')


if __name__ == "__main__":
    url = f'http://foxtools.ru/Proxy'
    page = requests.get(url)
    count_page = what_page(page)
    for i in range(1, count_page + 1):
        url = f'http://foxtools.ru/Proxy?page={i}'
        page = requests.get(url)
        get_page(page)