# PROJECT 1 — Command-Line Task Manager (with Priorities, Sorting & Search)

# import random
tasks = []


def print_tasks():
    for index, task in enumerate(tasks, start=1):
        print(
            f"{index}. Title : {task['title']} | Priority : {task['priority']} | Status : {task['status']}")


def add_task():
    title = input("Enter Task: ")
    while title == "":
        print("Task cannot be empty!")
        title = input("Enter Task: ")

    priority_level = ["Low", "Medium", "High"]
    priority = input("Set Priority (Low/Medium/High): ").capitalize()

    while priority not in priority_level:
        print("Invalid Priority")
        priority = input("Set Priority (Low/Medium/High): ").capitalize()

    status = input("Status(Completed/ Ongoing / Pending): ").capitalize()
    if status == "":
        status = "Pending"
    else:
        while status not in ['Completed', 'Ongoing', 'Pending']:
            print("Invalid Status")
            status = input("Status(Completed/ Ongoing / Pending): ")
        status = status.capitalize()

    tasks.append({"title": title, "priority": priority, "status": status})


def delete_task():
    if not tasks:
        print("No task to be deleted! ")
        return

    view_tasks()
    index = input("Enter task index to delete: ")
    while not index.isdigit():
        print("Please enter a number")
        index = input("Enter task index to delete: ")

    index = int(index) - 1
    if 0 <= index < len(tasks):
        removed_task = tasks.pop(index)
        print(f"Removed Task : |{removed_task['title']}|")
    else:
        print("Enter index from the shown tasks")


def view_tasks():
    if not tasks:
        print("No task to show")
        return

    print("YOUR TASK")
    # index = 0
    # for index, task in enumerate(tasks, start=1):
    #     title = task['title']
    #     priority = task['priority']
    #     status = task['status']
    #     print(f"{index}. Title : {title} | Priority : {priority} | Status : {status}")
    print_tasks()


def update_task():
    if not tasks:
        print("No task to show")
        return

    view_tasks()
    index = input("Enter task index to update: ")
    while not index.isdigit():
        print("Invalid Index")
        index = input("Enter task index to update: ")

    index = int(index) - 1
    if 0 <= index < len(tasks):
        new_title = input("Enter new title: ")
        if new_title == "":
            new_title = tasks[index]['title']
        new_priority = input(
            "Enter priority of new task: ").strip().capitalize()

        if new_priority == "":
            new_priority = tasks[index]['priority']
        else:
            priority_list = ["Low", "Medium", "High"]
            while new_priority not in priority_list:
                print("Invalid Priority!")
                new_priority = input(
                    "Enter priority of new task: ").strip().capitalize()

        new_status = input(
            "Enter status of the new task: ").strip().capitalize()
        if new_status == "":
            new_status = tasks[index]['status']
        else:
            status_list = ['Completed', 'Ongoing', 'Pending']
            while new_status not in status_list:
                print('Invalid Status!')
                new_status = input(
                    "Enter status of the new task: ").strip().capitalize()
            new_status = new_status.capitalize()

        tasks[index].update(
            {'title': new_title, 'priority': new_priority, 'status': new_status})


def search_task():
    if not tasks:
        print("No task to search")
        return

    search = input("Search: ").lower()
    found_any = False
    print("--Matching Tasks--")
    for index, task in enumerate(tasks, start=1):
        if search in task['title'].lower() or\
                search in task['priority'].lower() or\
                search in task['status'].lower():
            print(
                f"{index}. Title : {task['title']} | Priority : {task['priority']} | Status : {task['status']}")
            found_any = True

    if not found_any:
        print("No matching tasks")


def sort_task():
    method_of_sorting = input(
        "Sort tasks by what? (Priority / Status / Title): ").lower()
    methods = ['priority', 'status', 'title']
    while method_of_sorting not in methods:
        print("Unable to sort that way!")
        method_of_sorting = input(
            "Sort tasks by what? (Priority / Status / Title").lower()

    if method_of_sorting == 'priority':
        priority_order = {'Low': 1, 'Medium': 2, 'High': 3}
        tasks.sort(key=lambda task: priority_order[task['priority']])
        # for index, task in enumerate(tasks, start=1):
        #     print(
        #         f"{index}. Title : {task['title']} | Priority : {task['priority']} | Status : {task['status']}")

    elif method_of_sorting == 'status':
        status_order = {'Completed': 1, 'Ongoing': 2, 'Pending': 3}
        tasks.sort(key=lambda task: status_order[task['status']])
        # for index, task in enumerate(tasks, start=1):
        #     print(
        #         f"{index}. Title : {task['title']} | Priority : {task['priority']} | Status : {task['status']}")

    elif method_of_sorting == 'title':
        tasks.sort(key=lambda task: task['title'].lower())
        # for index, task in enumerate(tasks, start=1):
        #     print(
        #         f"{index}. Title : {task['title']} | Priority : {task['priority']} | Status : {task['status']}")
        # print_tasks()
    print("--Sorted Tasks--")
    print_tasks()


def filter_task():
    filter_by = input(
        "What do you want to filter by (Priority/Status)").strip().capitalize()
    while filter_by != "Priority" and filter_by != "Status":
        print("Invalid!")
        filter_by = input(
            "What do you want to filter by (Priority/Status)").strip().capitalize()

    if filter_by == "Priority":
        priority_list = ["Low", "Medium", "High"]
        priority_filter = input(
            "Filter by (Low/Medium/High): ").strip().capitalize()
        while priority_filter not in priority_list:
            print("Please choose priority from the list!")
            priority_filter = input(
                "Filter by (Low/Medium/High): ").strip().capitalize()
        found = False
        for index, task in enumerate(tasks, start=1):
            if priority_filter == task['priority']:  # i did it right man !!
                print(
                    f"{index}. Title : {task['title']} | Priority : {task['priority']} | Status : {task['status']}")
                found = True
        if not found:
            print("No tasks with this priority!")

    elif filter_by == "Status":
        status_list = ['Completed', 'Ongoing', 'Pending']
        status_filter = input(
            "Filter by (Completed/Ongoing/Pending):  ").strip().capitalize()
        while status_filter not in status_list:
            print("Please choose status from the list")
            status_filter = input(
                "Filter by (Completed/Ongoing/Pending):  ").strip().capitalize()
        found = False
        for index, task in enumerate(tasks, start=1):
            if status_filter == task['status']:
                print(
                    f"{index}. Title : {task['title']} | Priority : {task['priority']} | Status : {task['status']}")
                found = True
        if not found:
            print("No task with this status!")
    else:
        print("Can't filter that way!")


def main():
    print("╭───────────────────────────────────╮")
    print("│         TASK MANAGER APP          |  ")
    print("╰───────────────────────────────────╯")

    is_running = True

    while is_running:
        print()
        print("|1.Add task")
        print("|2.Delete Task")
        print("|3.View Task")
        print("|4.Search Task")
        print("|5.Sort Tasks")
        print("|6.Update Tasks ")
        print("|7.Filter Tasks")
        print("|8.Exit")
        choice = input("What do you want to do: ").strip()
        print()

        if choice == "1":
            add_task()
        elif choice == "2":
            delete_task()
        elif choice == "3":
            view_tasks()
        elif choice == "4":
            search_task()
        elif choice == "5":
            sort_task()
        elif choice == "6":
            update_task()
        elif choice == "7":
            filter_task()
        elif choice == "8":
            print("Exiting app....")
            break
        else:
            print("Invalid Option. Try Again")
    print("Thank You for using!")
    print()
    print("╭──────────────────────╮")
    print("│       GOODBYE!       │")
    print("│   SEE YOU SOON :)    │")
    print("╰──────────────────────╯")


if __name__ == "__main__":
    main()
