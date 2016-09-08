import cv2
import numpy as np
face_c=cv2.CascadeClassifier("h1gest.xml")
face_a=cv2.CascadeClassifier("aGest.xml")
cap=cv2.VideoCapture(0)
flagA=0
flagH=0
while True:
    ret, frame = cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_c.detectMultiScale(gray,1.66,25) # adjust the last values acc to your cascade file
    # 1.66,60
    faces2=face_a.detectMultiScale(gray,1.6,3)
    flagA=0
    flagH=0
    for (x, y, w, h) in faces2:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 16, 196), 2)
        flagA = 1
    if flagA==0:
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 16, 196), 2)
            flagH = 1
    if flagA==1:
        cv2.putText(frame, "A", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 0)
    elif flagH==1:
        cv2.putText(frame, "H", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 0)
    cv2.putText(frame, "Awaaz", (25, 450), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1.2,(0,16,196),2)
    cv2.imshow('Awaaz',frame)
    k = cv2.waitKey(30) & 0xFF
    if k == "Q":
        break
cv2.destroyAllWindows()
cap.release()
