from picamera.array import PiRGBArray
from picamera import PiCamera
from flask import Flask, render_template, Response, send_file
import cv2
import numpy as np

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('camerasFront.html')

@app.route('/takephoto')
def take_photos():
	try:
		return send_file('t.jpg', attachment_filename='foto.jpg')
	except Exception as e:
		return str(e)
	pass

def camera():
	cap = PiCamera()
	cap.resolution = (640, 480)
	cap.framerate = 16
	rawCapture = PiRGBArray(cap, size=(640, 480))
	
	print("tamo aqui")
		#Detection
	for frame in cap.capture_continuous(rawCapture, format="bgr", use_video_port=True):
		#Face Detection
		image = frame.array #BGR
	
		img=image
		img = img[...,::-1]  #BGR 2 RGB
		inputs = img.copy() / 255.0
			
		img_cv = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
		cv2.imwrite('t.jpg', img_cv)
		rawCapture.truncate(0)
		yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + cv2.imencode('.jpg', img_cv)[1].tobytes() + b'\r\n')
		#rawCapture.truncate(0)

def stream():	
	for frame in frames:
		#Face Detection
		image = frame.array #BGR
	
		img=image
		img = img[...,::-1]  #BGR 2 RGB
		inputs = img.copy() / 255.0
			
		img_cv = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
		cv2.imwrite('t.jpg', img_cv)
		rawCapture.truncate(0)
		yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + open('t.jpg', 'rb').read() + b'\r\n')
		#rawCapture.truncate(0)



'''
def gen():
	streaming=cv2.VideoCapture(0)	
	while True:
		ret1,frame=streaming.read()
		cv2.imwrite('t.jpg', frame)
		yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + open('t.jpg', 'rb').read() + b'\r\n')
'''    
@app.route('/video_feed')
def video_feed():
    return Response(camera(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
	camera()
	app.run(host='0.0.0.0', port='8000', debug=False)

