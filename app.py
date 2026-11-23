import csv

tasks = []

def add_one_task(title):
    tasks.append(title)

def print_list():
    for number, task in enumerate(tasks, start=1):
        print(f"{number}. {task}")

def delete_task(number_to_delete):
    try:
        number_to_delete = int(number_to_delete)
    except (TypeError, ValueError):
        print("Invalid task number")
        return

    index = number_to_delete - 1

    if 0 <= index < len(tasks):
        tasks.pop(index)
    else:
        print("Invalid task number")


def save_todos():
    with open("todos.csv", "w", newline="") as file:
        writer = csv.writer(file)
        for task in tasks:
            writer.writerow([task])


def load_todos():
    tasks.clear()

    try:
        with open("todos.csv", "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    tasks.append(row[0])
    except FileNotFoundError:
        return


def run_menu():
    while True:
        print("\nTodo List")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Delete a task")
        print("4. Save tasks")
        print("5. Load tasks")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter the task: ")
            add_one_task(title)
        elif choice == "2":
            print_list()
        elif choice == "3":
            number = input("Enter the task number to delete: ")
            delete_task(number)
        elif choice == "4":
            save_todos()
            print("Tasks saved.")
        elif choice == "5":
            load_todos()
            print("Tasks loaded.")
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1 through 6.")


if __name__ == "__main__":
    run_menu()