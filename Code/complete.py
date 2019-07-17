import requests

def complete_task(task_name, api_key):

    tasks = requests.get("https://beta.todoist.com/API/v8/tasks", headers={"Authorization": "Bearer %s" % api_key}).json()

    for x in range(len(tasks)):
        if tasks[x]["content"] == task_name:
            task_id = tasks[x]["id"]

    requests.post("https://beta.todoist.com/API/v8/tasks/" + task_id + "/close", headers={"Authorization": "Bearer %s" % api_key})

    print("Finished the task " + task_name + "! Congrats!")