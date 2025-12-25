import sys
from task_manager import TaskManager


class TaskCli:
    def __init__(self):
        self.task_manager = TaskManager()

    def run(self):
        if len(sys.argv)  < 2:
            print("Usage: python main.py <command> [args]")
            return

        command = sys.argv[1]

        match command:
            case "add":
                if len(sys.argv) < 3:
                    print("Usage: python main.py add <task_description>")
                    return
                self.task_manager.add_task(sys.argv[2])
                print("Task added successfully.")
            case "list":
                if len(sys.argv) == 2:
                    self.task_manager.list_tasks()
                elif len(sys.argv) == 3:
                    self.task_manager.list_tasks(sys.argv[2])
                else:
                    print("Usage: python main.py list [status]")

            case "delete":
                if len(sys.argv) < 3:
                    print("Usage: python main.py delete <task_id>")
                    return
                else:
                    try:
                        if self.task_manager.delete_task(int(sys.argv[2])):
                            print("Task deleted successfully.")
                        else: print("Task not found.")
                    except ValueError:
                        print("Invalid task id.")

            case "update":
                if len(sys.argv) < 4:
                    print("Usage: python main.py update <task_id> <new_description>")
                    return
                else:
                    try:
                        if result := self.task_manager.update_task(int(sys.argv[2]), sys.argv[3]):
                            print(f"Task {result['description']} updated successfully.")
                        else: print("Task not found.")
                    except ValueError:
                        print("Invalid task id.")

            case "status":
                if len(sys.argv) < 4:
                    print("Usage: python main.py status <task_id> <status>")
                    return
                else:
                    try:
                        if result := self.task_manager.update_status(int(sys.argv[2]), sys.argv[3]):
                            print(f"Task {result['status']} updated successfully.")
                        else: print("Task not found.")
                    except ValueError:
                        print("Invalid task id.")

