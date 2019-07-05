import requests

api_key = "" # put your todoist api key here

def get_tasks():
    projects = requests.get("https://beta.todoist.com/API/v8/projects", headers={"Authorization": "Bearer %s" % api_key}).json()

    for x in range(len(projects)):
        print(projects[x]["name"])
        for y in range(len(projects[x]["name"])):
            print("-", end="")
        print()
        current_id = projects[x]["id"]

        tasks = requests.get("https://beta.todoist.com/API/v8/tasks", params={"project_id": current_id}, headers={"Authorization": "Bearer %s" % api_key}).json()
    
        for y in range(len(tasks)):
            print(tasks[y]["content"])
    
        print()
