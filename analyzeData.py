#plot the files we've saved 

import pickle
import matplotlib as mpl 
import matplotlib.pyplot as mplpy
import numpy as np


confusionMatrix = np.zeros((2,2)) #data for each participant 
totalTrials = np.zeros((2,2)) #KEEPING TRACK OF TOTAL # OF TRIALS 
#2x2 since we have rows harm or disharm, and columns same or different 

for subjectID in range(4): #if we have 10 participants 
    data = pickle.load(open('subject_{}.p'.format(subjectID), 'rb')) #reading (rb)
    confusionMatrix += data['confmat'] #accessing the values we've saved in gridTrials file 
    #collapsing data across all participants 
    totalTrials += data['total']

confusionMatrix = confusionMatrix/totalTrials
#measures accuracy 


#x labels s/d, y labels h/d  

fig, ax = mplpy.subplots()
im = ax.imshow(confusionMatrix)

sameDiff = ['same', 'different']
harmDisharm = ['harmonious', 'disharmonious']

ax.set_xticklabels(sameDiff) ax.set_yticklabels(harmDisharm)


for i in range(len(harmDisharm)):
    for j in range(len(sameDiff)):
        text = ax.text(j,i, confusionMatrix[i,j], ha = "center", va ="center", color="w")

ax.set_title("Accuracy for Harmonious and Disharmonious Color Schemes")
fig.tight_layout()
mplpy.show()