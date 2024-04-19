import os, sys
import shutil
from object_detection.logger import logging
from object_detection.exception import Custom_Exception

from object_detection.pipeline.training_pipeline import TrainingPipeline
from object_detection.utils.main_utils import decodeImage, encodeImageIntoBase64
from flask import Flask, request, jsonify, render_template, Response
from flask_cors import CORS, cross_origin
from object_detection.constants.application import APP_HOST, APP_PORT




app = Flask(__name__)
CORS(app)

class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"



@app.route("/train")
def trainRoute():
    obj = TrainingPipeline()
    obj.run_pipeline()
    return "Training Successfull!!" 


@app.route("/")
def home():
    return render_template("index.html")

best = r"D:\PycharmProjects\mlops_projects\object_detection_end2end\artifacts\model_trainer\best.pt"

@app.route("/predict", methods=['POST','GET'])
@cross_origin()
def predictRoute():
    try:
        # if os.path.exists("yolov5/runs"):
        #     shutil.rmtree("yolov5/runs")

        image = request.json['image']
        decodeImage(image, clApp.filename)
        
        os.system(f"cd yolov5/ && python detect.py --weights {best} --img 416 --conf 0.01 --source ../data/inputImage.jpg")
        
        opencodedbase64 = encodeImageIntoBase64("yolov5/runs/detect/exp/inputImage.jpg")
        result = {"image": opencodedbase64.decode('utf-8')}
        shutil.rmtree("yolov5/runs")

    except ValueError as val:
        print(val)
        return Response("Value not found inside  json data")
    except KeyError:
        return Response("Key value error incorrect key passed")
    except Exception as e:
        print(e)
        result = "Invalid input"

    return jsonify(result)



@app.route("/live", methods=['GET'])
@cross_origin()
def predictLive():
    try:
        os.system(f"cd yolov5/ && python detect.py --weights {best} --img 416 --conf 0.5 --source 0")
        os.system("rm -rf yolov5/runs")
        return "Camera starting!!" 

    except ValueError as val:
        print(val)
        return Response("Value not found inside  json data")
    


if __name__ == "__main__":
    clApp = ClientApp()
    app.run(host=APP_HOST, port=APP_PORT)