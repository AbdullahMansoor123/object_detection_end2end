import os
import sys
# import zipfile
# import gdown
import shutil
# import yaml
# from utils import *
from object_detection.logger import logging
from object_detection.exception import Custom_Exception
from object_detection.entity.config_entity import  ModelTrainerConfig, DataIngestionConfig
from object_detection.entity.artifacts_entity import  ModelTrainerArtifacts


class ModelTrainer:
    def __init__(self, model_trainer_config: ModelTrainerConfig):
        self.model_trainer_config = model_trainer_config

    def initiate_model_trainer(self,)->ModelTrainerArtifacts:
        logging.info("entered initiate_model_trainer method of ModelTrainer class")
        try:
            logging.info("data yaml founded")
            data_yaml = os.path.join(os.getcwd(), DataIngestionConfig.feature_store_file_path+"\data.yaml")
            logging.info("started initiate model training method of ModelTrainer class")
            os.system(f"cd yolov5/ && python train.py --img 320 --batch {self.model_trainer_config.batch_size} --epochs {self.model_trainer_config.no_epochs} --data {data_yaml} --weights {self.model_trainer_config.weight_name} --name yolov5n_results --cache")
            
            shutil.copy("yolov5/runs/yolov5n_results/weights/best.pt yolov5/")
            os.makedirs(self.model_trainer_config.model_trainer_dir, exist_ok=True)
            shutil.copy(f"yolov5/runs/yolov5n_results/weights/best.pt {self.model_trainer_config.model_trainer_dir}")

            os.rmdir("yolov5/runs")

            model_trainer_artifacts = ModelTrainerArtifacts(trained_model_file_path="yolov5/best.pt")
            
            logging.info('Ended model training method of ModelTrainer class')
            logging.info(f"model training artifacts: {model_trainer_artifacts}")

            return model_trainer_artifacts

        except Exception as e:
                raise Custom_Exception(e,sys)

