import numpy as np
import psychopy as py
import matplotlib as mpl 
import pandas as pd 
from skimage.color import rgb2hsv, hsv2rgb 
import matplotlib.pyplot as mplpy 
import cv2

numBlocks = 3 #number of blocks in rows or columns (so n = 3 is a 3x3 grid) 
gridSize = 150 #overall pixels in grid 
GridType = 2
nTrialTypes = 2
useHSV = True #flag that will indicate if you want to work in HSV or RGB space 



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
    
    trialType = np.random.randint(GridType) #if trial type =1 harmonious, if 2, disharmonious
    groundtruth.append(trialType) #trying to concatonate
    trialType = 1 #?

    if trialType == 1: # harmonious -----------------------------
        if useHSV: 
            randomHue = np.random.rand() #for harmonious grid (picking one color channel and random int within that color)
            # c should give number between 0 and 1 for HUE
            for satLoop in range(0, numBlocks):
                numBlocks[satLoop] = np.random.randint(255, size=(numBlocks,numBlocks))
                randomSat = numBlocks ##for saturation 
            randomValue = np.random.rand()

            resizedChannel = cv2.resize(randomSat.astype(np.uint8), (gridSize,gridSize), interpolation=cv2.INTER_NEAREST_EXACT)
                #interpolation has to due with the way the blocks blend together, so interpolation=cv2.INTER_NEAREST_EXACT means 
                #that the blocks are distinct (not tye-dye looking)
            displayImage = np.zeros((gridSize,gridSize,3), dtype=np.float32) #the 3 is for color channels 
            displayImage[:,:,0] += randomHue 
            displayImage[:,:,1] = resizedChannel
            displayImage[:,:,2] += randomValue
    
            RGBImage = hsv2rgb(displayImage)
        else: 
            pass 


        mplpy.imshow(RGBImage)
        mplpy.show()
       
        mplpy.imshow(blankMat)
        mplpy.show()

        pause(3)
        GridSD = np.random.randint(nTrialTypes)
        GridSD = 1
        samedifferent.append(GridSD)
        if GridSD == 3: #Show the same harmonious grid as user just saw -----------------------
            mplpy.imshow(yy) #showing same grid
            mplpy.show() 
            pause(3)

            blankMat = np.zeros(150)
            mplpy.imshow(blankMat)
            mplpy.show()
            pause(3)

        else: #if GridSD == 4, show the original harmonious grid, with one lego different  
            #two parenthesis, because we want it to know that it's a tuple (two separate entities)
            #attempting more sustainable code, using matrix instead of hard code 
            #zz = np.random.randint(255, size=(numBlocks,numBlocks)) ##for saturation 
            funkyLegoLen = np.random.randint(0,gridSize+1,size=None, dType=np.uint8)
            funkyLegoWid = np.random.randint(0,gridSize+1,size=None, dType=np.uint8)
            FunkyLegoGrid = yy
            FunkyLegoGrid[funkyLegoLen,funkyLegoWid,1] = np.random.rand()
            #1 is the HUE... np.random.rand() 
            resizedChannel = cv2.resize(FunkyLegoGrid.astype(np.uint8), (gridSize,gridSize), interpolation=cv2.INTER_NEAREST_EXACT)
            #interpolation has to due with the way the blocks blend together, so interpolation=cv2.INTER_NEAREST_EXACT means 
            #that the blocks are distinct (not tye-dye looking)
            #yy[:,:,c] = resizedChannel

    #if trialType == 2:



