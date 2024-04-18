import os
from dataclasses import dataclass
from datetime import datetime
from object_detection.constants.training_pipeline import *


@dataclass
class TrainingPipelineConfig:
    artifacts_dir: str = ARTIFACTS_DIR
    

@dataclass
class DataIngestionConfig:
    
    data_ingestion_dir: str = os.path.join(
        TrainingPipelineConfig.artifacts_dir, DATA_INGESTION_DIR_NAME
    )
    feature_store_file_path: str = os.path.join(
        TrainingPipelineConfig.artifacts_dir, DATA_INGESTION_FEATURE_STORE_DIR
    )
    data_download_url: str = os.path.join(
        TrainingPipelineConfig.artifacts_dir, DATA_DOWNLOAD_URL 
    )
