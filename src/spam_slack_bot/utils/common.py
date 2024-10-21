import yaml
from box.exceptions import BoxValueError
import os
from spam_slack_bot import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
import json
@ensure_annotations
def readYaml(yaml_path:Path)->ConfigBox:
    try:
        with open(yaml_path) as yaml_file:
            contents=yaml.safe_load(yaml_file)
            logger.info(f"{yaml_path} read successfully")
            return ConfigBox(contents)
    except BoxValueError:
        raise ValueError("yaml is empty")
    except Exception as e:
        raise e
    

@ensure_annotations   
def create_dir(Path_to_dirs:list,Verbose=True):
    for f in Path_to_dirs:
        os.makedirs(f,exist_ok=True)
        if Verbose:
            logger.info(f"created directory at {f}")

@ensure_annotations
def save_json(file_path:Path,data:dict):
    with open(file_path,'w') as f:
        json.dump(data,f,indent=4)
    
    logger.info(f"json file saved at {file_path}")

@ensure_annotations
def load_json(file_path:Path):
    with open(file_path) as f:
        contents=json.load(f)
    logger.info(f"loaded the json file at {file_path}")
    return ConfigBox(contents)

        