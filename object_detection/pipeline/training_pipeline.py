import os,sys
from object_detection.logger import logging
from object_detection.exception import Custom_Exception
from object_detection.components.data_ingestion import DataIngestion
from object_detection.entity.config_entity import (DataIngestionConfig)
from object_detection.entity.artifacts_entity import (DataIngestionArtifacts)


class TrainingPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
    
    def start_data_ingestion(self) -> DataIngestionArtifacts:
        try:
            logging.info("Enter the start_data_ingestion method of TrainingPipeline class")
            logging.info('getting data from URL')
            
            data_ingestion = DataIngestion(data_ingestion_config = self.data_ingestion_config
                                           )
            data_ingestion_artifacts = data_ingestion.initiate_data_ingestion()
            logging.info('Got the data from URL')
            logging.info("exited the start_data_ingestion method of the TrainPipeline class")

            return data_ingestion_artifacts

        except Exception as e:
            raise Custom_Exception(e,sys)
    
    def run_pipeline(self)->None:
        try:
            data_ingestion_artifacts = self.start_data_ingestion()
            return data_ingestion_artifacts
        except Exception as e:
            raise Custom_Exception(e,sys)
            