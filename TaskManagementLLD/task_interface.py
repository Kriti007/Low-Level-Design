from abc import ABC, abstractmethod
from task_status import TaskStatus


class TaskInterface(ABC):
    def __init__(self, task_id: int, dependencies: list):
        self.task_id = task_id
        self.task_status = TaskStatus.NEW
        self.dependencies = dependencies


    @abstractmethod
    def set_status(self):
        pass

    @abstractmethod
    def add_dependencies(self, dependencies):
        pass

    @abstractmethod
    def get_status(self):
        pass

    @abstractmethod
    async def run_task(self):
        pass