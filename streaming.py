import cv2
import numpy as np
	
streaming=cv2.VideoCapture(0)

K=0
while K!=27:
    ret1,img1=streaming.read()
    cv2.namedWindow('Streaming KAM', cv2.WINDOW_NORMAL)
    cv2.imshow('Streaming KAM', img1)
    K=cv2.waitKey(10) & 0xff #MÁQUINA DE 64 BITS
    
streaming.release()
cv2.destroyWindow("Streaming KAM")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
