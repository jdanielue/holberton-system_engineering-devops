#!/usr/bin/python3
""" script to request data in using an API"""
import requests
from sys import argv

def API_request(argv):
    """ script to request data in using an API"""
    tod = "https://jsonplaceholder.typicode.com/todos/?userId=" + str(argv[1])
    users = "https://jsonplaceholder.typicode.com/users/" + str(argv[1])

    responset = requests.get(tod)
    responseu = requests.get(users)
    json_t = responset.json()
    json_u = responseu.json()
    user_name = json_u.get("name")
    var1 = 0
    var2 = 0
    list1 = []
    for tasks in json_t:
        var1 += 1
        if tasks['completed'] is True:
            list1 += [tasks['title']]
            var2 += 1
    print("Employee {} is done with tasks({}/{}):".format(user_name, var2, var1))

    for count in list1:
        print('\t{}'.format(count))

if __name__ == "__main__":
    API_request(argv)
