import re

import requests
from bs4 import BeautifulSoup


if __name__ == '__main__':
    pattern = r'\d{2}\.\d{2}'
    resp = requests.get(
        'https://weather.i.ua/Kyiv/',
        headers={'user-agent': ''}
    )
    soup = BeautifulSoup(resp.text, 'html.parser')

    curr_time_text = soup.findAll('div', class_='layout layout-sidebar_premium')[0].find('h2').getText()
    curr_time = re.findall(pattern, curr_time_text)[0]
    print("Дата: {}".format(curr_time))

    for el in soup.find_all('div', class_="weather_item")[8:21]:
        print(
            "Час: {},".format(el.findAll('span', class_="_title", text=True)[0].getText()),
            "температура: {}".format(el.findAll('span', class_="_value")[0].getText()),
        )
