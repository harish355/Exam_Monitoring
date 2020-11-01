# Using Android IP Webcam video .jpg stream (tested) in Python2 OpenCV3

import urllib
import cv2
import numpy as np
import time
cv2.namedWindow("output", cv2.WINDOW_NORMAL)        
cv2.resizeWindow("output", 700, 500)      
# Replace the URL with your own IPwebcam shot.jpg IP:port
url='http://192.168.43.31:1060/shot.jpg?rnd=687086'
while True:
    imgResp = urllib.urlopen(url)
    imgNp = np.array(bytearray(imgResp.read()),dtype=np.uint8)
    img = cv2.imdecode(imgNp,-1)
    cv2.imshow('output',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break