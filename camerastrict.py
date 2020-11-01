import cv2 
import numpy as np 
import dlib 
in_out=2
detector = dlib.get_frontal_face_detector() 
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat") 
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
import math
dist=[]
cnt=0
font = cv2.FONT_HERSHEY_SIMPLEX 
from scipy.spatial import distance as dist
from imutils import face_utils
import imutils
import time
def eye_aspect_ratio(eye):
    A = dist.euclidean(eye[1], eye[5])
    B = dist.euclidean(eye[2], eye[4])
    C = dist.euclidean(eye[0], eye[3])
    ear = (A + B) / (2.0 * C)
    return ear
 
EYE_AR_THRESH = 0.3
EYE_AR_CONSEC_FRAMES = 48

COUNTER = 0
ALARM_ON = False

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]


# org 
org = (20, 20) 
  
# fontScale 
fontScale = 1
   
# Blue color in BGR 
color = (255, 0, 0) 
  
# Line thickness of 2 px 
thickness = 2
def isInside(circle_x, circle_y, rad, x, y): 
       
    if ((x - circle_x) * (x - circle_x) + 
        (y - circle_y) * (y - circle_y) <= rad * rad): 
        return True; 
    else: 
        return False; 

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
    
    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        co=0
        success, frame = self.video.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  
        frame = cv2.cv2.circle(frame, (int((frame.shape[1]/2))+55,int((frame.shape[0]/2))), 150, (0,180,0),2)
        frame = cv2.cv2.circle(frame, (int((frame.shape[1]/2))+55,int((frame.shape[0]/2))+150), 5, (255,0,0),5)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            dst = 6421 / w
            dst = '%.2f' %dst
            k=int(dst[:2])
            cv2.putText(frame, str(dst), (0,0), font, 1, (0, 50, 250), 1, cv2.LINE_AA)
            if k>40:
                frame = cv2.putText(frame, 'Come front', org, font,  fontScale, color, thickness, cv2.LINE_AA) 
                print("Come near to the screen")
    # We actually Convert to grayscale conversion 
        faces = detector(gray) 
        for face in faces: 
    # The face landmarks code begins from here 
            x1 = face.left() 
            y1 = face.top() 
            x2 = face.right() 
            y2 = face.bottom() 
            # Then we can also do cv2.rectangle function (frame, (x1, y1), (x2, y2), (0, 255, 0), 3) 
            landmarks = predictor(gray, face) 
            shape = face_utils.shape_to_np(landmarks)
            leftEye = shape[lStart:lEnd]
            rightEye = shape[rStart:rEnd]
            leftEAR = eye_aspect_ratio(leftEye)
            rightEAR = eye_aspect_ratio(rightEye)
            ear = (leftEAR + rightEAR) / 2.0
            leftEyeHull = cv2.convexHull(leftEye)
            rightEyeHull = cv2.convexHull(rightEye)
            cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
            cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)
            if ear <0.28:
                cv2.putText(frame, "Look Up"+str(ear), (300, 30),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                
        # We are then accesing the landmark points 
            for n in range(0, 68): 
                x = landmarks.part(n).x 
                y = landmarks.part(n).y 
                lx=landmarks.part(5).x
                ly=landmarks.part(5).y
                mlx=landmarks.part(49).x
                mly=landmarks.part(49).y
                mrx=landmarks.part(55).x
                mry=landmarks.part(55).y
                rx=landmarks.part(13).x
                ry=landmarks.part(13).y
                l=[lx,ly]
                r=[rx,ry]
                bpc=[]
                lm=[mlx,mly]
                rm=[mrx,mry]
                dl=math.sqrt( ((l[0]-lm[0])**2)+((l[1]-lm[1])**2) )
                dr=math.sqrt( ((r[0]-rm[0])**2)+((r[1]-rm[1])**2) )
                bpc=math.sqrt( ((r[0]-rm[0])**2)+((r[1]-rm[1])**2) )
                #print(dl,dr)
                if dl>67:
                    print("left")
                    frame = cv2.putText(frame, 'LEFT', org, font,  fontScale, color, thickness, cv2.LINE_AA) 

                if dr>75:
                    print("right")
                    frame = cv2.putText(frame, 'Right', org, font,  fontScale, color, thickness, cv2.LINE_AA) 
                if(isInside(int((frame.shape[1]/2))+55,int((frame.shape[0]/2)),150,landmarks.part(9).x,landmarks.part(9).y) and isInside(int((frame.shape[1]/2))+55,int((frame.shape[0]/2)),150,landmarks.part(17).x,landmarks.part(17).y) and isInside(int((frame.shape[1]/2))+55,int((frame.shape[0]/2)),150,landmarks.part(1).x,landmarks.part(1).y) and isInside(int((frame.shape[1]/2))+55,int((frame.shape[0]/2)),150,landmarks.part(25).x,landmarks.part(25).y) and isInside(int((frame.shape[1]/2))+55,int((frame.shape[0]/2)),150,landmarks.part(20).x,landmarks.part(20).y)): 
                    print("inside")
                else: 
                    print("outside")
                    frame = cv2.putText(frame, 'Allign yoursef in circle', org, font,  fontScale, color, thickness, cv2.LINE_AA) 
                  
                cv2.circle(frame, (x, y), 2, (255, 255, 0), -1)

#        cv2.imshow("Frame", frame) 
        scale_percent = 40        #calculate the 50 percent of original dimensions
        width = int(frame.shape[1] * scale_percent / 100)
        height = int(frame.shape[0] * scale_percent / 100)

        # dsize
        dsize = (width, height)

        # resize image
        frame = cv2.resize(frame, dsize)
        print(frame.shape)
        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()