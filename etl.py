from threading import Thread

from typing import List, Dict, Tuple

import requests

from constants import START_YEAR, FINISH_YEAR, URL


class ThreadWithResult(Thread):
    def run(self):
        self._return = []

        if self._target is not None:
            self._return = self._target(*self._args, **self._kwargs)

    def join(self, *args) -> List[Dict]:
        Thread.join(self, *args)
        return self._return


def crawler(url: str) -> List[Dict]:
    r = requests.get(url)
    return r.json()


def parser(population_data: Dict) -> Tuple[int, int]:
    women = 0
    men = 0
    for row in population_data:
        women += row['females']
        men += row['males']
    return women, men


def get_all_data():
    threads = []

    for year in range(START_YEAR, FINISH_YEAR + 1):
        threads.append(
            (year, ThreadWithResult(target=crawler, args=(URL.format(year),)))
        )

    for _, thread in threads:
        thread.start()

    for year, thread in threads:
        result = thread.join()
        women, men = parser(result)
        print(year, ' Rate = ', women / men)


if __name__ == '__main__':
    get_all_data()
