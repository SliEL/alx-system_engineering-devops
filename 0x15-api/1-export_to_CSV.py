#!/usr/bin/python3
"""
A Script that, uses a REST API, for a given employee ID, returns
information about his TO-DO list progress
exporting data in the CSV format.
"""

import requests, json, csv
from sys import argv


if __name__ == "__main__":

    Req = requests.Session()

    idEmp = argv[1]
    idURL = f'https://jsonplaceholder.typicode.com/users/{idEmp}/todos'
    nameURL = f'https://jsonplaceholder.typicode.com/users/{idEmp}'

    employee = Req.get(idURL)
    employeeName = Req.get(nameURL)

    json_req = employee.json()
    usr = employeeName.json()['username']

    totalTasks = 0

    for done_tasks in json_req:
        if done_tasks['completed']:
            totalTasks += 1

    fileCSV = idEmp + '.csv'

    with open(fileCSV, "w", newline='') as csvfile:
        write = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
        for i in json_req:
            write.writerow([idEmp, usr, i.get('completed'), i.get('title')])