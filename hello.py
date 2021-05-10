import cv2
from deepface import DeepFace
import numpy
import keyboard

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(1)

if not cap.isOpened():
  cap=cv2.VideoCapture(0)
if not cap.isOpened():
  raise IOError("Cannot Open The Webcam")


while True:
  ret, frame=cap.read()
  result= DeepFace.analyze(frame, actions=["emotion"])

  gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  faces= faceCascade.detectMultiScale(gray,1.1,4)

  for(x,y,w,h) in faces:
    cv2.rectangle(frame, (x,y),(x+w, y+h),(0,255,0),2)

  font= cv2.FONT_HERSHEY_SIMPLEX

  cv2.putText(frame, 
              result['dominant_emotion'],
              (50,50),
              font, 3,
              (0,0,255),
              2,
              cv2.LINE_4)
  cv2.imshow('Original video', frame)

  emo=result["dominant_emotion"]
  print(f"Dominant emotion detected is {emo}")

  inp=input("Press 'q' to QUIT OR Press any other key to continue to detect next emotion ")
  if keyboard. is_pressed('q'):
    cap.release()
    cv2.destroyAllWindows()
  else:
    continue

  