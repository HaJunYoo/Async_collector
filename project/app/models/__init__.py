from motor.motor_asyncio import AsyncIOMotorClient

from odmantic import AIOEngine
from app.config import MONGO_URL, MONGO_DB_NAME


class MongoDB:

    def __init__(self):
        self.client = None
        self.engine = None

    def connect(self):
        self.client = AsyncIOMotorClient(MONGO_URL)
        self.engine = AIOEngine(client=self.client, database=MONGO_DB_NAME)
        print("db와 성공적으로 연결이 되었습니다.")

    def close(self):
        self.client.close()


# 인스턴스를 한번만 찍는 싱글톤 패턴
mongodb = MongoDB()

