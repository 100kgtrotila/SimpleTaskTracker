from datetime import datetime
from task_status import TaskStatus
from file_handler import *
from typing import Dict, Any, Optional

class TaskManager:
    def __init__(self):
        self.file_handler = FileHandler("tasks.json")


    def add_task(self, description: str) -> int:
        tasks = self.file_handler.read_data()

        if len(tasks) > 0:
            new_id = tasks[-1]["id"] + 1
        else:
            new_id = 1

        timestamp = datetime.now().isoformat()

        new_task = {"id": new_id, "description": description, "status": TaskStatus.TODO.value, "created_at": timestamp, "updated_at": timestamp}

        tasks.append(new_task)
        self.file_handler.save_data(tasks)
        print(f"Task {new_id} added successfully.")
        return new_id

    def list_tasks(self, status_filter: str = None) -> None:
        tasks = self.file_handler.read_data()

        if not tasks:
            print("No tasks found.")
            return

        if status_filter:
            filtered_tasks = [t for t in tasks if t["status"] == status_filter]
        else:
            filtered_tasks = tasks

        if not filtered_tasks:
            print(f"No tasks with status '{status_filter}' found.")
            return

        print(f"{'ID':<5} | {'Status':<12} | {'Description'}")
        print("-" * 40)

        for task in filtered_tasks:
            print(f"{task['id']:<5} | {task['status']:<12} | {task['description']}")


    def delete_task(self, task_id: int) -> bool:
        tasks = self.file_handler.read_data()

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
        tasks = self.file_handler.read_data()

        if len(tasks) == 0:
            print("No tasks found.")
            return

        for task in tasks:
            if task["id"] == task_id:
                task["description"] = new_description
                self.file_handler.save_data(tasks)
                return task

        return None

    def update_status(self, task_id, new_status: str) -> Optional[Dict[str, Any]]:
        valid_statuses = [s.value for s in TaskStatus]
        if new_status not in valid_statuses:
            print(f"Invalid status: {new_status}. Valid statuses are: {', '.join(valid_statuses)}")
            return None

        tasks = self.file_handler.read_data()

        if len(tasks) == 0:
            print("No tasks found.")
            return

        for task in tasks:
            if task["id"] == task_id:
                task["status"] = new_status
                task["updated_at"] = datetime.now().isoformat()
                self.file_handler.save_data(tasks)
                return task
        return None