"""The main script for this project.  Run this in order to use the tasktracker."""

import os
import tmods

# get current directory & directory of messages
cwd = os.getcwd()
msg_dir = os.path.join(cwd, "uimsg")

# dictionary of paths to messages
messages = {
    "welcome": os.path.join(msg_dir, "welcome.txt"),
    "help": os.path.join(msg_dir, "help.txt")
}

# print welcome message
welcome = open(messages["welcome"], "r")
print(welcome.read())
welcome.close()

while True:
    cmd = input("\nEnter a command: ")

    match cmd:
        case "quit":
            break

        case "help":
            # print help message
            help = open(messages["help"], "r")
            print(help.read())
            help.close()

        case "about":
            print("insert something here")

        case "license":
            # print license message
            print("\n")
            license = open(os.path.join(cwd, "LICENSE.txt"))
            print(license.read())
            license.close()
            
        case _:
            print(cmd + " is not a recognized command, or I may not have implemented it yet.\nEnter\"help\" for the list of commands.")

    # TODO - add the other cmds
    # TODO - show output
    # TODO - clear the screen