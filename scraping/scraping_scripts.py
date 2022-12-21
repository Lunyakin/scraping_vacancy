import requests
from bs4 import BeautifulSoup as bs
from random import randint

__all__ = ('work_ua', 'dou_ua',)

# TODO дополнить --> 'Accept'
headers = [
    {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"},

    {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36}'}
]


def work_ua(url):
    jobs = []
    errors = []
    domain = 'https://www.work.ua'
    response = requests.get(url, headers = headers[randint(0, 1)])
    if response.status_code == 200:
        soup = bs(response.content, 'html.parser')
        main_div = soup.find('div', id = 'pjax-job-list')
        if main_div:
            div_list = main_div.find_all('div', attrs = {'class': 'job-link'})
            for div in div_list:
                title = div.find('h2')
                href = title.a['href']
                description = div.p.text
                temp_data = div.find('div', attrs = {'class': 'add-top-xs'}).find_all('span', {
                    'class': False, 'data-content': False
                })
                company = temp_data[0].text.strip()
                jobs.append({
                    'title': title.text.strip(),
                    'url': domain + href,
                    'description': description,
                    'company': company,
                })
        else:
            errors.append({'url': url, 'title': 'Main_div does not exist'})
    else:
        errors.append({'url': url, 'title': 'Page do not response'})

    return jobs, errors


def dou_ua(url):
    jobs = []
    errors = []
    response = requests.get(url, headers = headers[randint(0, 1)])
    if response.status_code == 200:
        soup = bs(response.content, 'html.parser')
        main_div = soup.find('div', id = 'vacancyListId')
        div_list = main_div.find_all('li', attrs = {'class': 'l-vacancy'})
        if main_div:
            for div in div_list:
                title = div.find('div', attrs = {'class': 'title'}).a.text
                href = div.find('div', attrs = {'class': 'title'}).a['href']
                company = div.find('div', attrs = {'class': 'title'}).strong.a.text.strip()
                description = div.find('div', attrs = {'class': 'sh-info'}).text

                jobs.append({
                    'title': title.strip(),
                    'url': href,
                    'description': description,
                    'company': company,
                })
        else:
            errors.append({'url': url, 'title': 'Main_div does not exist'})
    else:
        errors.append({'url': url, 'title': 'Page do not response'})

    return jobs, errors
