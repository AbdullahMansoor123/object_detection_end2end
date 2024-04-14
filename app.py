from object_detection.logger import logging
from object_detection.exception import Custom_Exception
import os, sys

def app():
    try:
        raise Exception("welcome to my custom log")
    except Exception as e:
        abc= Custom_Exception(e, sys)
        logging.info(abc)

if __name__ == "__main__":
    app()
