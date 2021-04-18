##plot the files we've saved 

import pickle
import matplotlib as mpl 
import matplotlib.pyplot as mplpy
import numpy as np


confusionMatrix = np.zeros((2,2)) #data for each participant 
totalTrials = np.zeros((2,2)) #KEEPING TRACK OF TOTAL # OF TRIALS 
#2x2 since we have rows harm or disharm, and columns same or different 

for subjectID in range(7): #if we have 7 participants 
    data = pickle.load(open('subject_{}.p'.format(subjectID), 'rb')) #reading (rb)
    confusionMatrix += data['confmat'] #accessing the values we've saved in gridTrials file 
    #collapsing data across all participants 
    totalTrials += data['total']

confusionMatrix = confusionMatrix/totalTrials
#measures accuracy 


#x labels s/d, y labels h/d  

fig, ax = mplpy.subplots()
im = ax.imshow(confusionMatrix)

sameDiff = ["Same", "Different"]
harmDisharm = ["Harmonious", "Disharmonious"]

ax.set_xticks(np.arrange(len(sameDiff)) 
ax.set_yticks(np.arrange(len(harmDisharm)
ax.set_xticklabels(sameDiff, fontsize=10) 
ax.set_yticklabels(harmDisharm, fontsize=10)
mplpy.setp(ax.get_xticklabels(), rotation=0, ha="right", rotation_mode="anchor")


for i in range(len(harmDisharm)):
    for j in range(len(sameDiff)):
        text = ax.text(j,i, confusionMatrix[i,j], ha = "center", va ="center", color="b")

ax.set_title("Participant Accuracy by Trial Type in Color Relations Experiment", fontweight = 'bold', fontsize=16)
fig.tight_layout()
mplpy.show()