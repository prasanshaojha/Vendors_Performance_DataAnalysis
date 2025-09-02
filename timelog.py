from datetime import datetime
from logger import logging

def timetaken (starttime,message):
    duration = datetime.now() -  starttime 
    minutes = duration / 60
    logging.info(f"Time Taken for {message} : {minutes} min ")
    return duration


if __name__ == '__main__':
    starttime = datetime.now()
    timetaken(starttime,"testing this function")