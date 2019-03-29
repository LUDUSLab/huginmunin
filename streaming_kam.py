from flask import Flask, render_template, Response
import cv2
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('camerasFront.html')

def gen():
    streaming=cv2.VideoCapture(0)
    while (streaming.isOpened()):
        ret1,img1=streaming.read()
        yield (img1)

@app.route('/video_feed')
def video_feed():
    return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=img')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000', debug=True)

