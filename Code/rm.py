import requests
import sys

api_key = "31d045e904a01dedc75b2091bcc62e688bb270fb"

project_names = []
task_names = []
projects = requests.get("https://api.todoist.com/rest/v1/projects", headers={"Authorization": "Bearer %s" % api_key}).json()
tasks = requests.get("https://api.todoist.com/rest/v1/tasks", headers={"Authorization": "Bearer %s" % api_key}).json()

for x in range(len(projects)):
    project_names.append(projects[x]["name"])

for x in range(len(tasks)):
    task_names.append(tasks[x]["content"])    

def exitProgram(type_name, name):
    print("There is no " + type_name + " called " + name + "!")
    print("Terminating program...")
    sys.exit()

def remove_task(task_name):
        
    if task_name in task_names:
        
        requests.delete("https://api.todoist.com/rest/v1/tasks/" + str(tasks[task_names.index(task_name)]["id"]), headers={"Authorization": "Bearer %s" % api_key})

    else:
        exitProgram("task", task_name)   

def remove_project(project_name):
    
    if project_name in project_names:
        
        requests.delete("https://api.todoist.com/rest/v1/projects/" + str(projects[project_names.index(project_name)]["id"]), headers={"Authorization": "Bearer %s" % api_key})
    
    else:
        exitProgram("project", project_name)

    