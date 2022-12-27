import time


def delivery(name, mealtime):
    print(f"{name}에게 배달 완료!")
    time.sleep(mealtime) # 식사 시간
    print(f"{name} 식사 완료, {mealtime}시간 소요...")
    print(f"{name} 그릇 수거 완료")


def main():
    delivery("A", 1)
    delivery("B", 1)
    delivery("C", 1)

# 동기적 진행
if __name__ == "__main__":
    start = time.time()
    print(main())  # None
    end = time.time()
    print(end - start)
