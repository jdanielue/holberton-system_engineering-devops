#!/usr/bin/python3
import requests
from sys import argv
import json
import csv


def API_request(argv):
    todo = "https://jsonplaceholder.typicode.com/todos/?userId=" + str(argv[1])
    users = "https://jsonplaceholder.typicode.com/users/" + str(argv[1])

    responset = requests.get(todo)
    responseu = requests.get(users)
    json_t = responset.json()
    json_u = responseu.json()
    user_name = json_u.get("username")

    with open(str(argv[1])+"."+"csv", 'w', newline='') as file:
        writer = csv.writer(file)
        for count in json_t:
            writer.writerow([str(argv[1]), str(user_name), str(count['completed']), str(count['title'])])


if __name__ == "__main__":
    API_request(argv)