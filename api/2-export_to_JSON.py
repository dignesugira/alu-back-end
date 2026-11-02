#!/usr/bin/python3
"""Export an employee's TODO list to a JSON file using a REST API."""
import json
import requests
import sys


if __name__ == "__main__":
    emp_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(emp_id)
    user = requests.get(url).json()

    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        emp_id)
    todos = requests.get(todos_url).json()

    username = user.get("username")
    tasks = []
    for task in todos:
        tasks.append({"task": task.get("title"),
                      "completed": task.get("completed"),
                      "username": username})

    with open("{}.json".format(emp_id), "w") as f:
        json.dump({emp_id: tasks}, f)
