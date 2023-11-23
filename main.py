"""The main script for this project.  Run this in order to use the tasktracker."""

import datetime
import os
from tmods import inputver, serialize, tasktrack

# get current directory & directory of messages
cwd = os.getcwd()
msg_dir = os.path.join(cwd, "uimsg")

# dictionary of paths to messages
messages = {
    "welcome": os.path.join(msg_dir, "welcome.txt"),
    "help": os.path.join(msg_dir, "help.txt"),
    "license": os.path.join(cwd, "LICENSE.txt")
}


def clear_screen():
    """Clear the output screen."""

    if os.name == "nt":
        # Windows
        os.system("cls")
    elif os.name == "posix":
        # Mac & Linux
        os.system("clear")


# print welcome message
with open(messages["welcome"], "r") as f:
    print(f.read())

while True:
    cmd = input("\nEnter a command: ")

    match cmd:
        case "quit":
            break

        case "help":
            # print help message
            clear_screen()
            with open(messages["help"], "r") as f:
                print(f.read())

        case "about":
            clear_screen()
            print("insert something here")

        case "license":
            # print license message
            clear_screen()
            with open(messages["license"], "r") as f:
                print(f.read())

        case "new task":
            clear_screen()

            # ask for task name
            name = inputver.valid_input(
                "\nWhat is the name of the task? ",
                16)
            
            # ask for task description
            desc = inputver.valid_input(
                "\nProvide a description of the task: ",
                512
            )

            # TODO: ask for task project
            project = inputver.valid_input(
                "\nWhich project is this task in? "
                # TODO: make sure the project exists
                # TODO: maybe display a list of projects?
            )

            # get current date & ask for task due date
            today = str(datetime.date.today())
            duedate = inputver.input_date(
                "\nWhen is this due? Use the format MM-DD-YYYY",
                "Please use the format MM-DD-YYYY: ")
            
            # actually create the task with the args
            taskdict = tasktrack.create_taskdict(
                name,
                today,
                duedate,
                desc,
                project
            )

            # dump the taskdict into a json in the correct folder.
            serialize.save_task(taskdict,
                                # make the full path to the project directory
                                os.path.join(serialize.TASKS_DIR, project),
                                # add .json extension to the file name
                                name + ".json")
            
        case "new project":
            clear_screen()

            # ask for name
            name = inputver.valid_input(
                "\nWhat is the name of the project? ",
                16)
            
            # ask for description
            desc = inputver.valid_input(
                "\nProvide a description of the project: ",
                512)

            # TODO: attempt to create the directory
            # TODO: return a message if success or fail
            
        case _:
            print("\n")
            print(cmd + " is not a recognized command, or I may not have implemented it yet.\nEnter\"help\" for the list of commands.")

    # TODO - add the other cmds
    # TODO - show output