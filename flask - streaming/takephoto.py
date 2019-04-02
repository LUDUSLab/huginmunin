from picamera.array import PiRGBArray
from picamera import PiCamera
from flask import Flask, render_template, Response, send_file, make_response, jsonify
from flask_cors import CORS
import cv2
import base64
import numpy as np

app = Flask(__name__)
CORS(app)
@app.route('/')
def index():
    return render_template('camerasFront.html')

@app.route('/takephoto')
def take_photos():
	try:
		#return send_file('t.jpg', attachment_filename='foto.jpg')
		return make_response(jsonify({"image":base64.b64encode(open('t.jpg', 'rb').read())}))
	except Exception as e:
		print(e)
		return str(e)
	pass

if __name__ == '__main__':
	app.run(host='0.0.0.0', port='8001', debug=False)

