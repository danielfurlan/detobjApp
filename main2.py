!pip3 install flask
!pip3 install werkzeug
!pip3 install Pillow
!pip3 install -U Werkzeug

import flask
from flask import Flask, jsonify, render_template
import flask
import werkzeug
from PIL import Image
import io
import cv2
import json, base64
    
import torch, torchvision
    #print("Torch version: ", torch.__version__)

import detectron2
from detectron2.utils.logger import setup_logger
setup_logger()

    # import some common libraries
import numpy as np
#from google.colab.patches import cv2_imshow

# import some common detectron2 utilities
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2.utils.visualizer import Visualizer
from detectron2.data import MetadataCatalog

app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/', methods=['GET', 'POST'])
def handle_request():
    
    path = "/var/www/danielfurlan.com/immaggine/"
    fileJPG = "AIimage.jpeg"
    #filePng = "upsud.png"
    
    #new_im = Image.open(path+fileJPG)
    if flask.request.method == "POST":
        imageFile = flask.request.files['image']
        Filename = werkzeug.utils.secure_filename(imageFile.filename)
        print("\nReceived image file name : " + Filename)
    
    ### FACCIAMO QUALSIASI COSA CON L'IMMAGGINE E SALVIAMOLA NELLA SCATOLA "STATIC"
        resp = ["./Processed/new_Im.jpg", 2]
    
        imageFile.save("./static/"+ Filename + "altered")
    #url_path = "http://192.168.1.105:5000/static/"+ Filename + "altered"
        url_path = "http://192.168.1.105:5000/static/banana1.jpgaltered"
    
        num_inst = resp[1]

        js = {"num_inst":2, "image_url":url_path}
    
    #myfile = {'document':('imgBytes', open(imgBytes)),'datas':'json.dumps(js)'}
    #return imgBytes
        return js
    
@app.route('/static/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    uploads = os.path.join(current_app.root_path, app.config['static'])
    print("funziona!")
    return send_from_directory(directory=uploads, filename=filename)

@app.route("/test/<name>")
#def test(Image im):
def test(name):
    print("Il nome consegnato è : ", name)

    im = cv2.imread("./" + name)

    outputs = predictor(im)
    print("Numero di elementi: ", len(outputs["instances"]))
          
    num_inst = len(outputs["instances"])
    
    v = Visualizer(im[:, :, ::-1], MetadataCatalog.get(cfg.DATASETS.TRAIN[0]), scale=1.2)
    v = v.draw_instance_predictions(outputs["instances"].to("cpu"))

    new_Im = Image.fromarray(v.get_image()[:, :, ::-1])
    new_Im.save("./Processed/new_Im.jpg")
    new_Im.filename = "new_Im.jpg";
    
    print("funzionando...")
    
    js = ["./Processed/new_Im.jpg", num_inst]
    return js

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

