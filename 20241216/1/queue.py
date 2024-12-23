import asyncio
from asyncio import Queue, Event
import sys


async def writer(queue: Queue, delay: int, stop_event: Event, writer_id: int):
    count = 0
    await asyncio.sleep(delay)
    while not stop_event.is_set():
        item = f"{count}_{writer_id}"
        await queue.put(item)
        count += 1
        await asyncio.sleep(delay)


async def stacker(queue: Queue, stack: list, stop_event: Event):
    while not stop_event.is_set():
        try:
            item = await asyncio.wait_for(queue.get(), timeout=0.1)
            stack.append(item)
        except asyncio.TimeoutError:
            continue


async def reader(stack: list, count: int, delay: int, stop_event: Event):
    await asyncio.sleep(delay)
    for _ in range(count):
        while not stack:
            await asyncio.sleep(0.1)
        print(stack.pop())
        await asyncio.sleep(delay)
    stop_event.set()

async def main(delays, read_count):
    delay1, delay2, delay3 = map(int, delays[:3])
    read_count = int(read_count)

    queue = Queue()
    stack = []
    stop_event = Event()

    writer1 = asyncio.create_task(writer(queue, delay1, stop_event, writer_id=delay1))
    writer2 = asyncio.create_task(writer(queue, delay2, stop_event, writer_id=delay2))
    stacker_task = asyncio.create_task(stacker(queue, stack, stop_event))
    reader_task = asyncio.create_task(reader(stack, read_count, delay3, stop_event))

    await reader_task
    writer1.cancel()
    writer2.cancel()
    stacker_task.cancel()

if __name__ == "__main__":
    input_data = sys.stdin.read()
    exec(input_data)
    delays, read_count = input_data.split(",")[:3], input_data.split(",")[3]
    asyncio.run(main(delays, read_count))

"""
0_2
0_3
1_2
1_3
2_2
3_2
2_3
4_2
3_3
5_2
"""