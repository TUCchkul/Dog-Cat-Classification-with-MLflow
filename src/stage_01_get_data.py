import argparse
import os
import shutil
from tqdm import tqdm
import logging
from src.utils.common import read_yaml, create_directories
import random
import urllib.request as req 


STAGE="GET_DATA"
logging.basicConfig(
    filename=os.path.join("logs",'running_logs.log'),
    level=logging.INFO,
    format="[%(asctime)s: %(levelname)s: %(module)s]: %(message)s",
    filemode="a"
)
def main(config_path):
    config=read_yaml(config_path)
    print(config)
    #params=read_yaml(param_path)

if __name__=="__main__":
    args=argparse.ArgumentParser()
    args.add_argument("--config","-c", default="configs/config.yaml")
    #args.add_argument("--param","-p", default=param.yaml)
    parsed_args=args.parse_args()

    try:
        logging.info("\n********************")
        logging.info(f">>>>>> stage {STAGE} started <<<<<<<")
        main(config_path=parsed_args.config)
        logging.info(f">>>>>> stage {STAGE} completed!<<<<<<<<\n")
    except Exception as e:
        logging.exception(e)
        raise e