import os
import pytz
import logging
import azure.functions as func
from datetime import datetime, timezone


def main(myblob: func.InputStream):
    new_name = changeName(myblob.name)
    
    try:       new_file = createFileTest(blob_name)
    except:    new_file = "something didn't work"
    
    logging.info(f"Python blob trigger function processed blob \n"
                 f"Name: {myblob.name}\n"
                 f"Blob Size: {myblob.length} bytes\n"
                 )


    logging.info(f"=====DATA=====\n"
                 f"New name created: {new_name}\n"
                 f"Created new txt file: {new_file}\n"
    )


def createFileTest(blob_name):
    new_name = getNewFileName(blob_name)

    with open(new_name, 'w') as fp:
        pass
    return new_name
    

def getNewFileName(blob_name):
    new_name = getNewName(blob_name);
    splitted = new_name.split("/")
    folder = splitted[0]
    name, extention = splitted[-1].split(".")

    new_file_name = f"{folder}/{name}.txt"
    splitted[-1] = new_file_name
    new_path = "/".join(splitted)
    return new_path


def changeName(blob_name):
    new_name = getNewName(blob_name)
    return new_name


def getNewName(blob_name):
    splitted = str(blob_name).split("/")
    file_name, file_ext = splitted[-1].split(".")

    time = getTime()
    splitted[-1] = f"processed_at_{time}.{file_ext}"
    new_name = '/'.join(splitted)
    return new_name


def getTime():
    tz = pytz.timezone('America/Mexico_City')
    cdmx_time = str(datetime.now(tz)).split('.')[0]
    # print(f"cdmx time is {cdmx_time}\n")

    return cdmx_time
    

if __name__ == "__main__":
    #blob_name = "test-storage/aaaaaaa.png"
    blob_name = "/home/cuetorra/Pictures/aaaaaaa.png"
    resul = createFileTest(blob_name)
    print( resul )