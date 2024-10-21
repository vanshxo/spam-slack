import os
import sys
import logging
log_str="[%(asctime)s: %(levelname)s:%(module)s:%(message)s]"
log_dir='running_logs'
log_file='logs.log'

log_file_path=os.path.join(log_dir,log_file)

os.makedirs(log_dir,exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=log_str,
    handlers=[
        logging.FileHandler(log_file_path),
        logging.StreamHandler(sys.stdout)
    ]
)

logger=logging.getLogger("info_logger")