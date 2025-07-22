import threading
import uuid
from collections import deque, defaultdict
from print_task import PrintTask
from addition_task import AdditionTask
from subtraction_task import SubtractionTask
from task_status import TaskStatus


class TaskManager:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(TaskManager, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if hasattr(self, '_initialized') and self._initialized:
            return
        self.task_order = []
        self.remaining_tasks = []
        self.task_map = {}
        self._initialized = True

    def create_task(self, task_type, dependencies=[]):
        task_id = uuid.uuid4()
        task = None
        if task_type == "print":
            task = PrintTask(task_id, [])
        if task_type == "addition":
            task = AdditionTask(task_id, [])
        if task_type == "subtraction":
            task = SubtractionTask(task_id, [])
        if dependencies:
            task.add_dependencies(dependencies)

        self.task_map[task_id] = task
        task.set_status(TaskStatus.QUEUED)
        return task_id

    def add_dependencies(self, task_id, dependencies):
        if dependencies:
            task = self.task_map[task_id]
            task.add_dependencies(dependencies)

    def validate_dependencies(self):
        adj = defaultdict(list)
        for tid in self.task_map.keys():
            task = self.task_map[tid]
            adj[tid].extend(task.dependencies)
        if self.has_cycle(adj):
            raise Exception("Can't resolve dependencies- CYCLE DETECTED")
        print(self.task_order)

    def set_task_status(self, task_id, status):
        self.task_map[task_id].set_status(status)

    def get_task_status(self, task_id):
        return self.task_map[task_id].get_status()

    def dependencies_resolved(self, task_id):
        dependencies = self.task_map[task_id].dependencies
        for d in dependencies:
            print(f"d in deps {d}")
            if d in self.task_map:
                dep_task = self.task_map[d]
                print(f"task in deps {dep_task}")
                if dep_task.task_status != TaskStatus.COMPLETED:
                    return False
        return True

    async def run(self):
        self.validate_dependencies()
        while self.task_order:
            task_id = self.task_order.pop()
            task = self.task_map[task_id]
            print(f"Checking task: {task_id} with dependencies: {task.dependencies}")

            t = await task.run_task()
            task.set_status(TaskStatus.COMPLETED)

    def has_cycle(self, adj: defaultdict):
        rec_stack = set()
        visited = set()

        def dfs(tid):
            if tid in rec_stack:
                return True
            if tid in visited:
                return False

            rec_stack.add(tid)
            for neighbor in list(adj[tid]):
                if dfs(neighbor):
                    return True
            rec_stack.remove(tid)
            visited.add(tid)
            self.task_order.append(tid)
            return False

        for key in list(adj.keys()):
            if key not in visited:
                if dfs(key):
                    return True
        return False
