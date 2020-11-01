# We Import the necessary packages needed 
import cv2 
import numpy as np 
import dlib 
left_timer=0
right_timer=0
out_timer=0
tml=0
tmr=0
tmo=0
in_out=2
cap = cv2.VideoCapture(0) 
detector = dlib.get_frontal_face_detector() 
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat") 
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
import math
dist=[]
cnt=0
def isInside(circle_x, circle_y, rad, x, y): 
       
    if ((x - circle_x) * (x - circle_x) + 
        (y - circle_y) * (y - circle_y) <= rad * rad): 
        return True; 
    else: 
        return False; 
while True: 
	_, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  
	facess = detector(gray) 
	i =0
	for face in facess: 

	    # Get the coordinates of facess 
	    x, y = face.left(), face.top() 
	    x1, y1 = face.right(), face.bottom() 
	    
	    # Increment iterator for each face in facess 
	    i = i+1

	    # Display the box and facess 
	    cv2.putText(frame, 'Total person:'+str(i), (x-10, y-10), 
	                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2) 
	    
	frame = cv2.cv2.circle(frame, (int((frame.shape[1]/2))+55,int((frame.shape[0]/2))), 150, (0,180,0),2)
	frame = cv2.cv2.circle(frame, (int((frame.shape[1]/2))+55,int((frame.shape[0]/2))+150), 5, (255,0,0),5)
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	for (x, y, w, h) in faces:
		dst = 6421 / w
		dst = '%.2f' %dst
		k=int(dst[:2])
		font = cv2.FONT_HERSHEY_SIMPLEX
		cv2.putText(frame, str(dst), (x, y-10), font, 1, (0, 50, 250), 1, cv2.LINE_AA)
		if k>40:
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
			if dl>63:
				print("left")
			if dr>70:
				print("right")
			if(isInside(int((frame.shape[1]/2))+55,int((frame.shape[0]/2)),150,landmarks.part(9).x,landmarks.part(9).y) and isInside(int((frame.shape[1]/2))+55,int((frame.shape[0]/2)),150,landmarks.part(17).x,landmarks.part(17).y) and isInside(int((frame.shape[1]/2))+55,int((frame.shape[0]/2)),150,landmarks.part(1).x,landmarks.part(1).y) and isInside(int((frame.shape[1]/2))+55,int((frame.shape[0]/2)),150,landmarks.part(25).x,landmarks.part(25).y) and isInside(int((frame.shape[1]/2))+55,int((frame.shape[0]/2)),150,landmarks.part(20).x,landmarks.part(20).y)): 
			    pass
			    
			else: 
			    print("outside")
			  
			cv2.circle(frame, (x, y), 2, (255, 255, 0), -1) 
	cv2.imshow("Frame", frame) 

	key = cv2.waitKey(1) 
	if key == 27: 
		break