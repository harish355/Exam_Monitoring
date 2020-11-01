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
        in_out=2
        ri_le=0
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
                    ri_le=2
                if dr>75:
                    print("right")
                    ri_le=1
                    frame = cv2.putText(frame, 'Right', org, font,  fontScale, color, thickness, cv2.LINE_AA) 
                if dl<67 and dr<75:
                    ri_le=0
                if(isInside(int((frame.shape[1]/2))+55,int((frame.shape[0]/2)),150,landmarks.part(9).x,landmarks.part(9).y) and isInside(int((frame.shape[1]/2))+55,int((frame.shape[0]/2)),150,landmarks.part(17).x,landmarks.part(17).y) and isInside(int((frame.shape[1]/2))+55,int((frame.shape[0]/2)),150,landmarks.part(1).x,landmarks.part(1).y) and isInside(int((frame.shape[1]/2))+55,int((frame.shape[0]/2)),150,landmarks.part(25).x,landmarks.part(25).y) and isInside(int((frame.shape[1]/2))+55,int((frame.shape[0]/2)),150,landmarks.part(20).x,landmarks.part(20).y)): 
                    print("inside")
                    in_out=0
                else: 
                    print("outside")
                    in_out=in_out+1
                    frame = cv2.putText(frame, 'Allign yoursef in circle', org, font,  fontScale, color, thickness, cv2.LINE_AA) 
                    #print(in_out)
                    if in_out>300:
                        print("Warning Allign yoursef in circle")
            
                    
                  
                cv2.circle(frame, (x, y), 2, (255, 255, 0), -1)


#        cv2.imshow("Frame", frame) 
        scale_percent = 40        #calculate the 50 percent of original dimensions
        width = int(frame.shape[1] * scale_percent / 100)
        height = int(frame.shape[0] * scale_percent / 100)

        # dsize
        dsize = (width, height)

        # resize image
        frame = cv2.resize(frame, dsize)
        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()