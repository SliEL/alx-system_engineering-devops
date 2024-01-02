#!/usr/bin/python3
"""
A sript that, uses a REST API, for a given employee ID, returns
information about his TO-DO list progress
and exports data in the JSON format.
"""

import requests, json
from sys import argv


if __name__ == "__main__":

    Req = requests.Session()

    idEmp = argv[1]
    idURL = f'https://jsonplaceholder.typicode.com/users/{idEmp}/todos'
    nameURL = f'https://jsonplaceholder.typicode.com/users/{idEmp}'

    employee = sessionReq.get(idURL)
    employeeName = sessionReq.get(nameURL)

    json_req = employee.json()
    usr = employeeName.json()['username']

    totalTasks = []
    updateUser = {}

    for all_Emp in json_req:
        totalTasks.append(
            {
                "task": all_Emp.get('title'),
                "completed": all_Emp.get('completed'),
                "username": usr,
            })
    updateUser[idEmp] = totalTasks

    file_Json = idEmp + ".json"
    with open(file_Json, 'w') as f:
        json.dump(updateUser, f)
