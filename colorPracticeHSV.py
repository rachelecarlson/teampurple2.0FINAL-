import skimage as sk
import numpy as np
import matplotlib.pyplot as mpimg
print(sk.__version__)
channel = np.ones((3,3)) #3x3 is the shape
imageHSV = np.dstack([1*channel, 0*channel, 0*channel]) 
##now H is hue, so between 0,1 
#S is between 0 (gray), 1 (perfect version of the color)
#brightness 0 (black), 1 (white)
imagePractice = sk.hsv2rgb(imageHSV)
#we'll treat imagePractice as an HSV image 
#concatenate along third dimension
imgplot = mpimg.imshow(imagePractice) 
mpimg.show()