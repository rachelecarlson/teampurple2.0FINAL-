##plot the files we've saved 

import pickle
import matplotlib as mpl 
import matplotlib.pyplot as mplpy
import numpy as np
import seaborn as sb
from matplotlib import colors 



confusionMatrix = np.zeros((2,2)) #data for each participant 
totalTrials = np.zeros((2,2)) #KEEPING TRACK OF TOTAL # OF TRIALS 
#2x2 since we have rows harm or disharm, and columns are either same or different 


for subjectID in range(6): #if we have 6 participants 
    data = pickle.load(open('subject_{}.p'.format(subjectID), 'rb')) #reading (rb)
    confusionMatrix += data['confmat'] #accessing the values we've saved in gridTrials file 
    #collapsing data across all participants 
    totalTrials += data['total']

confusionMatrix = confusionMatrix/totalTrials
confusionMatrix = np.around(confusionMatrix, decimals=3)
#measures accuracy 


#x labels same/different, y labels harmonious/disharmonious  

fig, ax = mplpy.subplots()
im = ax.imshow(confusionMatrix, cmap = 'YlOrRd')

 
sameDiff = ["Same", "Different"]
harmDisharm = ["Harmonious", "Disharmonious"]
 
ax.set_xticks(np.arange(len(sameDiff)))
ax.set_yticks(np.arange(len(harmDisharm)))
ax.set_xticklabels(sameDiff, fontsize=12) 
ax.set_yticklabels(harmDisharm, fontsize=12)
mplpy.setp(ax.get_xticklabels(), rotation=0, ha="right", rotation_mode="anchor")

#fill in the grid with data from confusionMatrix 
for i in range(len(harmDisharm)):
    for j in range(len(sameDiff)):
        text = ax.text(j,i, confusionMatrix[i,j], ha = "center", va ="center", color="k", fontsize = 18)

ax.set_title("Participant Accuracy by Trial Type in Color Relations Experiment", fontweight = 'bold', fontsize=16)
fig.tight_layout()
mplpy.show()

