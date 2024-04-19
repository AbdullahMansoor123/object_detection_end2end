import os
import sys
import zipfile
import gdown
import shutil

from object_detection.logger import logging
from object_detection.exception import Custom_Exception
from object_detection.entity.config_entity import DataValidationConfig
from object_detection.entity.artifacts_entity import (DataIngestionArtifacts ,DataValidationArtifacts)

class DataValidation:
    def __init__(self, data_ingestion_artifacts:DataIngestionArtifacts,
                 data_validation_config: DataValidationConfig,
                    ):
        try:
            self.data_ingestion_artifacts = data_ingestion_artifacts
            self.data_validation_config = data_validation_config
        except Exception as e:
            raise Custom_Exception(e,sys)
        
    def validate_all_files_exist(self)->bool:
        try:
            validation_status = None

            all_files = os.listdir(self.data_ingestion_artifacts.feature_store_path)
                        
            for file in all_files:
                if file not in self.data_validation_config.required_file_list:
                    validation_status = False
                    os.makedirs(os.path.join(DataValidationConfig.data_validation_dir),exist_ok=True)
                    with open(self.data_validation_config.valid_status_file_dir, 'w') as f:
                        f.write(f"validation_status: {validation_status}")
                else:
                    validation_status = True
                    os.makedirs(os.path.join(DataValidationConfig.data_validation_dir),exist_ok=True)
                    with open(self.data_validation_config.valid_status_file_dir, 'w') as f:
                        f.write(f"validation_status: {validation_status}")
            return validation_status

        except Exception as e:
            raise Custom_Exception(e,sys)
        

    def initiate_data_validation(self)->DataValidationArtifacts:
        logging.info("Entered initiate_data_validation method of DataValidation class")
        try:
            logging.info("got data_validation_dir")
            status = self.validate_all_files_exist()
            data_validation_artifacts= DataValidationArtifacts(validation_status=status)
            
            logging.info("Exited initiate_data_validation")
            logging.info(f"data validation artifacts {data_validation_artifacts}")
            if status:
                shutil.copy(self.data_ingestion_artifacts.data_zip_file_path, os.getcwd())
            
            return data_validation_artifacts
        
        except Exception as e:
            raise Custom_Exception(e,sys)