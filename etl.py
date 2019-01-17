import requests

from constants import START_YEAR, FINISH_YEAR, URL


def crawler(url):
    r = requests.get(url)
    print(url, r.status_code)


def get_all_data():
    for year in range(START_YEAR, FINISH_YEAR + 1):
        crawler(URL.format(year))


if __name__ == '__main__':
    get_all_data()
