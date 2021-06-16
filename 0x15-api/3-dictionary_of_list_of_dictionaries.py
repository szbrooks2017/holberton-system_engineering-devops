#!/usr/bin/python3
"""for api"""
import json
import requests
import sys


def save_all_to_json():
    """for api"""
    # variables
    users_and_tasks = {}

    # do the get requests
    users_json = requests.get(
        "https://jsonplaceholder.typicode.com/users/").json()
    todos_json = requests.get(
        "https://jsonplaceholder.typicode.com/todos").json()

    # get the json from responses
    user_info = {}
    for user in users_json:
        user_info[user['id']] = user['username']

    for task in todos_json:
        if users_and_tasks.get(task['userId'], False) is False:
            users_and_tasks[task['userId']] = []
        task_dict = {}
        task_dict['username'] = user_info[task['userId']]
        task_dict['task'] = task['title']
        task_dict['completed'] = task['completed']
        users_and_tasks[task['userId']].append(task_dict)

    with open("todo_all_employees.json", 'w') as jFile:
        json.dump(users_and_tasks, jFile)

if __name__ == '__main__':
    save_all_to_json()
# need all users make dict id: username
# get all todos
# loop the todos
# if the userID in task is not in the dict -> add with []
# create new task dictionary
# append task dict
# put it in the file
