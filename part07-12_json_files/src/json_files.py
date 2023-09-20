# Write your solution here

import json

def print_persons(filename: str):
    with open(filename) as file:
        contents = json.loads(file.read())
        for person in contents:
            print(f"{person['name']} {person['age']} years ({', '.join((person['hobbies']))})")

# print_persons("file1.json")
