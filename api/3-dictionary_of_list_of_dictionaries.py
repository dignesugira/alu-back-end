#!/usr/bin/python3
"""Export all employees' TODO lists to a JSON file using a REST API."""
import json
import requests


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"
    users = requests.get("{}/users".format(base_url)).json()

    all_tasks = {}
    for user in users:
        user_id = user.get("id")
        todos = requests.get("{}/todos?userId={}".format(
            base_url, user_id)).json()
        all_tasks[user_id] = []
        for task in todos:
            all_tasks[user_id].append({"username": user.get("username"),
                                       "task": task.get("title"),
                                       "completed": task.get("completed")})

    with open("todo_all_employees.json", "w") as f:
        json.dump(all_tasks, f)
