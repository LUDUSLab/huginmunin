from picamera.array import PiRGBArray
from picamera import PiCamera

import cv2
import numpy as np

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
		yield
		#rawCapture.truncate(0)

c = camera()
while True:
	next(c)