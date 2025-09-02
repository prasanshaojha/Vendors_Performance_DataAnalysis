import logging
import os 
from datetime import datetime 

log_folder_path  = r"C:\Users\ojhap\Documents\PRACTICE\InventoryDataAnalysis\logs"

os.makedirs(log_folder_path, exist_ok= True)

today = datetime.now().strftime("%y-%m-%d")
log_path = os.path.join(log_folder_path, f"logfile{today}.log")

logging.basicConfig(
    filename= log_path,
    level= logging.DEBUG,
    format= '%(asctime)s - %(levelname)s - %(message)s',
    filemode= 'a'
)