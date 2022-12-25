import time
import asyncio

async def delivery(name, mealtime):
    print(f"{name}에게 배달 완료!")
    await asyncio.sleep(mealtime)
    # await : 비동기 -> 동기
    print(f"{name} 식사 완료, {mealtime}시간 소요...")
    print(f"{name} 그릇 수거 완료")
    return mealtime
# 비동기 함수는 atomic한 연산을 요구할 때는 좋지 않다 (덧셈과 같은 사칙연산들)
# 요청을 받고 응답을 받는 류의 코드에 유용
# 비동기 처리는 코드가 진행되다가 다른 함수를 처리하고 다시 이어서 진행하기도 한다
# 코드가 반드시 작성된 순서대로 진행되지 않는다는 것
# 비동기 함수를 async 키워드를 붙여서 코루틴 함수라고 부른다.


async def main():

    result = await asyncio.gather(
        delivery("A", 1),
        delivery("B", 2),
        delivery("C", 3),
    )

    print(result)

# 비동기 함수에서 총 처리 시간은 가장 늦게 먹는 mealtime 이다.
if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(end - start)
