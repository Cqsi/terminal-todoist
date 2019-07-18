import requests

def get_tasks(api_key):
    projects = requests.get("https://api.todoist.com/rest/v1/projects", headers={"Authorization": "Bearer %s" % api_key}).json()

    for x in range(len(projects)):
        print(projects[x]["name"])
        for y in range(len(projects[x]["name"])):
            print("-", end="")
        print()
        current_id = projects[x]["id"]

        tasks = requests.get("https://api.todoist.com/rest/v1/tasks", params={"project_id": current_id}, headers={"Authorization": "Bearer %s" % api_key}).json()
    
        for y in range(len(tasks)):
            print(tasks[y]["content"])
    
        print()
