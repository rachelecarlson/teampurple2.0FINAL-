import numpy as np
#import psychopy as py
import matplotlib as mpl 
import pandas as pd 
import skimage as sk
import matplotlib.pyplot as mplpy 
import cv2

numBlocks = 3 #number of blocks in rows or columns (so n = 3 is a 3x3 grid) 
gridSize = 150 #overall pixels in grid 
nTrialTypes = 2

counter = 1
print('Instructions: In each round, two colored grids will be displayed (one after the other). When prompted, indicate whether the two grids were the same or different.')
answer_vector = []
groundtruth = [] #keeping track of whether the grid is disharmonious or harmonious
samedifferent = [] #keeping track of whether the grid was the same or different in the trial

while counter <= 5: #the program will run for 5 rounds 
    counter += 1
    blankMat = np.zeros((gridSize,gridSize))
    #mplpy.imshow(blankMat.astype(np.uint8))
    #mplpy.pause(3)
    
    trialType = np.random.randint(nTrialTypes) #if trial type =1 harmonious, if 2, disharmonious
    groundtruth.append(trialType) #trying to concatonate
    trialType = 1

    if trialType == 1:
        c = np.random.randint(3) #for harmonious grid (picking one color channel and random int within that color)
        yy = np.zeros((gridSize,gridSize,3), dtype=np.uint8) #the 3 is for color channels 
        #two parenthesis, because we want it to know that it's a tuple (two separate entities)

        #attempting more sustainable code, using matrix instead of hard code 
        zz = np.random.randint(255, size=(numBlocks,numBlocks)) ##for saturation 
        #we could also make one vector 
        resizedChannel = cv2.resize(zz.astype(np.uint8), (gridSize,gridSize), interpolation=cv2.INTER_NEAREST_EXACT)
        #interpolation has to due with the way the blocks blend together, so interpolation=cv2.INTER_NEAREST_EXACT means 
        #that the blocks are distinct (not tye-dye looking)
        yy[:,:,c] = resizedChannel

        # for colorChan in range(3): ## will go through all 9 squares in red, g, b channels
        #     for rowscols in range(0,len(zz)):
        #      #make sure it's going through all 9 of the squares, not just one dimension 
             
        #         #initialize start position 
        #         startXPosition = 0 #starting a first block at 0,0 -- we may need to specifiy the x and y here 
        #         startYPosition = 0
        #         endXPosition = len(yy[0]/n) #yy[0]/n = the length of a single block 
        #         endYPosition = len(yy[0]/n)
        # #after this, do a big for loop in range (0,n) - this is looping through the squares 
        #         for rows in range(0,n): #looping through the rows 
        #             while endYPosition <= len(yy[0]): #everything from yy[startX]... to endYPosition three lines below is one row 
        #                 #taking us through each square in a single row to cover all the columns 
        #                 yy[startXPosition:endXPosition][startYPosition:endYPosition][colorChan] = zz[rowscols]
        #                 #changing color of each square
        #                 startYPosition+=len(yy[0]/n) 
        #                 endYPosition+=len(yy[0]/n)
        #             startYPosition = 0
        #             endYPosition = len(yy[0]/n)
        #             #two above lines are re-initializing the Y values 
        #             startXPosition += len(yy[0]/n)
        #             endXPosition += len(yy[0]/n)
        #             #incrementing x values 

        mplpy.imshow(yy)
        mplpy.show()