import cv2
import numpy as np

image1 = cv2.imread('testImages/beachBright.jpeg', cv2.IMREAD_COLOR)
image2 = cv2.imread('testImages/medBeach.jpeg', cv2.IMREAD_COLOR)
image3 = cv2.imread('testImages/darkBeach.jpeg', cv2.IMREAD_COLOR)

image1Total = np.sum(image1[:,:,0]) + np.sum(image1[:,:,1]) + np.sum(image1[:,:,2])
image2Total = np.sum(image2[:,:,0]) + np.sum(image2[:,:,1]) + np.sum(image2[:,:,2])
image3Total = np.sum(image3[:,:,0]) + np.sum(image3[:,:,1]) + np.sum(image3[:,:,2])

print("Bright Beach Total: " + str(image1Total))
print("Medium Beach Total: " + str(image2Total))
print("Dark Beach Total: " + str(image3Total))
