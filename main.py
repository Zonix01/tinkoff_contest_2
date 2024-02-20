import asyncio
from concurrent.futures import ThreadPoolExecutor
from enum import Enum
from dataclasses import dataclass
from typing import List
import datetime
import random

@dataclass
class Address:
    pass

@dataclass
class Payload:
    pass

class Result(Enum):
    Accepted = 1
    Rejected = 2

class Event:
    def __init__(self, recipients: List[Address], payload: Payload):
        self.recipients = recipients
        self.payload = payload

class InstanceClass:
    def __init__(self):
        self.executor = ThreadPoolExecutor()

    async def read_data(self) -> Event:
        await asyncio.sleep(1)  # Пример задержки для имитации асинхронной операции
        return Event(recipients=[Address(), Address()], payload=Payload())

    async def send_data(self, dest: Address, payload: Payload) -> Result:
        await asyncio.sleep(1)  # Пример задержки для имитации асинхронной операции
        return random.choice([x for x in Result])  # Пример результата отправки

    async def perform_operation(self) -> None:
        loop = asyncio.get_event_loop()
        while True:
            event = await self.read_data()
            tasks = [loop.run_in_executor(self.executor, self.send_data, recipient, event.payload) for recipient in event.recipients]
            results = await asyncio.gather(*tasks)
            for result in results:
                if await result == Result.Rejected:
                    print(f"Something went wrong while sending data at {datetime.datetime.now()}")
                    await asyncio.sleep(1)
                else:
                    print(f"Data sent at {datetime.datetime.now()}")

async def main():
    contest_instance = InstanceClass()
    await contest_instance.perform_operation()

if __name__ == '__main__':
    asyncio.run(main())
