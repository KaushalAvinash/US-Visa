import logging
import os

from from_root import from_root
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

log_dir = 'logs'

logs_path = os.path.join(from_root(), log_dir, LOG_FILE)

os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(
    filename=logs_path,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)

#import logging
#import os
#from datetime import datetime

#LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

#logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
#os.makedirs(logs_path,exist_ok=True)

#LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

#logging.basicConfig(
    #filename=LOG_FILE_PATH,
    #format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    #level=logging.INFO,)