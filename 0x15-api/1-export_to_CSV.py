#!/usr/bin/python3
"""for api"""
import csv
import requests
import sys


def save_tasks_to_csv(employeeId):
    """for api"""
    # variables
    username = ''
    allTasks = []

    # do the get requests
    usersRes = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(employeeId))
    todosRes = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}/todos".
        format(employeeId))

    # get the json from responses
    username = usersRes.json().get('username')
    todosJson = todosRes.json()

    # loop through and save
    for task in todosJson:
        taskRow = []
        taskRow.append(employeeId)
        taskRow.append(username)
        taskRow.append(task.get('completed'))
        taskRow.append(task.get('title'))
        allTasks.append(taskRow)

    with open("{}.csv".format(employeeId), 'w') as csvFile:
        csvwriter = csv.writer(csvFile, quoting=csv.QUOTE_ALL)
        csvwriter.writerows(allTasks)
    return 0

if __name__ == '__main__':
    save_tasks_to_csv(sys.argv[1])
