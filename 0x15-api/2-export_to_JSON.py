#!/usr/bin/python3
""" script to export data in the JSON format"""
import csv
import requests
from sys import argv
import json


def API_request(argv):
    """ script to export data in the JSON format"""
    todo = "https://jsonplaceholder.typicode.com/todos/?userId=" + str(argv[1])
    users = "https://jsonplaceholder.typicode.com/users/" + str(argv[1])

    responset = requests.get(todo)
    responseu = requests.get(users)
    json_t = responset.json()
    json_u = responseu.json()
    user_id = json_u.get("userId")
    user_name = json_u.get("username")

    with open(str(argv[1])+"."+"json", 'w', newline='') as file:
        dicti = {}
        lista = []
        for element in json_t:
            subdicti = {}
            subdicti["task"] = element.get("title")
            subdicti["completed"] = element.get("completed")
            subdicti["username"] = user_name
            lista += [subdicti]
        dicti[argv[1]] = lista
        print(dicti)
        json.dump(dicti, file)


if __name__ == "__main__":
    API_request(argv)
