#!/usr/bin/python3
"""for api"""
import requests
import sys


def get_employee_tasks(employeeId):
    """for api"""
    # variables
    name = ''
    task_list = []
    completed_counter = 0

    # do the get requests
    usersRes = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(employeeId))
    todosRes = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}/todos".
        format(employeeId))
#    print("userRes: {}\n".format(userRes))
#    print("todoRes: {}\n".format(todoRes))

    # get the json from responses
    name = usersRes.json().get('name')
    # print('name: {}'.format(name))
    todosJson = todosRes.json()
    # save the employee Name

    # loop the tasks
    for task in todosJson:
        # up the counter if completed
        if task.get('completed') is True:
            completed_counter += 1
            # save the task title to task_list
            task_list.append(task.get('title'))
    # print('task: {}'.format(task_list)

    # print first line
    print('Employee {} is done with task({}/{}):'.format(
        name, completed_counter, len(todosJson)))
    # loop the task_list and print tasks
    for title in task_list:
        print('\t {}'.format(title))
    return 0

if __name__ == '__main__':
    get_employee_tasks(sys.argv[1])

# NOTES
# use sys to get input from teh terminal
# need to use at the API provided
# - name, # tasks done and not, task title
# tab and space
# look at requests module
