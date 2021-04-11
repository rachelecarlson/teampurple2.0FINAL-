import numpy as np
import psychopy as py
import matplotlib as mpl 
import pandas as pd 
import skimage as sk
import matplotlib.pyplot as mplpy 
import cv2

numBlocks = 3 #number of blocks in rows or columns (so n = 3 is a 3x3 grid) 
gridSize = 150 #overall pixels in grid 
GridType = 2
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
    
    trialType = np.random.randint(GridType) #if trial type =1 harmonious, if 2, disharmonious
    groundtruth.append(trialType) #trying to concatonate
    trialType = 1 #?

    if trialType == 1: # harmonious -----------------------------
        c = np.random.randint(3) #for harmonious grid (picking one color channel and random int within that color)
        yy = np.zeros((gridSize,gridSize,3), dtype=np.uint8) #the 3 is for color channels 
        #two parenthesis, because we want it to know that it's a tuple (two separate entities)
        colorChannelPicked = c
        #attempting more sustainable code, using matrix instead of hard code 
        zz = np.random.randint(255, size=(numBlocks,numBlocks)) ##for saturation 
        #we could also make one vector 
        resizedChannel = cv2.resize(zz.astype(np.uint8), (gridSize,gridSize), interpolation=cv2.INTER_NEAREST_EXACT)
        #interpolation has to due with the way the blocks blend together, so interpolation=cv2.INTER_NEAREST_EXACT means 
        #that the blocks are distinct (not tye-dye looking)
        yy[:,:,c] = resizedChannel


        mplpy.imshow(yy)
        mplpy.show()
        mplpy.imshow(blankMat)
        mplpy.show()
        pause(3)
        GridSD = np.random.randint(nTrialTypes)
        GridSD = 1
        samedifferent.append(GridSD)
        if trialType == 2: #Show the same thing -----------------------
            mplpy.imshow(yy) #showing same grid
            mplpy.show() 
            blankMat = np.zeros(150)
            mplpy.imshow(blankMat)
            mplpy.show()
            pause(3)
        else: 
            #two parenthesis, because we want it to know that it's a tuple (two separate entities)
            #attempting more sustainable code, using matrix instead of hard code 
            zz = np.random.randint(255, size=(numBlocks,numBlocks)) ##for saturation 
            funkyLegoLen = np.random.randint(0,gridSize+1,size=None, dType=np.uint8)
            funkyLegoWid = np.random.randint(0,gridSize+1,size=None, dType=np.uint8)
            FunkyLegoGrid = zz(funkyLegoLen,funkyLegoWid,np.random.randint(255,colorChannelPicked))
            #we could also make one vector 
            resizedChannel = cv2.resize(zz.astype(np.uint8), (gridSize,gridSize), interpolation=cv2.INTER_NEAREST_EXACT)
            #interpolation has to due with the way the blocks blend together, so interpolation=cv2.INTER_NEAREST_EXACT means 
            #that the blocks are distinct (not tye-dye looking)
            yy[:,:,c] = resizedChannel



