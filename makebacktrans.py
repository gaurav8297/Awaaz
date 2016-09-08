import cv2
import numpy

def cvttopng():
    img =cv2.imread("xyz.jpg",cv2.IMREAD_UNCHANGED)
    n=len(img)
    a=numpy.empty([n, 844,4])
    for i in range(n):
        m=len(img[i])
        for j in range(m):
            a[i][j]=numpy.append(img[i][j],[400])
    print a.shape
    cv2.imwrite("cc.png",a)

def remove_background():
    img = cv2.imread("abcd.gif", cv2.IMREAD_UNCHANGED)
    print img
    n = len(img)
    for i in range(n):
        m = len(img[i])
        for j in range(m):
            x=img[i][j]
            # img[i][j][3] = 50
            if x[0]==66 and x[1]==33 and x[2]==24:
                img[i][j][3]=0

    cv2.imwrite("final.png", img)

def change_to_dark():
    img = cv2.imread("image1.jpg", cv2.IMREAD_GRAYSCALE)
    cv2.imwrite("final.jpg", img)
change_to_dark()
