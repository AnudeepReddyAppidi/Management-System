import json

class Task:
    def __init__(self, description, due_date=None, completed=False):
        self.description = description
        self.due_date = due_date
        self.completed = completed

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def save_tasks(self):
        with open("tasks.json", "w") as file:
            json.dump([task.__dict__ for task in self.tasks], file)

    def load_tasks(self):
        try:
            with open("tasks.json", "r") as file:
                tasks_data = json.load(file)
                for task_data in tasks_data:
                    self.tasks.append(Task(**task_data))
        except FileNotFoundError:
            pass

    def add_task(self, description, due_date=None):
        task = Task(description, due_date)
        self.tasks.append(task)
        self.save_tasks()
        print(f"Task '{description}' added!")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            print("Tasks:")
            for index, task in enumerate(self.tasks):
                status = "completed" if task.completed else "not completed"
                due_date = f"Due: {task.due_date}" if task.due_date else ""
                print(f"{index + 1}. {task.description} ({status}) {due_date}")

    def mark_task_complete(self, task_index):
        try:
            self.tasks[task_index].completed = True
            self.save_tasks()
            print(f"Task '{self.tasks[task_index].description}' marked as completed.")
        except IndexError:
            print("Invalid task index.")

    def delete_task(self, task_index):
        try:
            del self.tasks[task_index]
            self.save_tasks()
            print("Task deleted successfully.")
        except IndexError:
            print("Invalid task index.")

    def update_task_description(self, task_index, new_description):
        try:
            self.tasks[task_index].description = new_description
            self.save_tasks()
            print("Task description updated successfully.")
        except IndexError:
            print("Invalid task index.")

def main():
    task_manager = TaskManager()

    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Update Task Description")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Enter task description: ")
            due_date = input("Enter due date (or leave blank): ")
            task_manager.add_task(description, due_date if due_date else None)
        elif choice == '2':
            task_manager.list_tasks()
        elif choice == '3':
            try:
                task_index = int(input("Enter the task index to mark as complete: "))
                task_manager.mark_task_complete(task_index - 1)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            try:
                task_index = int(input("Enter the task index to delete: "))
                task_manager.delete_task(task_index - 1)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '5':
            try:
                task_index = int(input("Enter the task index to update: "))
                new_description = input("Enter the new description: ")
                task_manager.update_task_description(task_index - 1, new_description)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

6