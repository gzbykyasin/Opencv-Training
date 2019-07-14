#classes and subclasses to import
import cv2
import numpy as np
import os

filename = 'result1B_1167.csv'
#################################################################################################
# DO NOT EDIT!!!
img1 = cv2.imread('rhombus.png')
img2 = cv2.imread('trapezium.png')
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, thresh1 = cv2.threshold(gray1,127,255,0)
ret, thresh2 = cv2.threshold(gray2,127,255,0)
_,conR,hierarchy = cv2.findContours(thresh1,2,1)
_,conT,hierarchy = cv2.findContours(thresh2,2,1)
lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])
lower_green = np.array([50, 50, 120])
upper_green = np.array([70, 255, 255])
lower_red = np.array([0, 100, 100])
upper_red = np.array([20, 255, 255])

def writecsv(color,shape,cx1,cy1):
    global filename
    #open csv file in append mode
    filep = open(filename,'a')
    # create string data to write per image
    datastr = "," + color + "-" + shape + "-" + str(cx1) + "-" + str(cy1)
    #write to csv
    filep.write("\n")
    filep.write(datastr)
def blend_transparent(face_img, overlay_t_img):
    # Split out the transparency mask from the colour info
    overlay_img = overlay_t_img[:,:,:3] # Grab the BRG planes
    overlay_mask = overlay_t_img[:,:,3:]  # And the alpha plane

    # Again calculate the inverse mask
    background_mask = 255 - overlay_mask

    # Turn the masks into three channel, so we can use them as weights
    overlay_mask = cv2.cvtColor(overlay_mask, cv2.COLOR_GRAY2BGR)
    background_mask = cv2.cvtColor(background_mask, cv2.COLOR_GRAY2BGR)

    # Create a masked out face image, and masked out overlay
    # We convert the images to floating point in range 0.0 - 1.0
    face_part = (face_img * (1 / 255.0)) * (background_mask * (1 / 255.0))
    overlay_part = (overlay_img * (1 / 255.0)) * (overlay_mask * (1 / 255.0))

    # And finally just add them together, and rescale it back to an 8bit integer image    
    return np.uint8(cv2.addWeighted(face_part, 255.0, overlay_part, 255.0, 0.0))
def detectShape(i):
    approx = cv2.approxPolyDP(i,0.01*cv2.arcLength(i,True),True)
    x = len(approx)
    if x==4:
        global conR
        global conT
        ret1=cv2.matchShapes(conR[1],i,1,0.0)
        ret2=cv2.matchShapes(conT[1],i,1,0.0)
        if ret1<ret2:
            return "rhombus"
        else :
            return "trapezium"
    elif x==3:
        return "triangle"
    elif x==5:
        return "pentagon"
    elif x==6:
        return "hexagon"
    else:
        return "circle"

def detectCentroid(i):
    M = cv2.moments(i)
    if M['m00']==0:
        return 0,0
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])
    return cx,cy

def checkTrue(shapeName,centroid,shape,centre):
    for i in range(len(shapeName)):
        if((shapeName[i]==shape) and (centroid[i]==centre)):
            return True
    
def detectColor(i,shapeName,centroid):
    hsv = cv2.cvtColor(i, cv2.COLOR_BGR2HSV)
    mask1 = cv2.inRange(hsv, lower_blue, upper_blue)
    mask2 = cv2.inRange(hsv, lower_red, upper_red)
    mask3 = cv2.inRange(hsv, lower_green, upper_green)
    ret, threshS1 = cv2.threshold(mask1,127,255,0)
    _,contoursS1,hierarchy = cv2.findContours(threshS1,2,1)
    ls=[]
    for i in contoursS1:
        blue=[]
        cx,cy=detectCentroid(i)
        shape=detectShape(i)
        if(checkTrue(shapeName,centroid,shape,(cx,cy))):
            blue.append("blue")
            blue.append(shape)
            blue.append((cx,cy))
            writecsv(blue[0],blue[1],cx,cy)
            ls.append(blue)
    ret, threshS2 = cv2.threshold(mask2,127,255,0)
    _,contoursS2,hierarchy = cv2.findContours(threshS2,2,1)
    for i in contoursS2:
        red=[]
        cx,cy=detectCentroid(i)
        shape=detectShape(i)
        if(checkTrue(shapeName,centroid,shape,(cx,cy))):
            red.append("red")
            red.append(shape)
            red.append((cx,cy))
            writecsv(red[0],red[1],(cx,cy))
            ls.append(red)
    ret, threshS3 = cv2.threshold(mask3,127,255,0)
    _,contoursS3,hierarchy = cv2.findContours(threshS3,2,1)
    for i in contoursS3:
        green=[]
        cx,cy=detectCentroid(i)
        shape=detectShape(i)
        if(checkTrue(shapeName,centroid,shape,(cx,cy))):
            green.append("green")
            green.append(shape)
            green.append((cx,cy))
            writecsv(green[0],green[1],(cx,cy))
            ls.append(green) 
    return ls

def search(i,ls):
    cx,cy=detectCentroid(i)
    for m in ls:
        for n in m:
            if n[2][0]==cx and n[2][1]==cy:
                if(n[0]=='red'):
                    return 'image_red'
                elif(n[0]=='green'):
                    return 'image_green'
                elif(n[0]=='blue'):
                    return 'image_blue'
                
def substractCont(A,B):
    c=[]
    flag=0
    for i in A:
        flag=0
        for j in B:
            for k in j:
                if cv2.matchShapes(i,k,1,0.0)<=0.001:
                    flag=1
                    break
        if flag==0:
            c.append(i)
    return c
                
def main(video_file_with_path):
#####################################################################################################
    #Write your code here!!!
    lCon=1
    print('video_file_with_path')
    cap = cv2.VideoCapture(video_file_with_path)
    image_red = cv2.imread("yellow_flower.png",-1)
    image_blue = cv2.imread("pink_flower.png",-1)
    image_green = cv2.imread("red_flower.png",-1)
    fourcc = cv2.VideoWriter_fourcc(*'DIVX')
    out = cv2.VideoWriter('video_output.mp4',fourcc,1.0,(1280,720))
    ls=[]
    contourGen=[]
    while cap.isOpened():
        ret, frame = cap.read()
        shape=[]
        centroid=[]
        ans=[]
        if ret == True:
            grayS = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            ret, threshS = cv2.threshold(grayS,127,255,0)
            _,contoursS,hierarchy = cv2.findContours(threshS,2,1)
            if (len(contoursS)>lCon):
                contoursS=substractCont(contoursS[1:],contourGen)
                contourGen.append(contoursS)
                for i in contoursS:
                    shape.append(detectShape(i))
                    centroid.append(detectCentroid(i))
                ans.append(detectColor(frame,shape,centroid))
                print(ans)
                for i in contoursS:
                    imageName = str(search(i,ans))
                    if(imageName=="image_red"):
                        x,y,w,h = cv2.boundingRect(i)
                        overlay_image = cv2.resize(image_red,(h,w))
                        frame[y:y+w,x:x+h,:] = blend_transparent(frame[y:y+w,x:x+h,:], overlay_image)
                        out.write(frame)
                    elif(imageName=="image_green"):
                        x,y,w,h = cv2.boundingRect(i)
                        overlay_image = cv2.resize(image_green,(h,w))
                        frame[y:y+w,x:x+h,:] = blend_transparent(frame[y:y+w,x:x+h,:], overlay_image)
                        out.write(frame)
                    elif(imageName=="image_blue"):
                        x,y,w,h = cv2.boundingRect(i)
                        overlay_image = cv2.resize(image_blue,(h,w))
                        frame[y:y+w,x:x+h,:] = blend_transparent(frame[y:y+w,x:x+h,:], overlay_image)
                        out.write(frame)
                lCon+=1
                if cv2.waitKey(1) & 0xFF==ord('q'):
                    cv2.destroyAllWindows()## 27 - ASCII for escape key
                    break
        else:
            break
    cap.release()
    out.release()
    print("Video Processing done")
    
#####################################################################################################

#####################################################################################################
    #sample of overlay code for each frame
    #x,y,w,h = cv2.boundingRect(current_contour)
    #overlay_image = cv2.resize(image_red,(h,w))
    #frame[y:y+w,x:x+h,:] = blend_transparent(frame[y:y+w,x:x+h,:], overlay_image)
#######################################################################################################

#################################################################################################
# DO NOT EDIT!!!
#################################################################################################
#main where the path is set for the directory containing the test images
if __name__ == "__main__":
    main('Video.mp4')
