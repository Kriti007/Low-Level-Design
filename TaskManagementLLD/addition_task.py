from abc import ABC

from task_interface import TaskInterface
from task_status import TaskStatus


class AdditionTask(TaskInterface, ABC):
    def __init__(self, task_id: int, dependencies: list):
        super().__init__(task_id, dependencies)

    def add_dependencies(self, dependencies):
        self.dependencies.extend(dependencies)

    def set_status(self, status):
        self.task_status = status

    def get_status(self):
        return self.task_status

    async def run_task(self):
        self.set_status(TaskStatus.RUNNING)
        a, b = 10, 20
        print(f"This is the addition to add {a} and {b} and is {a+b}")
