Design an Asynchronous Task Management Library.

Requirements:
Should allow users to define a task,
Tasks can have dependencies on other tasks,
Tasks get added to a Queue - 1 queue global,
Should have a main task runner (run once for this problem) that runs the tasks in the queue.

Entities - 
1. Task Interface with some concrete tasks like - add, subtract, print
2. TaskQueue - Implemented a stack since we need to maintain topological order
3. TaskRunner - TaskDemo class
4. TaskManager
5. Task State - Enum
   

