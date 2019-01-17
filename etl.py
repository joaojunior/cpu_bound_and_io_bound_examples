from threading import Thread

import requests

from constants import START_YEAR, FINISH_YEAR, URL


def crawler(url: str):
    r = requests.get(url)
    print(url, r.status_code)


def get_all_data():
    threads = []

    for year in range(START_YEAR, FINISH_YEAR + 1):
        threads.append(Thread(target=crawler, args=(URL.format(year), )))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == '__main__':
    get_all_data()
