import numpy as np
import psychopy as py
import matplotlib as mpl 
import pandas as pd 
from skimage.color import rgb2hsv, hsv2rgb 
import matplotlib.pyplot as mplpy 
import cv2
from copy import deepcopy

numBlocks = 3 #number of blocks in rows or columns (so n = 3 is a 3x3 grid) 
gridSize = 200 #overall pixels in grid 
GridType = 2 #there are two options for grids––same grid or different grid
nTrialTypes = 2 #there are two options for trial types––harmonious or disharmonious
useHSV = True #flag that will indicate if you want to work in HSV or RGB space 



counter = 0
print('Instructions: In each round, two colored grids will be displayed (one after the other). When prompted, indicate whether the two grids were the same or different.')
UserAnswerList = []
CorrectHarmDisharmList = [] #keeping track of whether the grid is disharmonious or harmonious
CorrectAnswerList = [] #keeping track of whether the grid was the same or different in the trial

while counter <= 2: #the program will run for 4 rounds 
    counter += 1
    blankMat = np.zeros((gridSize,gridSize))
    #mplpy.imshow(blankMat.astype(np.uint8))
    #mplpy.pause(3)
    
    trialType = np.random.randint(GridType) #if trial type =1 harmonious, if 2, disharmonious
    CorrectHarmDisharmList.append(trialType) #trying to concatonate
    #trialType = 1 #right now, just shortcut for it to be 1 -- once we have code for trialType = 2 we can delete

    #import ipdb; ipdb.set_trace()

    if trialType == 0: # harmonious -----------------------------
        print('harmonious')
        if useHSV: 
            randomHue = np.random.rand() #for harmonious grid (picking one color channel and random int within that color)
            # c should give number between 0 and 1 for HUE
            #for satLoop in range(0, numBlocks):
                #numBlocks[satLoop] = np.random.randint(255, size=(numBlocks,numBlocks))
                #randomSat = numBlocks
            randomSat = np.random.rand(numBlocks,numBlocks)
            #randomSat creates a numB by numBlocks matrix, filled with values from 0 to 1  
            randomValue =  0.2 * np.random.rand() + 0.8 #making sure that the value is never 0
            #resizedChannel = cv2.resize(randomSat.astype(np.uint8), (gridSize,gridSize), interpolation=cv2.INTER_NEAREST_EXACT)
                #interpolation has to due with the way the blocks blend together, so interpolation=cv2.INTER_NEAREST_EXACT means 
                #that the blocks are distinct (not tye-dye looking)
            displayImage = np.zeros((numBlocks,numBlocks,3), dtype=np.float32) #the 3 is for color channels 
            displayImage[:,:,0] += randomHue #+= because randomHue is a single number, not a matrix
            displayImage[:,:,1] = randomSat #randomSat is a matrix 
            displayImage[:,:,2] += randomValue
    
            RGBImage = hsv2rgb(displayImage) * 255
            RGBImage = cv2.resize(RGBImage.astype(np.uint8), (gridSize,gridSize), interpolation=cv2.INTER_NEAREST_EXACT)
                
        else: 
            pass 


        mplpy.imshow(RGBImage)
        mplpy.axis('off')
        mplpy.pause(3)
       
        mplpy.imshow(blankMat)
        mplpy.axis('off')
        mplpy.pause(3)

        GridSD = np.random.randint(nTrialTypes)
        CorrectAnswerList.append(GridSD)

        if GridSD == 0: #Show the same harmonious grid as user just saw -----------------------
            print('Harmonious Same')
            mplpy.imshow(RGBImage) #showing same grid
            mplpy.axis('off')
            mplpy.pause(3)

            mplpy.imshow(blankMat)
            mplpy.axis('off')
            mplpy.pause(3)

        else: #if GridSD == 1, show the original harmonious grid, with one lego different  
            #attempting more sustainable code, using matrix instead of hard code 
            #zz = np.random.randint(255, size=(numBlocks,numBlocks)) ##for saturation 
            print('Harmonious Different')
            funkyLegoX = np.random.randint(numBlocks)
            funkyLegoY = np.random.randint(numBlocks)
            funkyLegoGrid = deepcopy(displayImage)

            # change saturation for a randomly selected pixel
            funkyLegoGrid[funkyLegoX, funkyLegoY, 1] = np.random.rand()
            funkyLegoGrid = hsv2rgb(funkyLegoGrid) * 255  
            funkyLegoGrid = cv2.resize(funkyLegoGrid.astype(np.uint8), (gridSize,gridSize), interpolation=cv2.INTER_NEAREST_EXACT)
             
            mplpy.imshow(funkyLegoGrid) #showing same grid
            mplpy.axis('off')
            mplpy.pause(3)

            mplpy.imshow(blankMat)
            mplpy.axis('off')
            mplpy.pause(3)
        
        UserInput = input("End of Round! Type 's' if the two grids were the same. Type 'd' if the grids were different. Enter response here: ") 
        if UserInput == 's': 
            UserAnswerList.append(0)
        elif UserInput == 'd': 
            UserAnswerList.append(1)
        else: 
            UserAnswerList.append('null')
    
    else: #if trialType == 1 --> disharmonious grid 
        if useHSV:
            print("disharmonious")
            randomHue = np.random.rand(numBlocks,numBlocks) #picking one color channel and random int within that color
            # c should give number between 0 and 1 for HUE
            randomSat = np.random.rand(numBlocks, numBlocks)
            #randomSat creates a numB by numBlocks matrix, filled with values from 0 to 1  
            randomValue =  0.2 * np.random.rand() + 0.8 #making sure that the value is never 0
            #resizedChannel = cv2.resize(randomSat.astype(np.uint8), (gridSize,gridSize), interpolation=cv2.INTER_NEAREST_EXACT)
            displayImage = np.zeros((numBlocks,numBlocks,3), dtype=np.float32) #the 3 is for color channels 
            displayImage[:,:,0] = randomHue #+= because randomHue is a single number, not a matrix
            displayImage[:,:,1] = randomSat #randomSat is a matrix 
            displayImage[:,:,2] += randomValue
    
            RGBImage = hsv2rgb(displayImage) * 255
            RGBImage = cv2.resize(RGBImage.astype(np.uint8), (gridSize,gridSize), interpolation=cv2.INTER_NEAREST_EXACT) 
        
        else: 
            pass 

        mplpy.imshow(RGBImage)
        mplpy.axis('off')
        mplpy.pause(3)
        
        mplpy.imshow(blankMat)
        mplpy.axis('off')
        mplpy.pause(3)
        

        GridSD = np.random.randint(nTrialTypes)
        CorrectAnswerList.append(GridSD)
    
        if GridSD == 0: #Show the same disharmonious grid as user just saw -----------------------
            print('Disharmonious Same')
                
            mplpy.imshow(RGBImage) #showing same grid
            mplpy.axis('off')
            mplpy.pause(3)

            mplpy.imshow(blankMat)
            mplpy.axis('off')
            mplpy.pause(3)

        else: #if GridSD == 1, show the original disharmonious grid, with one lego different  
            print('Disharmonious Different')
            funkyLegoX = np.random.randint(numBlocks)
            funkyLegoY = np.random.randint(numBlocks)
            funkyLegoGrid = deepcopy(displayImage)

            # change hue and saturation for a randomly selected pixel
            funkyLegoGrid[funkyLegoX, funkyLegoY, 0] = np.random.rand()
            funkyLegoGrid[funkyLegoX, funkyLegoY, 1] = np.random.rand()
            funkyLegoGrid = hsv2rgb(funkyLegoGrid) * 255  
            funkyLegoGrid = cv2.resize(funkyLegoGrid.astype(np.uint8), (gridSize,gridSize), interpolation=cv2.INTER_NEAREST_EXACT)
             
            mplpy.imshow(funkyLegoGrid) #showing the new disharmonious grid
            mplpy.axis('off')
            mplpy.pause(3)

            mplpy.imshow(blankMat)
            mplpy.axis('off')
            mplpy.pause(3)
    
        UserInput = input("End of Round! Type 's' if the two grids were the same. Type 'd' if the grids were different. Enter response here: ") 
        if UserInput == 's': 
            UserAnswerList.append(0)
        elif UserInput == 'd': 
            UserAnswerList.append(1)
        else: 
            UserAnswerList.append('null')
        
    
        User_Correct_Harm = [] #not dependent on the user
        ##for researchers to keep track if user got it right or wrong in harmonious or disharmonious trials 
        User_Correct_Disharmonious = [] 



        # if CorrectHarmDisharmList == 0 and UserAnswerList == 0 and CorrectAnswerList == 0: 
        #     #if the program picked harmonious grid, and user said it is the same (0), and the two grids were the same 
        #     User_Correct_Harm.append('harmonious correct')
        # elif CorrectHarmDisharmList == 0 and UserAnswerList ==1 and CorrectAnswerList == 1:
        #     #if the program picks harmonious, and user said it is diff and the two grids were different 
        #     User_Correct_Harm.append('harmonious correct')
        # elif CorrectHarmDisharmList == 0 and UserAnswerList ==1 and CorrectAnswerList == 0:
        #     #if the program picked harmonious, and user says it is different, but the two grids were the same 
        #     User_Correct_Harm.append('harmonious incorrect') 
        # elif CorrectHarmDisharmList == 0 and UserAnswerList ==0 and CorrectAnswerList == 1:
        #     #if the program picked harmioniuos, and user says same, and two grids were different
        #     User_Correct_Harm.append('harmonious incorrect')
        # elif CorrectHarmDisharmList == 1 and UserAnswerList == 0 and CorrectAnswerList == 0: 
        #     #if the program picked disharmonious grid, and user said it is the same (0), and the two grids were the same 
        #     User_Correct_Disharmonious.append('disharmonious correct')
        # elif CorrectHarmDisharmList == 1 and UserAnswerList ==1 and CorrectAnswerList == 1:
        #     #if the program picks disharmonious, and user said it is diff and the two grids were different 
        #     User_Correct_Disharmonious.append('disharmonious correct')
        # elif CorrectHarmDisharmList == 1 and UserAnswerList ==1 and CorrectAnswerList == 0:
        #     #if the program picked disharmonious, and user says it is different, but the two grids were the same 
        #     User_Correct_Disharmonious.append('disharmonious incorrect') 
        # elif CorrectHarmDisharmList == 1 and UserAnswerList ==0 and CorrectAnswerList == 1:
        #     #if the program picked disharmioniuos, and user says same, and two grids were different
        #     User_Correct_Disharmonious.append('disharmonious incorrect')

        for ii in range(len(UserAnswerList)):
            if UserAnswerList[ii] == CorrectAnswerList[ii] and CorrectHarmDisharmList == 0:
                User_Correct_Harm.append('harmonious correct')
            elif UserAnswerList[ii] == CorrectAnswerList[ii] and CorrectHarmDisharmList == 1: 
                User_Correct_Disharmonious.append('disharmonious correct')
            elif UserAnswerList[ii] != CorrectAnswerList[ii] and CorrectHarmDisharmList == 0:
                User_Correct_Harm.append('harmonious incorrect')
            elif UserAnswerList[ii] != CorrectAnswerList[ii] and CorrectHarmDisharmList == 1:
                User_Correct_Disharmonious.append('disharmonious incorrect')

        
        
        
print('this is user answer list', UserAnswerList)
print('this is whether grid was actually harm or disharm', CorrectHarmDisharmList) #harmonious = 0, and disharmonious = 1 
print('this is whether the program picked s or d grid', CorrectAnswerList) #same = 0, and different grid = 1 
print('this is whether user got correct answer when harmonious grid', User_Correct_Harm)
print('this is whether user got correct answer when disharmonious grid', User_Correct_Disharmonious)
    





#attempting to compare UserAnswerList to the correctAnswerList (for same/different and for harmonious/disharmonious)

# User_Correct_Harm = [] 
# for yy in range(len(UserAnswerList)): 
#     if UserAnswerList[yy] == User_Correct_Harm[yy]: 
#         User_Correct_Harm.append('correct harmonious')
#     else: 
#         User_Correct_Harm.append('incorrect harmonious')
        
# print(User_Correct_Harm)

# User_Correct_Disharmonious = []
# for zz in range(len(UserAnswerList)): 
#     if UserAnswerList[zz] == User_Correct_Disharmonious[zz]: 
#         User_Correct_Disharmonious.append('correct disharmonious')
#     else: 
#         User_Correct_Disharmonious.append('incorrect disharmonious')
        
# print(User_Correct_Disharmonious)
        



