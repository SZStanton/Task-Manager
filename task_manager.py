#=====importing libraries=====

import datetime
import time


#=====Login Section=====

print("=" * 55)
print("               Welcome to Task Manager")
print("=" * 55)
print("Default Login")
print("Username: admin")
print("Password: adm1n")
print("-" * 55)
print("Please log in below.\n")


container = ""

with open("user.txt", "r") as file:
    for line in file:
        container += line

container = container.split("\n")

# Creates the dictionary containing Username - Password pairs.
valid_user_pass_pairs = {}

for pair in container:
    if pair.strip() == "":
        continue

    key, value = pair.split(", ", 1)
    valid_user_pass_pairs[key] = value


while True:
    username = input("Please enter your username: ")

    if username in valid_user_pass_pairs:
        password = input("Please enter your password: ")

        if valid_user_pass_pairs[username] == password:
            print(f"\n\nLogin Successful.\nWelcome {username}.\n")
            break

        else:
            print("\nThe password is incorrect.\n")

    else:
        print("\nThe username is incorrect.\n")


#=====Menu Section=====

while True:

    if username == "admin":
        menu = input('''Select one of the following options:
st  - Statistics
r   - register a user
a   - add task
va  - view all tasks
vm  - view my tasks
e   - exit

Selection: ''').lower()

    else:
        menu = input('''Select one of the following options:
r   - register a user
a   - add task
va  - view all tasks
vm  - view my tasks
e   - exit

Selection: ''').lower()


    #=====Statistics=====

    if menu == "st":

        if username == "admin":

            with open("tasks.txt", "r") as task_file:
                total_tasks = [line for line in task_file if line.strip()]

            with open("user.txt", "r") as user_file:
                total_users = [line for line in user_file if line.strip()]

            print(f"""

The Total Tasks:    {len(total_tasks)}
The Total Users:    {len(total_users)}

""")

        else:
            print("\nYou have entered an invalid input.\n")


    #=====Register User=====

    elif menu == "r":

        if username == "admin":

            new_username = input("\nPlease provide the username: ")

            while True:

                if new_username in valid_user_pass_pairs:
                    print("That username already exists.")
                    break

                new_password = input("Please provide the password: ")
                pass_confirm = input("Please confirm the new password: ")

                if new_password == pass_confirm:

                    with open("user.txt", "a") as user_file:
                        user_file.write(f"\n{new_username}, {new_password}")

                    valid_user_pass_pairs[new_username] = new_password

                    print(f"\nUser {new_username} has been added successfully!\n")
                    break

                else:
                    print("The passwords do not match.\n")

        else:
            print("\nYou don't have access!\n")


    #=====Add Task=====

    elif menu == "a":

        task_user = input("\nPlease confirm who this task should be given to: ")
        task_title = input("Please provide the title of the task: ")
        task_desc = input("Provide a description for the task: ")
        task_due = input("Please provide the due date in d/m/y format: ")

        current_date = datetime.date.today()
        formatted_date = current_date.strftime("%d %b %Y")

        task_complete = "No"

        with open("tasks.txt", "a") as tasks_file:
            tasks_file.write(
                f"\n{task_user}, {task_title}, {task_desc}, "
                f"{formatted_date}, {task_due}, {task_complete}"
            )

        print(
            f"\nTask '{task_title}' for {task_user} "
            f"due on {task_due} has been added successfully!\n"
        )


    #=====View All Tasks=====

    elif menu == "va":

        with open("tasks.txt", "r") as task_file:
            all_tasks = task_file.read().split("\n")

        for task_data in all_tasks:

            if task_data.strip() == "":
                continue

            task_info = task_data.split(", ")

            print(f"""
------------------------------------------------------------

Task:               {task_info[1]}
Assigned to:        {task_info[0]}
Date assigned:      {task_info[3]}
Due date:           {task_info[4]}
Task Complete?      {task_info[5]}

Task description:
{task_info[2]}

------------------------------------------------------------
""")


    #=====View My Tasks=====

    elif menu == "vm":

        with open("tasks.txt", "r") as task_file:
            all_tasks = task_file.read().split("\n")

        username_found = False

        for task_data in all_tasks:

            if task_data.strip() == "":
                continue

            task_info = task_data.split(", ")

            if task_info[0] == username:

                print(f"""
------------------------------------------------------------

Task:               {task_info[1]}
Assigned to:        {task_info[0]}
Date assigned:      {task_info[3]}
Due date:           {task_info[4]}
Task Complete?      {task_info[5]}

Task description:
{task_info[2]}

------------------------------------------------------------
""")

                username_found = True

        if not username_found:
            print("\nYou have no tasks!\n")


    #=====Exit=====

    elif menu == "e":

        print(f"\nHave a good day {username}.\nGoodbye! :)\n")
        time.sleep(2)
        exit()


    #=====Invalid Input=====

    else:
        print("\nYou have provided an invalid input. Please try again.\n")