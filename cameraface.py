import cv2 
import numpy as np 

in_out=2
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
import cv2, os, numpy

dataset = ["", "Gokulraj", "Vishal Sinha", "Ashutosh Agarwal", "Aneesh Dixit", "Kshitiz Khatri", "Nihar Chitnis"]

def detect_faces(img) :
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faceCasc = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    faces = faceCasc.detectMultiScale(gray, 1.3, 5)
    graylist = []
    faceslist = []

    if len(faces) == 0 :
        return None, None

    for i in range(0, len(faces)) :
        (x, y, w, h) = faces[i]
        graylist.append(gray[y:y+w, x:x+h])
        faceslist.append(faces[i])

    return graylist, faceslist

def detect_face(img) :
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faceCasc = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    faces = faceCasc.detectMultiScale(gray, 1.3, 5)
    graylist = []
    faceslist = []

    if len(faces) == 0 :
        return None, None

    (x, y, w, h) = faces[0]
    return gray[y:y+w, x:x+h], faces[0]

def data() :
    dirs = os.listdir("Dataset")

    faces = []
    labels = []

    for i in dirs :
        set = "Dataset/" + i

        label = int(i)

        for j in os.listdir(set) :
            path = set + "/" + j
            img = cv2.imread(path)
            face, rect = detect_face(img)

            if face is not None :
                faces.append(face)
                labels.append(label)

    cv2.destroyAllWindows()
    cv2.waitKey(1)
    cv2.destroyAllWindows()

    return faces, labels

faces, labels = data()

face_recognizer = cv2.face.LBPHFaceRecognizer_create()

face_recognizer.train(faces, numpy.array(labels))

def predict(img) :

    face, rect = detect_faces(img)

    if face is not None :
        for i in range(0, len(face)) :
            label = face_recognizer.predict(face[i])
            label_text = dataset[label[0]]

            (x, y, w, h) = rect[i]
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0))
            cv2.putText(img, label_text, (x, y), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)

    return img


class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
    
    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        co=0
        success, frame = self.video.read()
        frame = predict(frame)
        scale_percent = 60        #calculate the 50 percent of original dimensions
        width = int(frame.shape[1] * scale_percent / 100)
        height = int(frame.shape[0] * scale_percent / 100)

        # dsize
        dsize = (width, height)

        # resize image
        frame = cv2.resize(frame, dsize)
        print(frame.shape)
        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()
