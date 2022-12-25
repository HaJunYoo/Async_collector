# 코루틴 hello world!
# https://docs.python.org/ko/3/library/asyncio-task.html

import asyncio


async def hello_world():
    print("hello world")
    return 123
    # await 키워드는 async 안에서 사용되어야 한다.
    # await은 awaitable 한 객체에서만 사용될 수 있다.


if __name__ == "__main__":
    asyncio.run(hello_world())
    # asyncio를 통해 async 함수를 파이썬 메인 루틴 안에서 돌림
