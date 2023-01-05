import cv2
import imutils

def getImage(input_image):
    image = cv2.imread(input_image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)[1]
    # check to see if we are using OpenCV 2.X
    if imutils.is_cv2() or imutils.is_cv4():
        (cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                                     cv2.CHAIN_APPROX_SIMPLE)
    # check to see if we are using OpenCV 3
    elif imutils.is_cv3():
        (_, cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                                        cv2.CHAIN_APPROX_SIMPLE)

    # draw the contours on the image
    cv2.drawContours(image, cnts, -1, (255,0,0), 3)

    return image