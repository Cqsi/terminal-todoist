import uuid
import requests
import json

def create_task(task_name, project_name, api_key):

    projects = requests.get("https://beta.todoist.com/API/v8/projects", headers={"Authorization": "Bearer %s" % api_key}).json()
    project_names = []

    for x in range(len(projects)):
        project_names.append(projects[x]["name"])
    
    if project_name in project_names:
        
        requests.post("https://api.todoist.com/rest/v1/tasks",
        data=json.dumps({"content": task_name, "project_id": projects[project_names.index(project_name)]["id"]}),
        headers={"Content-Type": "application/json", "X-Request-Id": str(uuid.uuid4()),"Authorization": "Bearer %s" % api_key}).json()
    
    else:
        print("There is no project called " + project_name + "!")
        print("Terminating program...")
        sys.exit()

def create_project(project_name, api_key):

    requests.post("https://api.todoist.com/rest/v1/projects",
    data=json.dumps({"name": project_name}),
    headers={"Content-Type": "application/json", "X-Request-Id": str(uuid.uuid4()), "Authorization": "Bearer %s" % api_key}).json()