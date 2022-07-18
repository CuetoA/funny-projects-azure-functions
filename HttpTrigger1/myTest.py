import json
import keys
#from . import keys
from twilio.rest import Client

client = Client(keys.account_sid, keys.auth_token)

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
    name, phone, msg_id = unpackJson(data)
    message = secret_messages[msg_id](name) if msg_id in secret_messages else "error"

    try:
        twilio_msg = client.messages.create(
            body=message,
            from_=keys.twilio_number,
            to = "+" + phone
        )
        print(f'from:{keys.twilio_number}  type of from: {type(keys.twilio_number)} \n to: {phone} type of phone: {type(phone)}')
    except Exception as e:
        message += f"---Got error {e}---"
    #message += " --bandera activada--"

    return message


def unpackJson(data):
    json_object = json.loads(data)
    name = json_object["name"] if "name" in json_object else None
    phone = json_object["phone"] if "phone" in json_object else None
    secret_msg_id = int(json_object["msg"]) if "msg" in json_object else None
    return name, phone, secret_msg_id


if __name__ == "__main__":
    data = '{"name": "Andrés", "phone": "+525585311908", "msg": 2}'
    data2 = '{"name2": "Scarlette", "phone": "16479074852", "msg": 3}'
    data3 = '{"name2": "chompi 1", "phone": "+525580883029", "msg": 5}'
    print(sendingWhatsapp(data3))