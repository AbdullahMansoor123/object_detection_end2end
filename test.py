import gdown
import os
import zipfile
import shutil

# dataset_url = "https://drive.google.com/file/d/1Wzg4EgtNe5JbMA4UoKeIKko-Falbol8w/view?usp=sharing"
# file_id = dataset_url.split('/')[-2]
# prefix = f"https://drive.google.com/uc?id={file_id}"
# zip_file_path = r"D:\PycharmProjects\mlops_projects\object_detection_end2end\artifacts\feature_store"
# gdown.download(prefix, zip_file_path)

# with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
#                 zip_ref.extractall(r"D:\PycharmProjects\mlops_projects\object_detection_end2end\artifacts\feature_store")


data_yaml = "data.yaml"
model_weight = "yolov5n"
# os.system(f"cd yolov5/ && python train.py --img 640 --batch 16 --epochs 1 --data {data_yaml} --weights yolov5n.pt --cache")

from object_detection.entity.config_entity import DataIngestionConfig
# print(os.path.join(os.getcwd(), DataIngestionConfig.feature_store_file_path+"\data.yaml"))

# shutil.rmtree("yolov5/runs")

with zipfile.ZipFile("catdogmonkey_dataset.zip", "r") as zip_ref:
    zip_ref.extractall()   
# os.remove("catdogmonkey_dataset.zip")