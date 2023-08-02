import asyncio
import time


async def seagull_to_complet_its_task():
    # Wait seagull to complete its task and do something else
    await asyncio.sleep(2)


async def assign_seagull_with_task(name: str, task: str) -> int:
    print(f"Sending seagull {name}")
    await seagull_to_complet_its_task()
    print(f"Seagull {name} returned and completed the task: {task}")
    return task


async def main():
    start = time.perf_counter()

    task_1 = asyncio.create_task(
        assign_seagull_with_task("Stippy", "Deliver a secret letter.")
    )
    task_2 = asyncio.create_task(
        assign_seagull_with_task("Ozzy", "Scream and wake up the neighbourhood.")
    )
    task_3 = asyncio.create_task(
        assign_seagull_with_task("Tommy", "Fly around the city.")
    )
    task_4 = asyncio.create_task(
        assign_seagull_with_task("Nikolas", "Steal an ice cream.")
    )

    res = await asyncio.gather(task_2, task_3, task_1, task_4)

    elapsed = time.perf_counter() - start
    print(f"Elapsed: {elapsed} seconds.")
    print(f"Results: {res}")


if __name__ == "__main__":
    asyncio.run(main())
