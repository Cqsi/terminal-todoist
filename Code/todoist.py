import requests
import sys
import get
import create
import rm
import complete

arguments = []
api_key = "" # put your todoist api key here

for x in range(len(sys.argv)):
    arguments.append(sys.argv[x])

def exitProgram():
    print("You typed the command wrong!")
    print("Terminating program...")
    sys.exit()

def todo():
    if arguments[1] == "get":
        get.get_tasks(api_key)

    elif arguments[1] == "create":
        if arguments[2] == "task":
            create.create_task(arguments[3], arguments[4], api_key)
        elif arguments[2] == "project":
            create.create_project(arguments[3], api_key)
        else:
            exitProgram()

    elif arguments[1] == "remove":
        if arguments[2] == "task":
            rm.remove_task(arguments[3])
        elif arguments[2] == "project":
           rm.remove_project(arguments[3])
        else:
            exitProgram()
    elif arguments[1] == "complete":
        complete.complete_task(arguments[2], api_key)
    else:
        exitProgram()

if __name__ == "__main__":
    todo()
