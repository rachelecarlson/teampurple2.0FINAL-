import numpy as np
#import psychopy as py
import matplotlib as mpl 
import pandas as pd 
import skimage as sk
import matplotlib.pyplot as mplpy 

n = 3 #number of blocks in rows or columns (so n = 3 is a 3x3 grid) 
counter = 1
print('Instructions: In each round, two colored grids will be displayed (one after the other). When prompted, indicate whether the two grids were the same or different.')
answer_vector = []
groundtruth = [] #keeping track of whether the grid is disharmonious or harmonious
samedifferent = [] #keeping track of whether the grid was the same or different in the trial
while counter <=5: #the program will run for 5 rounds 
    blankMat = np.zeros(150)
    mplpy.imshow(np.uint8(blankMat))
    #pause(3)
    T = np.randint([1,2],1)
    #groundtruth = [groundtruth T] #trying to concatonate 
    if T == 1:
        c = np.randint(3) #for harmonious grid (picking one color channel and random int within that color)
        c = np.uint8(c)
        yy = np.zeros(150,150,3)
        yy= np.uint8(yy)
        #attempting more sustainable code, using matrix instead of hard code 
        zz = np.randint(255, size=(3.,3.)) ##for saturation 
        #we could also make one vector 

        for colorChan in range(0,3): ## will go through all 9 squares in red, g, b channels
            for rowscols in range(0,len(zz)):
             #make sure it's going through all 9 of the squares, not just one dimension 
             
 #initialize start position 
                startXPosition = 0 #starting a first block at 0,0 -- we may need to specifiy the x and y here 
                startYPosition = 0
                endXPosition = len(yy[0]/n) #yy[0]/n = the length of a single block 
                endYPosition = len(yy[0]/n)
        #after this, do a big for loop in range (0,n) - this is looping through the squares 
                for rows in range(0,n): #looping through the rows 
                    while endYPosition <= len(yy[0]): #everything from yy[startX]... to endYPosition three lines below is one row 
                        #taking us through each square in a single row to cover all the columns 
                        yy[startXPosition:endXPosition][startYPosition:endYPosition][colorChan] = zz[rowscols]
                        #changing color of each square
                        startYPosition+=len(yy[0]/n) 
                        endYPosition+=len(yy[0]/n)
                    startYPosition = 0
                    endYPosition = len(yy[0]/n)
                    #two above lines are re-initializing the Y values 
                    startXPosition += len(yy[0]/n)
                    endXPosition += len(yy[0]/n)
                    #incrementing x values 

mplpy.imshow(zz)