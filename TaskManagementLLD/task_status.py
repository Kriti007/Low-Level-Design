from enum import Enum


class TaskStatus(Enum):
    NEW = "new"
    CREATED = "created"
    QUEUED = "queued"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
