#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TO-DO list progress.
"""

import requests
import json
from sys import argv


if __name__ == "__main__":
    Req = requests.Session()

    idEmp = argv[1]
    idURL = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(idEmp)
    nameURL = 'https://jsonplaceholder.typicode.com/users/{}'.format(idEmp)

    employee = Req.get(idURL)
    employeeName = Req.get(nameURL)

    json_req = employee.json()
    name = employeeName.json()['name']

    totalTasks = 0

    for done_tasks in json_req:
        if done_tasks['completed']:
            totalTasks += 1

    print("Employee {} is done with tasks({}/{}):".
          format(name, totalTasks, len(json_req)))

    for done_tasks in json_req:
        if done_tasks['completed']:
            print("     " + done_tasks.get('title'))
