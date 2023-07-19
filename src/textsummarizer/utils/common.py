import os 
from box.exceptions import BoxValueError
import yaml
from textsummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yamL:Path) -> ConfigBox:

    try:
        with open(path_to_yamL) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(F"yaml file: {path_to_yamL} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("Yaml file is empty")
    except Exception as e:
        raise e
    
