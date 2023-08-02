import asyncio
import time


async def seagull_to_complet_its_task(is_task_difficult: bool):
    # Wait seagull to complete its task and do something else
    if is_task_difficult:
        await asyncio.sleep(4)
    else:
        await asyncio.sleep(2)


async def assign_seagull_with_task(name: str, task: str, is_task_difficult: bool) -> int:
    print(f"Sending seagull {name}")
    await seagull_to_complet_its_task(is_task_difficult)
    print(f"Seagull {name} returned and completed the task: {task}")
    return task


async def main():
    start = time.perf_counter()

    task_1 = asyncio.create_task(
        assign_seagull_with_task("Blocky", "Just go around and block stuff.", True)
    )
    task_2 = asyncio.create_task(
        assign_seagull_with_task("Ozzy", "Scream and wake up the neighbourhood.", False)
    )

    await asyncio.gather(task_1, task_2)

    elapsed = time.perf_counter() - start
    print(f"Elapsed: {elapsed} seconds.")


if __name__ == "__main__":
    asyncio.run(main())
