from typing import List, Dict, Tuple

import asyncio
import aiohttp

from constants import START_YEAR, FINISH_YEAR, URL


async def crawler(url: str) -> List[Dict]:
    async with aiohttp.ClientSession() as session:
        response = await session.get(url)
        return await response.json()


def parser(population_data: Dict) -> Tuple[int, int, int]:
    year = 0
    women = 0
    men = 0
    for row in population_data:
        year = row['year']
        women += row['females']
        men += row['males']
    return women, men, year


def get_all_data():
    loop = asyncio.get_event_loop()
    tasks = []

    for year in range(START_YEAR, FINISH_YEAR + 1):
        tasks.append(
            asyncio.ensure_future(crawler(URL.format(year)))
        )

    loop.run_until_complete(asyncio.gather(*tasks))
    for task in tasks:
        women, men, year = parser(task.result())
        print(year, ' Rate = ', women / men)


if __name__ == '__main__':
    get_all_data()
