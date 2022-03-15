import os
import json
CWD = os.path.dirname(__file__)

def menu():
    print("1. Create user")
    print("2. Log in")
    print("3. Change password")
    print("Q. Quit")

def read_json(json_file):
    with open(f"{CWD}/{json_file}", encoding="utf8") as file:
        return json.load(file)

def create_user(users, json_file):
    with open(f"{CWD}/{json_file}", "w", encoding="utf8") as file:
        json.dump(users, file, ensure_ascii=False, indent=4)
        