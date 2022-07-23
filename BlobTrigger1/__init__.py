import time
import pytz
import logging
import azure.functions as func
from datetime import datetime, timezone


def main(myblob: func.InputStream):
    new_name = changeName(myblob.name)
    
    logging.info(f"Python blob trigger function processed blob \n"
                 f"Name: {myblob.name}\n"
                 f"Blob Size: {myblob.length} bytes\n"
                 f"New name created: {new_name}\n")
    

def changeName(blob_name):
    splitted = str(blob_name).split("/")
    file_name, file_ext = splitted[-1].split(".")

    time = getTime()
    splitted[-1] = f"processed_at_{time}.{file_ext}"
    new_name = '/'.join(splitted)
    return new_name


def getTime():
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S_%d-%m-%G", t)

    utc_dt = datetime.now(timezone.utc)
    tz = pytz.timezone('America/Mexico_City')
    cdmx_time = str(datetime.now(tz)).split('.')[0]
    # print(f"cdmx time is {cdmx_time}\n")

    return cdmx_time
    

# if __name__ == "__main__":
#     resul = changeName("test-storage/aaaaaaa.png")
#     print( resul )