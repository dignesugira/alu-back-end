#!/usr/bin/python3
"""Display an employee's TODO list progress using a REST API."""
import requests
import sys


if __name__ == "__main__":
    emp_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(emp_id)
    user = requests.get(url).json()

    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        emp_id)
    todos = requests.get(todos_url).json()

    done = [task for task in todos if task.get("completed")]

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(done), len(todos)))
    for task in done:
        print("\t {}".format(task.get("title")))
