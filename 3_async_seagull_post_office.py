import asyncio
import time


async def send_seagull(i: int):
    print(f'Sending seagull {i}')
    await asyncio.sleep(1)
    print(f'Seagull {i} delivered the letter.')



async def main():
    start = time.perf_counter()
    for seagull in range(1, 5):
        await send_seagull(seagull)
    elapsed = time.perf_counter() - start
    print(f'Elapsed: {elapsed} seconds.')


if __name__ == '__main__':
    asyncio.run(main())