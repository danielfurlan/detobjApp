#import flask
from flask import Flask, jsonify, render_template

import werkzeug
from PIL import Image
import io
import cv2
import json, base64



# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    #return 'Hello World!'


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



if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python37_app]
