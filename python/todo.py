import argparse
import os

TASK_FILE = ".tasks.txt"

def add_task(task):
    """Function: add_task
    
    Input - a task to add to the list
    Return - nothing
    """
    with open(TASK_FILE, "a") as file:
        file.write(task + "\n")
        print(f"Task '{task}' added.")

def list_tasks():
    """Read tasks from task file and return them as a list"""
    if not os.path.exists(TASK_FILE):
        print("No tasks found yet.")

    with open(TASK_FILE, "r") as file:
        lines = [line.strip() for line in file.readlines() if line.strip()]
       
        if not lines:
            print("No tasks found.")
        
        numbered_tasks = [f"{idx + 1}. {line}" for idx, line in enumerate(lines)]
        return "\n".join(numbered_tasks)


def remove_task(index):
    return

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
