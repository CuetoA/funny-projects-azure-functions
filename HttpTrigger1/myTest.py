import json

secret_messages ={
    1: lambda name: f"Hola {str(name).capitalize()} quiero que sepas que te tqm.",
    2: lambda name: f"Según Google el nombre \"{name}\" es de personas guapas.",
    3: lambda name: f"Te deseo que tengas una excelente semana {name}",
    4: lambda name: f"Tu nombre al revés es {str(name)[::-1].capitalize()}",
    5: lambda name: f"{str(name).capitalize()}, la revolución de los bots de whatsapp empezó",
}



def helloAzure(name):
    message = f"{name} says hello Azure"
    return message


def gettingData(data):
    json_object = json.loads(data)
    name = json_object["name"] if json_object["name"] else None
    number = json_object["number"] if json_object["number"] else None
    message = f" your name is {name} and your number is {number}"
    return message


def sendingWhatsapp(data):
    name, phone, secret_msg_id = unpackJson(data)
    message = secret_messages[secret_msg_id](name) if secret_msg_id in secret_messages else "error"
    return message


def unpackJson(data):
    json_object = json.loads(data)
    name = json_object["name"] if "name" in json_object else None
    phone = json_object["phone"] if "phone" in json_object else None
    secret_msg_id = int(json_object["secret_msg_id"]) if "secret_msg_id" in json_object else None
    return name, phone, secret_msg_id


if __name__ == "__main__":
    data = '{"name": "Scarlette", "phone": "+525585311908", "secret_msg_id": 5}'
    data2 = '{"name2": "Scarlette", "phone2": "+525585311908", "secret_msg_id": 5}'
    print(sendingWhatsapp(data2))