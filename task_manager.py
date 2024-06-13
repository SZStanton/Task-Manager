
# So it begins :3
# And I'm back!
# Please review this as soon as possible, I would really like to earnestly finish the Bootcamp!
# It is challenging to find time between work.
# Also I am not sure if you are looking for Pseudo Code for this task, so I've omitted it.



#=====importing libraries=====

import datetime
import time



#=====Login Section=====

container = ""

with open('user.txt', 'r') as file:
    for line in file:
        container += line

container = container.split("\n")
# Copies text from user.txt file into a variable.
# Then turns the variable into a list, separated from the new lines.
# Creates the dictionary containing Username - Password pairs.


valid_user_pass_pairs = {}

for pair in container:
    key, value = pair.split(', ')
    valid_user_pass_pairs[key] = value
# Shows valid Key-value pairs in the dictionary.


while True:
    username = input("Please enter your username: ")
    if username in valid_user_pass_pairs:
    # Checks if valid Key/username.
        password = input("Please enter your password: ")
        if valid_user_pass_pairs[username] == password:
        # Checks if password used, matches the username's password.
            print(f"\n\nLogin Successful.\nWelcome {username}.\n\n")
            break
        else:
            print("\nThe password is incorrect.\n")
    else:
        print("\nThe username is incorrect.\n")



#=====Menu Section=====

# If login was successful.
while True:
    # Present the menu to the user and convert input to lower case.
    if username == "admin":
    # admin check for Statistics option.
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


    if menu == 'st':
    # Check total tasks and users in the database / files.
        if username == "admin":
        # Checks if user is 'admin'.

            tasks_read = ""
            with open('tasks.txt', 'r') as task_file:
                for line in task_file:
                    tasks_read += line
            total_tasks = tasks_read.split("\n")
            # Copies text from tasks.txt file into a variable.
            # Then turns the variable into a list, separated from the new lines.

            users_read = ""
            with open('user.txt', 'r') as user_file:
                for line in user_file:
                    users_read += line
            total_users = users_read.split("\n")
            # Copies text from user.txt file into a variable.
            # Then turns the variable into a list, separated from the new lines.

            print(f"""

The Total Tasks:    {len(total_tasks)}
The Total Users:    {len(total_users)}
""")

        else:
            print("\nYou have entered an invalid input. Please try again\n\n")
            # Loops back to main menu if user is not 'admin'.


    elif menu == 'r':
    # Register a new username with password.
        if username == "admin":
        # Checks if user is admin.

            new_username = input("\nPlease provide the username: ")
            while True:
                new_password = input("Please provide the password: ")
                pass_confirm = input("Please confirm the new password: ")
                if new_password == pass_confirm:
                    user_file = open("user.txt","a")
                    user_file.write(f"\n{new_username}, {new_password}")
                    user_file.close()
                    # If 'password' matches the 'password confirm', then user and their password is added to user.txt
                    print(f"\nUser {new_username} has been added successfully!\n")
                    break
                    # Exits loop.
                else:
                    print("The password does not match.")
                    # Loops back to asks for the 'password' and to confirm 'password'.
        else:
            print("\nYou don't have access!\n\n")
            # Loops back to main menu if user is not 'admin'.


    elif menu == 'a':
    # Add a new task to assign to an agent with a deadline.
        task_user = input("\nPlease confirm who this task should be given too: ")
        task_title = input("Please provide the title of the task: ")
        task_desc = input("Provide a description for the task: ")
        task_due = input("Please provide the due date in d/m/y format: ")
        current_date = datetime.date.today()
        formatted_date = current_date.strftime("%d %b %Y")
        task_complete = "No"
        tasks_file = open("tasks.txt","a")
        tasks_file.write(f"\n{task_user}, {task_title}, {task_desc}, {formatted_date}, {task_due}, {task_complete}")
        tasks_file.close()
        # Requests various information and then writes it into tasks.txt in a specific order and closes file.
        print(f"\nTask {task_title} for {task_user} due on {task_due} has been added successfully!\n")


    elif menu == 'va':
    # Shows all tasks available for all users.
        tasks_read = ""
        with open('tasks.txt', 'r') as task_file:
            for line in task_file:
                tasks_read += line
        all_tasks = tasks_read.split("\n")
        # Copies text from tasks.txt file into a variable.
        # Then turns the variable into a list, separated from the new lines.

        for task_data in all_tasks:
            task_info = task_data.split(", ")
            # Further splits the created list into a list, separated from the ", ".
            # Set as a for loop to display all the tasks available.
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
# User-Friendly layout with specific index used to match the file/list order.


    elif menu == 'vm':
    # Shows the user's task that logged in.
        tasks_read = ""
        with open('tasks.txt', 'r') as task_file:
            for line in task_file:
                tasks_read += line
        all_tasks = tasks_read.split("\n")
        # Copies text from tasks.txt file into a variable.
        # Then turns the variable into a list, separated from the new lines.

        username_found = False  
        # Flag to track if tasks for the username are found - had to use ChatGPT to learn this code line and about flags.

        for task_data in all_tasks:
            task_info = task_data.split(", ")
            # Further splits the created list into a list, separated from the ", ".
            if task_info[0] == username:
            # Does a check to match the info provided to the username given.
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
                # Set flag to True if tasks are found for the username - had to use ChatGPT to learn this code line and about flags.
        if not username_found:
            print("\nYou have no tasks!\n\n")
            # If no tasks show for the logged in user, then exit loop and inform user.


    elif menu == 'e':
    # Exits program.
        print(f'\n\nHave a good day {username}.\nGoodbye! :)\n\n')
        time.sleep(2)
        # Short delay before exit/closing program.
        exit()


    else:
    # Checks for all invalid inputs.
        print("\nYou have provided an invalid input. Please try again\n\n")
        # Loops back to main menu.

