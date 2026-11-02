#!/usr/bin/python3
"""Export an employee's TODO list to a CSV file using a REST API."""
import csv
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
    with open("{}.csv".format(emp_id), "w", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([emp_id, username,
                             task.get("completed"), task.get("title")])
