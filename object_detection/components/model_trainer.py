import os
import sys
import zipfile
import gdown
import shutil
import yaml
from utils import *
from object_detection.logger import logging
from object_detection.exception import Custom_Exception
from object_detection.entity.config_entity import  ModelTrainerConfig
from object_detection.entity.artifacts_entity import  ModelTrainerArtifacts


class ModelTrainer:
    def __init__(self, model_trainer_config: ModelTrainerConfig):
        self.model_trainer_config = model_trainer_config

    def initiate_model_trainer(self,)->ModelTrainerArtifacts:
        logging.info("entered initiate_model_trainer method of ModelTrainer class")
        try:
            

        except Exception as e:
                raise Custom_Exception(e,sys)

