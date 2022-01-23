import aiohttp
import asyncio
import requests
from bs4 import BeautifulSoup
from links import *

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

headers = {  # Imitate user behavior
    "accept": "*/*",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,"
                  "like Gecko) Chrome/96.0.4664.93 Safari/537.36 "
}


def soup_constructor(link):  # Main engine to create soup object
    req = requests.get(link, headers=headers)
    src = req.text
    soup = BeautifulSoup(src, "lxml")
    return soup


async def parse_Lama():  # scrap Barbershop Lucky Lama
    async with aiohttp.ClientSession() as session:
        async with session.get(url_1, ssl=False) as response:
            await response.read()
            result = soup_constructor(url_1).find_all(class_="t812__pricelist-item__row_1 " \
                                                               "t-row")
            title = "Barbershop Lucky Lama"
            lst = []
            for item in result:
                lst.append(item.text.strip())
            lst.insert(0, title)
            return lst


async def parse_Brutmen():  # scrap Barbershop Brutmen
    async with aiohttp.ClientSession() as session:
        async with session.get(url_2, ssl=False) as response:
            await response.read()
            result = soup_constructor(url_2).find(class_="mprice mprice2").find_all("td")
            title = "Barbershop Brutmen"
            lst = []
            for item in result:
                lst.append(item.text)
            lst.insert(0, title)
            return lst


async def parse_Shamps():  # scrap Barbershop Shamps Cut
    async with aiohttp.ClientSession() as session:
        async with session.get(url_3, ssl=False) as response:
            await response.read()
            result = soup_constructor(url_3).find_all("div", class_="t792__wrapper")
            title = "Barbershop Shamps Cut"
            lst = []
            for item in result:
                lst.append(item.text.strip())
            lst.insert(0, title)
            return lst


async def main():
    async with aiohttp.ClientSession() as session:
        result = await asyncio.gather(parse_Lama(), parse_Shamps(), parse_Brutmen())
    return result


result = asyncio.run(main())

data = " ".join(map(str, result)) # create str instead list

data = data.replace(",","\n")
data = data.replace("]","\n")
data = data.replace("[","\n")




