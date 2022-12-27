import ssl

import aiohttp
import asyncio

import certifi

from config import get_secret

# NAVER_API_ID = "CwXT9pf3vmmVO094YT9I"
# NAVER_API_SECRET = "PYAxQDsv1s"

async def fetch(session, url, i):
    print(i + 1)
    headers = {"X-Naver-Client-Id": get_secret("NAVER_API_ID"), "X-Naver-Client-Secret": get_secret("NAVER_API_SECRET")}
    # headers = {"X-Naver-Client-Id": NAVER_API_ID, "X-Naver-Client-Secret": NAVER_API_SECRET}
    async with session.get(url, headers=headers) as response:
        result = await response.json()
        items = result["items"]
        images = [item["link"] for item in items]
        print(images)


async def main():
    BASE_URL = "https://openapi.naver.com/v1/search/image"
    keyword = "cat"
    urls = [f"{BASE_URL}?query={keyword}&display=20&start={1+ i*20}" for i in range(10)]

    # ssl_context = ssl.create_default_context(cafile=certifi.where())
    # conn = aiohttp.TCPConnector(ssl=ssl_context)

    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
        await asyncio.gather(*[fetch(session, url, i) for i, url in enumerate(urls)])


if __name__ == "__main__":
    asyncio.run(main())
