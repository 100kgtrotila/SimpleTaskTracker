import datetime

from Repository import file_handler
from file_handler import *
from typing import List, Dict, Any, Optional

class TaskManager:
    def __init__(self):
        self.file_handler = FileHandler("tasks.json")


    def add_task(self, description: str) -> int:
        tasks = file_handler.read_data()

        if len(tasks) > 0:
            new_id = tasks[-1]["id"] + 1
        else:
            new_id = 1

        timestamp = datetime.now().isoformat()

        new_task = {"id": new_id, "description": description, "status": "todo", "created_at": timestamp, "updated_at": timestamp}

        tasks.append(new_task)
        self.file_handler.save_data(tasks)
        print(f"Task {new_id} added successfully.")
        return new_id


    def list_tasks(self) -> None:
        tasks = file_handler.read_data()
        if len(tasks) == 0:
            print("No tasks found.")
            return

        print(f"{'ID':<5} | {'Status':<12} | {'Description'}")
        print("-" * 40)
        for task in tasks:
            print(f"{task['id']:<5} | {task['status']:<12} | {task['description']}")


    def delete_task(self, task_id: int) -> bool:
        tasks = file_handler.read_data()

        if len(tasks) == 0:
            print("No tasks found.")
            return False

        for task in tasks:
            if task["id"] == task_id:
                tasks.remove(task)
                self.file_handler.save_data(tasks)
                return True

        return False

    def update_task(self, task_id, new_description: str) -> Optional[Dict[str, Any]]:
        tasks = file_handler.read.data()

        if len(tasks) == 0:
            print("No tasks found.")
            return

        for task in tasks:
            if task["id"] == task_id:
                task["description"] = new_description
                self.file_handler.save_data(tasks)
                return task

        return None