# import the necessary packages
import imutils
import cv2
 
# load the input image and show its dimensions, keeping in mind that
# images are represented as a multi-dimensional NumPy array with
# shape no. rows (height) x no. columns (width) x no. channels (depth)
# Carica immagine nella forma di array
image = cv2.imread("img/1.jpeg")
(h, w, d) = image.shape
print("width={}, height={}, depth={}".format(w, h, d))


# access the RGB pixel located at x=50, y=100, keepind in mind that
# OpenCV stores images in BGR order rather than RGB
(B, G, R) = image[100, 50]
print("R={}, G={}, B={}".format(R, G, B))


# display the image to our screen -- we will need to click the window
# open by OpenCV and press a key on our keyboard to continue execution
cv2.imshow("Imagine", image)

# extract a 100x100 pixel square ROI (Region of Interest) from the
# input image starting at x=320,y=60 at ending at x=420,y=160
roi = image[60:160, 10:20]
cv2.imshow("ROI", roi)

cv2.waitKey(0)
