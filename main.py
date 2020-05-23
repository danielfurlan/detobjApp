!pip3 install flask
!pip3 install werkzeug
!pip3 install Pillow
!pip3 install -U Werkzeug

import flask
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
    return 'Hello World!'


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python37_app]
