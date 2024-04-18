import gdown
import os



dataset_url = "https://drive.google.com/file/d/1Wzg4EgtNe5JbMA4UoKeIKko-Falbol8w/view?usp=sharing"
file_id = dataset_url.split('/')[-2]
prefix = f"https://drive.google.com/uc?id={file_id}"
zip_file_path = r"D:\PycharmProjects\mlops_projects\object_detection_end2end\artifacts\feature_store"
gdown.download(prefix, zip_file_path)