# teampurple2.0FINAL-
the repository for team purple 2.0 final project in CLPS 0950 

**IMPORTANT DOCUMENTS:**

The document **gridTrials.py** is the file that runs the actual experiment with color grids and option for participant input, while the **analyzeData.py** file should be used to analyze participant data. 

**TOOLBOXES/DOWNLOADS: **

In order to run this experiment in the gridTrials file, researchers would need to import numpy as np, matplotlib as mpl, hsv2rgb and rgb2hsv from skimage.color, matplotlib.pyplot as mplpy, pickle, cv2, deepcopy from copy, and pickle.  

In order to plot the data in the analyzeData file, researchers would need to import pickle, matplotlib as mpl, matplotlib.pyplot as mplpy, numpy as np, seaborn as sb, and colors from matplotlib. 

**BACKGROUND/USER INFORMATION: **

The program randomly fills a matrix (of adjustable dimensions, default 3x3) with blocks of either harmonious or disharmonious colors – harmonious color schemes have the program choose a random hue, and then create a grid full of different saturations of that hue. For disharmonious rounds, all of the hues and saturations are randomly selected. Then in the second part of the trial, the program randomly selects to either show the participant the same harmonious/disharmonious grid again (a “same” round), or pick one random grid-unit to change (a “different” round). In a harmonious different round, only the saturation value is changed so the altered grid-unit is still in the harmonious color scheme. In a disharmonious different round, the hue and saturation of one grid-unit change so it becomes a different random color that is not harmonious with the other grid-units. 

Researchers could run this program with any number of participants (just changing the SUBJECT ID at the top each time), with any grid size/number of grid blocks (i.e. 2x2 grid or a 100x100 grid, or anything else they choose by changing the variable “numBlocks”), and with any number of trials per round (i.e., the number of times the participant will be asked to input an answer). 

Again, participant data is tracked with the variable subjectID. At the beginning of each experiment with a new subject, the researcher should update subjectID so as to save new data without working over old user data. At present, we had six users participate, so line 17 in analyzeData.py says for subjectID in range(6). This can be changed if researchers were to add more subjects (as long as they had updated the subjectID in the gridTrials file each time they ran the experiment with a new subject. 

When participants take the program, they are prompted in the command window after each “round” (pair of grids) to enter whether they thought they saw the same grid twice, or two different grids (program waits for “s” or “d” keystroke and saves response). 

