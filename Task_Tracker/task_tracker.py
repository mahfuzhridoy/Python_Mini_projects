
import json
import click

def add_task():
    pass

def update_task():
    pass

def delete_task():
    pass

def main():
    print("Choose your option")
    print("1. Add a task")
    print("2. Update a task")
    print("3. Delete a task")
    choice = input("Enter your choice")

    match choice:
        case "1":
            add_task()

        case "2":
            update_task()

        case "3":
            delete_task()

if __name__ == "__main__":
    main()