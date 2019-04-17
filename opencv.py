import cv2
import numpy as np

def buildMap(Ws,Hs,Wd,Hd,R1,R2,Cx,Cy):
    map_x = np.zeros((Hd,Wd),np.float32)
    map_y = np.zeros((Hd,Wd),np.float32)
    for y in range(0,int(Hd-1)):
        for x in range(0,int(Wd-1)):
            r = (float(y)/float(Hd))*(R2-R1)+R1
            theta = (float(x)/float(Wd))*2.0*np.pi
            xS = Cx+r*np.sin(theta)
            yS = Cy+r*np.cos(theta)
            map_x.itemset((y,x),int(xS))
            map_y.itemset((y,x),int(yS))
        
    return map_x, map_y

def unwarp(img,xmap,ymap):
    output = cv2.remap(img,xmap,ymap,cv2.INTER_LINEAR)
    output = cv2.flip(output,0)
    return output

cap = cv2.VideoCapture(0)
Wd = 590
Hd = 125
Ws = 640
Hs = 480
Cx = 304
Cy = 223
R1 = 32
R2 = 155

print 'wd',Wd,'Hd',Hd,'Ws',Ws,'Hs',Hs,'R1',R1,'R2',R2,'Cx',Cx,'Cy',Cy
xmap,ymap = buildMap(Ws,Hs,Wd,Hd,R1,R2,Cx,Cy)

while(True):

    ret, frame = cap.read()
    result = unwarp(frame,xmap,ymap)
    cv2.imshow('frame',frame)
    cv2.imshow('dewarp',result)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
 
cap.release()
cv2.destroyAllWindows()
