import os
import json
import csv

task_ids = set()


class Task:
    def __init__(self, task_id, name, description, due_date, status):
        """initialize a new task"""
        self.task_id = task_id
        self.name = name
        self.description = description
        self.due_date = due_date
        self.status = status

    def __str__(self):
        """string representation of task"""
        return f"{self.task_id}, {self.name}, {self.description}, {self.due_date}, {self.status}"

    def to_dict(self):
        """from task to dictionary format"""
        return {
            "task_id": self.task_id,
            "name": self.name,
            "description": self.description,
            "due_date": self.due_date,
            "status": self.status
        }

    @classmethod
    def from_dict(cls, data):
        """from dictionary format to task"""
        return cls(data["task_id"], data["name"], data["description"], data["due_date"], data["status"])


def load_from_json(path):
    """load tasks from json file and  return a list"""
    with open(path, "r") as file:
        return [Task.from_dict(task) for task in json.load(file)]


def load_from_txt(path):
    """load tasks from txt file and return a list"""
    tasks = []
    with open(path, "r") as file:
        for line in file:
            parts = line.strip().split(", ")
            if len(parts) == 5:
                tasks.append(Task(parts[0], parts[1], parts[2], parts[3], parts[4]))
    return tasks


def load_from_csv(path):
    """load tasks from csv file and return a list"""
    tasks = []
    with open(path, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            tasks.append(Task(row["task_id"], row["name"], row["description"], row["due_date"], row["status"]))
    return tasks


def write_to_json(file_path, tasks):
    """Write tasks to json file"""
    with open(file_path, "w") as file:
        json.dump([task.to_dict() for task in tasks], file, indent=4)


def write_to_txt(file_path, tasks):
    """Write tasks to txt file"""
    with open(file_path, "w") as file:
        for task in tasks:
            file.write(f"{task}\n")


def write_to_csv(file_path, tasks):
    """Write tasks to csv file"""
    with open(file_path, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["task_id", "name", "description", "due_date", "status"])
        writer.writeheader()
        for task in tasks:
            writer.writerow(task.to_dict())


class ToDo:
    def __init__(self):
        """initiate tasks list"""
        self.tasks = []

    def load_tasks(self, path):
        """navigate to corresponding function to load tasks from a file"""
        if os.path.exists(path):
            ext = os.path.splitext(path)[1].lower()
            if ext == ".txt":
                self.tasks.extend(load_from_txt(path))
            elif ext == ".csv":
                self.tasks.extend(load_from_csv(path))
            elif ext == ".json":
                self.tasks.extend(load_from_json(path))
            else:
                print("Unsupported file type.")

    def add_task(self, task_id, name, description, due_date, status):
        """add a new task"""
        if task_id in task_ids:
            print("Task ID must be unique!")
            return
        self.tasks.append(Task(task_id, name, description, due_date, status))
        task_ids.add(task_id)

    def view_all_tasks(self):
        """view all tasks"""
        return '\n'.join(str(task) for task in self.tasks) if self.tasks else "No tasks available."

    def search_task(self, task_id):
        """search task by task id"""
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        return "Task not found."

    def update_task(self, task_id, name=None, description=None, due_date=None, status=None):
        """update task by task id, let skip fields"""
        task = self.search_task(task_id)
        if isinstance(task, Task):
            task.name = name or task.name
            task.description = description or task.description
            task.due_date = due_date or task.due_date
            task.status = status or task.status
            print("Task updated.")
        else:
            print(task)

    def delete_task(self, task_id):
        """delete task by task id"""
        task = self.search_task(task_id)
        if isinstance(task, Task):
            self.tasks.remove(task)
            task_ids.discard(task_id)
            print("Task removed.")
        else:
            print(task)

    def save_tasks(self):
        """save all tasks to a csv/txt/json"""
        ext = input("Enter file type to save (csv/txt/json): ").lower()
        if ext == "csv":
            write_to_csv("to_do_list.csv", self.tasks)
        elif ext == "json":
            write_to_json("to_do_list.json", self.tasks)
        elif ext == "txt":
            write_to_txt("to_do_list.txt", self.tasks)
        else:
            print("Invalid file type.")
        print("Tasks saved.")

    def filter_tasks(self, status):
        """filter tasks by status"""
        return '\n'.join(str(task) for task in self.tasks if task.status == status) or "No matching tasks."


def show_menu():
    print("""
    1. Add Task
    2. View All Tasks
    3. Update Task
    4. Delete Task
    5. Filter Tasks by Status
    6. Save Tasks
    7. Load Tasks
    8. Exit
    """)


def get_input(update_mode=False):
    """get details of a task, lets skip fields when upload mode is on"""
    task_id = input("Enter Task ID: ")
    if update_mode and task_id not in task_ids:
        print("Task ID not found.")
        return None
    if not update_mode and task_id in task_ids:
        print("Task ID already exists.")
        return None
    name = input("Enter Title: ") if not update_mode else input("New title (leave blank to keep current): ")
    description = input("Enter Description: ") if not update_mode else input(
        "New description (leave blank to keep current): ")
    due_date = input("Enter Due Date (YYYY-MM-DD): ") if not update_mode else input(
        "New due date (leave blank to keep current): ")
    status = input("Enter Status (Pending/In Progress/Completed): ") if not update_mode else input(
        "New status (leave blank to keep current): ")
    return [task_id, name, description, due_date, status]


def main():
    app = ToDo()
    print("Welcome to To-Do Application!")
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        if choice == "1": #add new task
            line = get_input()
            if line: app.add_task(*line)
        elif choice == "2": #view all tasks
            print(app.view_all_tasks())
        elif choice == "3": #update a task
            line = get_input(True)
            if line: app.update_task(*line)
        elif choice == "4":
            app.delete_task(input("Enter Task ID: ")) #delete task
        elif choice == "5":
            print(app.filter_tasks(input("Enter status (Pending/In Progress/Completed): ")))#filter
        elif choice == "6": #save tasks
            app.save_tasks()
        elif choice == "7":#load tasks
            app.load_tasks(input("Enter file path: "))
        elif choice == "8":#exit
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
