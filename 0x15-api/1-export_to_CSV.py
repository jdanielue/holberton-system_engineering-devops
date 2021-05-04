#!/usr/bin/python3
""" script to export data in the CSV format"""
import csv
import requests
from sys import argv


def API_request(argv):
    """ script to export data in the CSV format"""
    todo = "https://jsonplaceholder.typicode.com/todos/?userId=" + str(argv[1])
    users = "https://jsonplaceholder.typicode.com/users/" + str(argv[1])

    responset = requests.get(todo)
    responseu = requests.get(users)
    json_t = responset.json()
    json_u = responseu.json()
    user_name = json_u.get("username")

    with open(str(argv[1])+"."+"csv", 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for count in json_t:
            writer.writerow([argv[1], user_name,
                             count.get('completed'), count.get('title')])


if __name__ == "__main__":
    API_request(argv)
