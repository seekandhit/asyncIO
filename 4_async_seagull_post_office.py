import asyncio
import time


async def send_seagull(i: int) -> int:
    print(f"Sending seagull {i}")
    await asyncio.sleep(1)
    print(f"Seagull {i} delivered the letter.")
    return i


async def main():
    start = time.perf_counter()
    results = await asyncio.gather(
        send_seagull(1),
        send_seagull(2),
        send_seagull(3),
        send_seagull(4),
        send_seagull(5),
    )
    elapsed = time.perf_counter() - start
    print(f"Elapsed: {elapsed} seconds.")
    print(f"Results: {results}")


if __name__ == "__main__":
    asyncio.run(main())
