import asyncio
import random

import aiohttp

from bs4 import BeautifulSoup as BS
from fake_useragent import UserAgent


BASE_URL = 'https://skillbox.ru/media/marketing/chto-takoe-vebsayt-kak-on-rabotaet-i-kak-sozdayut-sayty/'
HEADERS = {'User-Agent': UserAgent().random}

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get(BASE_URL, headers = HEADERS) as response:
            r = await aiohttp.StreamReader.read(response.content)
            soup = BS(r, 'html.parser')
            items = soup.findAll('p')
    

            print(items)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    
