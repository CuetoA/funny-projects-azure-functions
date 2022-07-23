import time
import logging
import azure.functions as func

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
    return current_time
    

# if __name__ == "__main__":
#     resul = changeName("test-storage/aaaaaaa.png")
#     print( resul )