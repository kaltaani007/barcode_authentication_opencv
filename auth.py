import cv2
import numpy as np
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(0)
# Reading the data file containing name of auhentic users
with open("data.txt") as file :
    data = file.read().splitlines()

while True:

    ret , frame = cap.read()

    for brcode in decode(frame):
        #print(brcode.data)

        myData = brcode.data.decode('utf-8')

        if myData in data:
            opt = "Authorise"
            myColor = (0 , 255, 0 )
        else :
            opt = "Un-Authorised"
            myColor = ( 255 , 0 , 0)



        #print(myData)
        pts = np.array([brcode.polygon] , np.int32)
        pts = pts.reshape(-1 , 1 , 2 )

        rect_pnts = brcode.rect

        cv2.polylines(frame , [pts] , True , (255 , 0 , 255 ) , 5)



        cv2.putText ( frame , opt  , (rect_pnts[0], rect_pnts[1] ) , cv2.FONT_HERSHEY_SIMPLXE ,
                      0.9 , myColor  , 2)



    cv2.imshow("test" , frame)
    #cv2.waitKey(1)
    if cv2.waitKey(0) == ord('q'):
        break

