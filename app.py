from object_detection.logger import logging
from object_detection.exception import Custom_Exception
import os, sys
from object_detection.pipeline.training_pipeline import TrainingPipeline


obj = TrainingPipeline()
obj.run_pipeline()


# def app():
#     try:
#         obj = TrainingPipeline()
#         obj.run_pipeline()
#     except Exception as e:
#         abc= Custom_Exception(e, sys)
#         logging.info(abc)

# if __name__ == "__main__":
#     app()
