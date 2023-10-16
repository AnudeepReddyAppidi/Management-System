class Task:
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        print(f"Task '{description}' added!")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            print("Tasks:")
            for index, task in enumerate(self.tasks):
                status = "completed" if task.completed else "not completed"
                print(f"{index + 1}. {task.description} ({status})")

    # 40% of features implemented: Marking tasks as complete
    def mark_task_complete(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].completed = True
            print(f"Task '{self.tasks[task_index].description}' marked as completed.")
        else:
            print("Invalid task index.")

def main():
    task_manager = TaskManager()

    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Complete")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Enter task description: ")
            task_manager.add_task(description)
        elif choice == '2':
            task_manager.list_tasks()
        elif choice == '3':
            task_index = int(input("Enter the task index to mark as complete: "))
            task_manager.mark_task_complete(task_index - 1)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
