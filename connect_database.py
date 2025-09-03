import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from logger import logging
from datetime import datetime
from timelog import timetaken

def database_connect():
    try:
        starttime = datetime.now()
        load_dotenv()
        connecting_string = os.getenv('connection_string')
        conn = create_engine(connecting_string)
        timetaken(starttime, 'to connect database')
        logging.info('Database Connected Sucessfully!')
        return conn
    except Exception as e:
        logging.error(f"Found ERROR: {e}")

# Only runs when executed directly, not when imported
if __name__ == "__main__":
    database_connect()
