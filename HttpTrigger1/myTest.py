import json

def helloAzure(name):
    message = f"{name} says hello Azure"
    return message

def gettingData(data):
    json_object = json.loads(data)
    name = json_object["name"] if json_object["name"] else None
    number = json_object["number"] if json_object["number"] else None
    message = f" your name is {name} and your number is {number}"
    return message
