import os
import sys
import zipfile
import gdown

from object_detection.logger import logging
from object_detection.exception import Custom_Exception
from object_detection.entity.config_entity import DataIngestionConfig
from object_detection.entity.artifacts_entity import DataIngestionArtifacts


class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig = DataIngestionConfig()):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise Custom_Exception(e,sys)
    # this methods can be replace be another methods use for downloading data
    def download_from_GoogleDrive(self)-> str:
        """fetech data from URL"""
        try:
            dataset_url = self.data_ingestion_config.data_download_url
            zip_dowonload_dir = self.data_ingestion_config.data_ingestion_dir
            os.makedirs(zip_dowonload_dir,exist_ok=True)
            data_filename = 'catdog_dataset.zip'
            zip_file_path = os.path.join(zip_dowonload_dir,data_filename)
            logging.info(f'Downloading {data_filename} from {dataset_url} into Directory: {zip_dowonload_dir}')

            file_id = dataset_url.split('/')[-2]
        
            prefix = f"https://drive.google.com/uc?id={file_id}"
            gdown.download(prefix, zip_file_path)
            logging.info(f"{data_filename} downloaded in directory {zip_dowonload_dir}")

            return zip_file_path


        except Exception as e:
            raise Custom_Exception(e,sys)
        
    def extract_zip_file(self, zip_file_path:str)-> str:
        try:
            feature_store_path = self.data_ingestion_config.feature_store_file_path
            os.makedirs(feature_store_path, exist_ok=True)
            with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
                zip_ref.extractall(feature_store_path)
            logging.info(f"extracting zip_file {zip_file_path} into dir {feature_store_path}")
         
            return feature_store_path
        
        except Exception as e:
            Custom_Exception(e,sys)

    def download_from_AWS_S3(self)-> str:
        try:
            pass
        except Exception as e:
            Custom_Exception(e,sys) 

    def initiate_data_ingestion(self)->DataIngestionArtifacts:
        logging.info('Starting data ingestion process')
        try:
            zip_file_path  = self.download_from_GoogleDrive()
            feature_store_path = self.extract_zip_file(zip_file_path)
            data_ingestion_artifacts = DataIngestionArtifacts(
                data_zip_file_path = zip_file_path,
                feature_store_path = feature_store_path
            )
            logging.infor("Exiting Data Ingestion Process")
            logging.infor(f"Data Ingestion artifacts {data_ingestion_artifacts}")
            return data_ingestion_artifacts
        except Exception as e:
            Custom_Exception(e, sys)
        