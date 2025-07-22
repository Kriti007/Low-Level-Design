import asyncio

from task_manager import TaskManager


class TaskDemo:
    def __init__(self):
        self.task_manager = TaskManager()

    async def run(self):
        print_task_id = self.task_manager.create_task("print")
        add_task_id = self.task_manager.create_task("addition")
        sub_task_id = self.task_manager.create_task("subtraction")
        self.task_manager.add_dependencies(print_task_id, [add_task_id])
        self.task_manager.add_dependencies(add_task_id, [sub_task_id])
        self.task_manager.add_dependencies(sub_task_id, [])
        runner = await self.task_manager.run()


async def main():
    demo = TaskDemo()
    await demo.run()

if __name__ == "__main__":
    asyncio.run(main())