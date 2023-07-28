import asyncio
from asyncio import Future, Task
from typing import Coroutine


class TaskManager:
    # Used for strong referencing tasks
    _background_task_reference = set()

    # Used for strong referencing futures
    _future_task_reference = set()

    def create_umbrella_task(self, background_task: Coroutine) -> Task:
        """Create task using AsyncIO and keep task reference in memory - so it doesn't get garbage collected.

        Accepts Coroutine and triggers background Task.

        """
        task = asyncio.create_task(background_task)

        self._background_task_reference.add(task)

        task.add_done_callback(self._background_task_reference.discard)
        # task.add_done_callback(lambda t: self._background_task_reference.remove(t))

        return task

    def ensure_umbrella_future(self, background_task: Coroutine) -> Future:
        """Create Future object using AsyncIO and keep task reference in memory - so it doesn't get garbage collected.

        Accepts Coroutine and returns Future.

        """
        future_task = asyncio.ensure_future(background_task)

        self._future_task_reference.add(future_task)

        future_task.add_done_callback(self._future_task_reference.discard)
        # future_task.add_done_callback(lambda ft: self._future_task_reference.remove(ft))

        return future_task


task_manager = TaskManager()
