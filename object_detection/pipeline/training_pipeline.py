import os,sys
from object_detection.logger import logging
from object_detection.exception import Custom_Exception
from object_detection.components.data_ingestion import DataIngestion
from object_detection.components.data_validation import DataValidation
from object_detection.components.model_trainer import ModelTrainer
from object_detection.entity.config_entity import (DataIngestionConfig, DataValidationConfig, ModelTrainerConfig)
from object_detection.entity.artifacts_entity import (DataIngestionArtifacts, DataValidationArtifacts, ModelTrainerArtifacts)


class TrainingPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        self.data_validation_config = DataValidationConfig()
        self.model_trainer_config = ModelTrainerConfig()
    
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
    
    def start_data_validation(self,data_ingestion_artifacts:DataIngestionArtifacts) -> DataValidationArtifacts:
        try:
            logging.info("Enter the start_data_validation method of TrainingPipeline class")
            logging.info('getting data from URL')
            
            data_validation = DataValidation(data_ingestion_artifacts= data_ingestion_artifacts,
                                             data_validation_config= self.data_validation_config
                                           )
            
            data_validation_artifacts = data_validation.initiate_data_validation()
            logging.info('Performed data validation')
            logging.info("exited the start_data_validation method of TrainPipeline class")

            return data_validation_artifacts
            
        except Exception as e:
            raise Custom_Exception(e,sys)
    

    def start_model_trainer(self)-> ModelTrainerArtifacts:
        try:
            model_trainer = ModelTrainer(model_trainer_config =  self.model_trainer_config)
            model_trainer_artifact = model_trainer.initiate_model_trainer()
            return model_trainer_artifact

        except Exception as e:
            raise Custom_Exception(e,sys)



    def run_pipeline(self)->None:
        try:
            data_ingestion_artifacts = self.start_data_ingestion()
            data_validation_artifacts = self.start_data_validation(data_ingestion_artifacts=data_ingestion_artifacts)

            if data_validation_artifacts.validation_status == True:
                model_trainer_artifact = self.start_model_trainer()
            else:
                raise Exception("Your Data is not in correct format")
            return model_trainer_artifact
        except Exception as e:
            raise Custom_Exception(e,sys)
            