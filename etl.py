from typing import List, Dict, Tuple

import requests

from constants import START_YEAR, FINISH_YEAR, URL


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
    for year in range(START_YEAR, FINISH_YEAR + 1):
        result = crawler(URL.format(year))
        women, men = parser(result)
        print(year,' Rate = ', women / men)



if __name__ == '__main__':
    get_all_data()
