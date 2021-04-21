import numpy as np
import matplotlib as mpl 
from skimage.color import rgb2hsv, hsv2rgb 
import matplotlib.pyplot as mplpy 
import cv2
from copy import deepcopy
import pickle   

numBlocks = 3 #number of blocks in rows or columns (so numBlocks = 3 is a 3x3 grid) 
gridSize = 200 #overall pixels in the grid 
GridType = 2 #there are two options for grids––same grid or different grid
nTrialTypes = 2 #there are two options for trial types––harmonious or disharmonious
useHSV = True #flag that will indicate if you want to work in HSV or RGB space 
subjectID = 7 #each time you run a different person, update this :) 


counter = 0
print('Instructions: In each round, two colored grids will be displayed (one after the other). When prompted, indicate whether the two grids were the same or different.')
UserAnswerList = [] #tracks users answers after each round (same or different)
CorrectHarmDisharmList = [] #keeping track of whether the grid is disharmonious or harmonious
CorrectAnswerList = [] #keeping track of whether the grid was the same or different in the trial

while counter <= 9: #the program will run for 10 rounds 
    counter += 1
    blankMat = np.zeros((gridSize,gridSize)) #blank matrix to fill later 
    
    trialType = np.random.randint(GridType) #if trial type =0 harmonious, if 1, disharmonious
    CorrectHarmDisharmList.append(trialType) #keeps track of whether grid was harmonious or disharm


    if trialType == 0: # harmonious grid 
        #print('harmonious') 
        # print the above if you want to keep track of what is being shown throughout the trial (only for researcher use, not participant)
        if useHSV: 
            randomHue = np.random.rand() #for harmonious grid (picking one color channel and random int within that color)
            # c should give number between 0 and 1 for HUE

            randomSat = np.random.rand(numBlocks,numBlocks)
            #randomSat creates a numB by numBlocks matrix, filled with values from 0 to 1  
            randomValue =  0.2 * np.random.rand() + 0.8 
            #making sure that the value is never 0
        
            displayImage = np.zeros((numBlocks,numBlocks,3), dtype=np.float32) #the 3 is for color channels 
            
            displayImage[:,:,0] += randomHue 
            #filling displayImage with random hue 
            #+= because randomHue is a single number, not a matrix 
            displayImage[:,:,1] = randomSat #randomSat is a matrix 
            #fill display image with random sat within the same Hue value as was chosen above 
            displayImage[:,:,2] += randomValue


            #image created in HSV, but must be shown in RGB 
            RGBImage = hsv2rgb(displayImage) * 255
            RGBImage = cv2.resize(RGBImage.astype(np.uint8), (gridSize,gridSize), interpolation=cv2.INTER_NEAREST_EXACT)
                
        else: #in the future, to add RGB option for users 
            pass 


        mplpy.imshow(RGBImage)
        mplpy.axis('off')
        mplpy.pause(3)
       
       #show blankMat between rounds
        mplpy.imshow(blankMat)
        mplpy.axis('off')
        mplpy.pause(3)

        GridSD = np.random.randint(nTrialTypes) #keeping track of same/different 
        CorrectAnswerList.append(GridSD)

        if GridSD == 0: #Show the same harmonious grid as user just saw 
            #print('Harmonious Same')
            mplpy.imshow(RGBImage) #showing same grid
            mplpy.axis('off')
            mplpy.pause(3)

            mplpy.imshow(blankMat)
            mplpy.axis('off')
            mplpy.pause(3)

        else: #if GridSD == 1, show the original harmonious grid, with one lego different  
            #print('Harmonious Different')

            #funkyLegoX and Y pick a random grid-unit to change 
            funkyLegoX = np.random.randint(numBlocks)
            funkyLegoY = np.random.randint(numBlocks)
            funkyLegoGrid = deepcopy(displayImage)

            # change saturation for the randomly selected pixel
            funkyLegoGrid[funkyLegoX, funkyLegoY, 1] = np.random.rand()
            funkyLegoGrid = hsv2rgb(funkyLegoGrid) * 255  
            funkyLegoGrid = cv2.resize(funkyLegoGrid.astype(np.uint8), (gridSize,gridSize), interpolation=cv2.INTER_NEAREST_EXACT)
             
            mplpy.imshow(funkyLegoGrid) #showing same grid
            mplpy.axis('off')
            mplpy.pause(3)

            mplpy.imshow(blankMat)
            mplpy.axis('off')
            mplpy.pause(3)
        
        #will appear in command window, for user to input answer
        #program will pause until the user inputs answer 
        UserInput = input("End of Round! Type 's' if the two grids were the same. Type 'd' if the grids were different. Enter response here: ") 
        if UserInput == 's': 
            UserAnswerList.append(0)
        elif UserInput == 'd': 
            UserAnswerList.append(1)
        else: 
            UserAnswerList.append('null')
    
    else: #if trialType == 1 --> disharmonious grid 
        if useHSV:
            #print("disharmonious")
            randomHue = np.random.rand(numBlocks,numBlocks) #picking one color channel and random int within that color
            randomSat = np.random.rand(numBlocks, numBlocks)
            #randomSat creates a numB by numBlocks matrix, filled with values from 0 to 1  
            randomValue =  0.2 * np.random.rand() + 0.8 #making sure that the value is never 0
        
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
    
        if GridSD == 0: #Show the same disharmonious grid as user just saw 
            #print('Disharmonious Same')
                
            mplpy.imshow(RGBImage) #showing same grid
            mplpy.axis('off')
            mplpy.pause(3)

            mplpy.imshow(blankMat)
            mplpy.axis('off')
            mplpy.pause(3)

        else: #if GridSD == 1, show the original disharmonious grid, with one lego different  
            #print('Disharmonious Different')
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

#these will print user's answers, correct answers, and whether the grids were harm or disharm 
# can be included in trials if researcher wants immediate feedback, or commented out        
print(UserAnswerList)   
print(CorrectAnswerList)     
print(CorrectHarmDisharmList)

#data for this participant
confusionMatrix = np.zeros((2,2))  

totalTrials = np.zeros((2,2)) #KEEPING TRACK OF TOTAL # OF TRIALS 
#2x2 since we have rows harm or disharm, and columns same or different 

#comparing UserAnswerList (user's answers to the correct answer list)
for k in range(len(UserAnswerList)):
    isCorrect = UserAnswerList[k] == CorrectAnswerList[k]
    if isCorrect: 
        confusionMatrix[CorrectHarmDisharmList[k], CorrectAnswerList[k]] += 1 
        #if correctHarmDisharm list is 0, and correctAnwer...[k] is zero, it was a harmonious trial
        #so update if they answered correctly 
        #recording how many correct trials there were 
    totalTrials[CorrectHarmDisharmList[k], CorrectAnswerList[k]] +=1 
    #this simply keeps track of total trials 



print(confusionMatrix)

data = {'confmat': confusionMatrix, 'total':totalTrials}
#dictionary of confusionMatrix, with two keys (confusionMatrix and totalTrials)
pickle.dump(data, open('subject_{}.p'.format(subjectID), 'wb'))   



     



