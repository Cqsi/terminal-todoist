import requests
import sys
import get
import create
import rm
import complete
import printhelp

arguments = []
api_key = "" # run "todo api <your Todoist api-key>" or put it manually here

for x in range(len(sys.argv)):
    arguments.append(sys.argv[x])

def exitProgram():
    print("You typed the command wrong!")
    print("Terminating program...")
    sys.exit()

def todo():
    if arguments[1] == "api":
        api_key = arguments[2]
    elif:
        if api_key != "":

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
            elif arguments[1] == "help":
                printhelp.print_help()
            else:
                exitProgram()
        else:
            print("""You haven't input your API-key yet. 
            To do that, run \"todo api <your API-key>\". 
            
            If "todo api" somehow doesn't work you can also manually put it in the todoist.py file, but I highly recommend the first method if it works. 
            """)


if __name__ == "__main__":
    todo()
