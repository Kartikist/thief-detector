import cv2 
import time
from mailing import send_email

video = cv2.VideoCapture(0)
time.sleep(1)
status_list = []
first_frame = None
while True:
    status = 0
    check, frame = video.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray_gau = cv2.GaussianBlur(gray, (21,21), 0)
    
    if first_frame is None:
        first_frame = gray_gau
        
    delta = cv2.absdiff(first_frame, gray_gau)
    thresh_frame = cv2.threshold(delta, 30, 255, cv2.THRESH_BINARY)[1]
    dil_frame = cv2.dilate(thresh_frame,None,iterations=2)

    contours, check = cv2.findContours(dil_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        if cv2.contourArea(contour)<7000:
            continue
        x,y,w,h = cv2.boundingRect(contour)
        rectangle = cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 3)
        if rectangle.any():
            status = 1
            
    status_list.append(status)
    status_list = status_list[-2:]
    
    if status_list[0] == 1 and status_list[1] == 0:
       send_email()


    cv2.imshow("Video", frame)    
    key = cv2.waitKey(1)
    
    if key == ord("q"):
        break
    
video.release()
        
