import argparse
import os

TASK_FILE = ".tasks.txt"

def add_task(task):
    """Add new task to task file"""
    with open(TASK_FILE, "a") as file:
        file.write(task + "\n")
        print(f"Task '{task}' added.")

def list_tasks():
    """Read tasks from task file and return them as a numbered list"""
    if not os.path.exists(TASK_FILE):
        print("No tasks found yet.")

    with open(TASK_FILE, "r") as file:
        lines = [line.strip() for line in file.readlines() if line.strip()]
       
        if not lines:
            print("No tasks found.")
        
        # Create numbered list of tasks
        numbered_tasks = [f"{idx + 1}. {line}" for idx, line in enumerate(lines)]
        return "\n".join(numbered_tasks)

def remove_task(index):
    """Remove a task by its number from the task file."""
    if not os.path.exists(TASK_FILE):
        print("No tasks found yet.")
        return

    # Read all non-empty lines from the file
    with open(TASK_FILE, "r") as file:
        tasks = [line.strip() for line in file if line.strip()]

    if not tasks:
        print("No tasks to remove.")
        return

    # Check for valid input from user
    if index < 1 or index > len(tasks):
        print(f"Invalid task number. Please choose between 1 and {len(tasks)}.")
        return

    # Remove the specified task
    removed = tasks.pop(index - 1)

    # Write remaining tasks back to the file
    if tasks:
        with open(TASK_FILE, "w") as file:
            file.write("\n".join(tasks) + "\n")
        print(f"Task '{removed}' removed successfully.")
        print("Remaining tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        os.remove(TASK_FILE)
        print(f"Task '{removed}' removed. No tasks left – file deleted.")


def main():
    parser = argparse.ArgumentParser(description="Command-line Todo List")
    parser.add_argument(
            "-a",
            "--add",
            help="Add a new task"
            )
    parser.add_argument(
            "-l",
            "--list",
            action="store_true",
            help="List all tasks")
    parser.add_argument(
            "-r",
            "--remove",
            help="Remove a task by index")

    args = parser.parse_args()

    if args.add:
        add_task(args.add)
    elif args.list:
        tasks = list_tasks()
        print(tasks)
    elif args.remove:
        remove_task(int(args.remove))
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
