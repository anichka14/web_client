"""[B]26.09. Скласти програму, яка читає прогноз погоди у заданому місті (назва міста
вводиться англійською як параметр) з сайту weather.i.ua та показує поточну дату і
прогноз температури протягом поточного дня (12 значень).
Запит на погоду у заданому місті:
https://weather.i.ua/<місто>/
Наприклад,
https://weather.i.ua/Kyiv/"""

from urllib.request import urlopen, Request
from urllib.error import HTTPError
import re


def get_weather_html(city="Kyiv"):
    try:
        url = "https://weather.i.ua/{}/"
        requests = Request(
            url.format(city),
            headers={
                "user-agent": ""
            },
        )
        response = urlopen(requests)
        enc = response.info().get_content_charset()
        html = str(response.read(), encoding=enc, errors="ignore")
        return html
    except HTTPError as e:
        print(e)


if __name__ == "__main__":
    data_pattern = r'(\d{2}\.\d{2})<\/h2><ul class="weather">'
    weather_pattern = r'<div class="weather_item"><span class="_title">(\d{2}:\d{2}).+?(?=<span class="_value">)<span class="_value"><em>(.+?(?=<\/em>))<\/em>'
    city = input("Введіть місто: ")
    html = get_weather_html(city)

    match = re.search(data_pattern, html)
    print("Поточна дата: ", match.group(1))
    for time, temp in re.findall(weather_pattern, html)[8:21]:
        print(f"Час: {time}, температура: {temp.replace('&deg;', '°')}")
