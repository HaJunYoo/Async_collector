import os
import aiohttp
import asyncio
from config import get_secret
import aiofiles

# pip install aiofiles==0.7.0


async def img_downloader(session, img):
    img_name = img.split("/")[-1].split("?")[0]

    # 다운받을 폴더 생성
    try:
        os.mkdir("./images")
    except FileExistsError:
        pass

    async with session.get(img) as response:
        # 응답이 성공적이라면
        if response.status == 200:
            # wb = write byte 쓰기 위해 비어 있는 2진 파일을 작성
            async with aiofiles.open(f"./images/{img_name}", mode="wb") as file:
                img_data = await response.read()
                await file.write(img_data)


async def fetch(session, url, i):
    print(i + 1)
    headers = {
        "X-Naver-Client-Id": get_secret("NAVER_API_ID"),
        "X-Naver-Client-Secret": get_secret("NAVER_API_SECRET"),
    }
    async with session.get(url, headers=headers) as response:
        result = await response.json()
        items = result["items"]
        images = [item["link"] for item in items]
        # 각각의 이미지에 대해서 이미지 다운로더가 실행
        await asyncio.gather(*[img_downloader(session, img) for img in images])


async def main():
    BASE_URL = "https://openapi.naver.com/v1/search/image"
    keyword = "cat"
    urls = [f"{BASE_URL}?query={keyword}&display=20&start={1+ i*20}" for i in range(10)]
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
        await asyncio.gather(*[fetch(session, url, i) for i, url in enumerate(urls)])


if __name__ == "__main__":
    asyncio.run(main())
