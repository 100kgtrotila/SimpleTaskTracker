# Task Tracker CLI

This is a solution to the [Task Tracker](https://roadmap.sh/projects/task-tracker) project on roadmap.sh.

A lightweight, fast, and reliable command-line interface (CLI) application for tracking tasks. Built with **pure Python** to demonstrate clean architecture and file handling concepts without external dependencies.

## ✨ Features

* **CRUD Operations**: Add, Read (List), Update, and Delete tasks.
* **Status Management**: Mark tasks as `todo`, `in-progress`, or `done`.
* **Filtering**: List all tasks or filter by status (e.g., `list done`).
* **Data Persistence**: All data is stored locally in a `tasks.json` file.
* **Error Handling**: Graceful handling of invalid inputs and file errors.

## 🛠️ Tech Stack

* **Language**: Python 3.10+ (utilizing `match/case` syntax).
* **Storage**: JSON (Native `json` module).
* **Architecture**: Layered Architecture (separation of concerns):
    * `task_cli.py`: Presentation Layer (User input/output).
    * `task_manager.py`: Business Logic Layer.
    * `file_handler.py`: Data Access Layer.

## 📦 Installation & Usage

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/task-tracker-cli.git](https://github.com/your-username/task-tracker-cli.git)
    cd task-tracker-cli
    ```

2.  **Run the application:**
    You don't need to install any requirements! Just run `main.py`.

    ```bash
    # Add a new task
    python main.py add "Buy groceries"

    # List all tasks
    python main.py list

    # List only done tasks
    python main.py list done

    # Mark a task as in-progress (by ID)
    python main.py 1 in-progress

    # Update a task description
    python main.py update 1 "Buy groceries and cook dinner"

    # Delete a task
    python main.py delete 1
    ```

## 📂 Project Structure

```text
TaskTracker/
├── main.py           # Entry point
├── task_cli.py       # Controller / Menu Logic
├── task_manager.py   # Service / Business Logic
├── file_handler.py   # Repository / File I/O
├── task_status.py    # Enums
└── tasks.json        # Data storage (auto-generated)