#close all
#clearvars

import numpy as np
import psychopy as py
import matplotlib as mpl 


counter = 1
print('Instructions: In each round, two colored grids will be displayed (one after the other). When prompted, indicate whether the two grids were the same or different.')
answer_vector = []
groundtruth = [] #keeping track of whether the grid is disharmonious or harmonious
samedifferent = [] #keeping track of whether the grid was the same or different in the trial
while counter <=5: #the program will run for 5 rounds 
    blankMat = np.zeros(150)
    imshow(np.uint8(blankMat))
    pause(3)
    T = randint([1,2],1)
    groundtruth = [groundtruth T] #trying to concatonate 
    if T == 1:
        c = randint(3) %harmonious grid 
        c = np.uint8(c)
        yy = np.zeros(150,150,3)
        yy= np.uint8(yy)
        sat = randint(255)
        sat = np.uint8(sat)
        sat2 = randint(255)
        sat2 = np.uint8(sat2)
        sat3 = randint(255)
        sat3= np.uint8(sat3)
        sat4 = randint(255)
        sat4= np.uint8(sat4)
        sat5 = randint(255)
        sat5= np.uint8(sat5)
        sat6 = randint(255)
        sat6= np.uint8(sat6)
        sat7 = randint(255)
        sat7= np.uint8(sat7)
        sat8 = randint(255)
        sat8= np.uint8(sat8)
        sat9 = randint(255)
        sat9= np.uint8(sat9)
        
        #top left lego
        for current_row in range(0,50)
            for current_col in range (0,50)
                yy(current_row,current_col, c) = sat:
      
        
        #top middle lego
        for current_row in range (0,50)
            for current_col in range (50,100)_
                yy(current_row,current_col, c) = sat2
   

        #top right lego
        for current_row in range (0,50)
            for current_col in range(100:150)
                yy(current_row,current_col, c) = sat3

        
        #middle left lego
        for current_row in range(50:100)
            for current_col in range (0:50)
                yy(current_row,current_col, c) = sat4


        
        #center lego
        for current_row in range(50,100)
            for current_col in range(50:100)
                yy(current_row,current_col, c) = sat5

  
        #middle right
        for current_row in range(50,100)
            for current_col in range(100,150)
                yy(current_row,current_col, c) = sat6
        
        #bottom left
        for current_row in range(100,150)
            for current_col in range (1,50)
                yy(current_row,current_col, c) = sat7
        
        #bottom middle lego
        for current_row in range(100,150)
            for current_col in range(50,100)
                yy(current_row,current_col, c) = sat8


        
        #bottom right lego
        for current_row in range(100:150)
            for current_col in range(100:150)
                yy(current_row,current_col, c) = sat9

        
        
        imshow(np.uint8(yy)) #we are showing harmious grid
        pause(3)
        
        blankMat = np.zeros(150)
        imshow(np.uint8(blankMat))
        pause(3)
       
        #Blank screen
        R = randint([3,4],1)
        samedifferent = [samedifferent, R]
        if R == 3: #if we want to show the exact same grid
            imshow(np.uint8(yy)) #showing same grid
            blankMat = np.zeros(150)
            imshow(np.uint8(blankMat))
            pause(3)
            
            
        else
            
            #funky lego - if we want to change one of the legos---------------
            #harmonious funky lego
            HG = yy
            
            rand_row = randint(3)
            rand_col = randint(3)
            
            if rand_row == 1 and rand_col == 1:
                for current_row in range(0,50):
                    for current_col in range(0,50):
                        HG(current_row,current_col, c) = sat

            elif rand_row == 1 and rand_col == 2:
                for current_row in range(0,50):
                    for current_col in range(50,100):
                        HG(current_row,current_col, c) = sat
 
            elif rand_row == 1 and rand_col == 3:
                for current_row in range(0,50):
                    for current_col in range(100,150):
                        HG(current_row,current_col, c) = sat

            elif rand_row == 2 and rand_col == 1:
                for current_row in range(50,100):
                    for current_col in range(0,50):
                        HG(current_row,current_col, c) = sat
                       
            elif rand_row == 2 and rand_col == 2:
                for current_row in range(50,100):
                    for current_col in range(50,100):
                        HG(current_row,current_col, c) = sat

            elif rand_row == 2 and rand_col == 3:
                for current_row in range(50,100):
                    for current_col in range(100,150):
                        HG(current_row,current_col, c) = sat
                       
            elif rand_row == 3 and rand_col == 1:
                for current_row in range(100,150):
                    for current_col in range(0,50):
                        HG(current_row,current_col, c) = sat

            elif rand_row == 3 and rand_col == 2:
                for current_row in range(100,150):
                    for current_col in range(50,100):
                        HG(current_row,current_col, c) = sat

            elif rand_row == 3 and rand_col == 3:
                for current_row in range(100,150):
                    for current_col in range(100:150)
                        HG(current_row,current_col, c) = sat
  
            
            imshow(np.uint8(HG)) #showing harmonious funky lego
            pause(3)
            
            blankMat = np.zeros(150)
            imshow(np.uint8(blankMat))
            pause(3)
            
            
         #end for if statement within big if statement
    else:
        c = randint(3) #%% disharmonious grid
        c = np.uint8(c)
        cc = randint(3)
        if cc == c and c == 1:
            cc = randint([2, 3], 1)
        elif cc == c and c == 2:
            cc = randint([1, 3], 1)
        elif cc==c and c == 3:
            cc = randint([1, 2], 1)
        else
        #end 

        xx = zeros(150,150,3)
        xx= np.uint8(xx)
        sat = randint(255)
        sat = np.uint8(sat)
        sat2 = randint(255)
        sat2 = np.uint8(sat2)
        sat3 = randint(255)
        sat3= np.uint8(sat3)
        sat4 = randint(255)
        sat4= np.uint8(sat4)
        sat5 = randint(255)
        sat5= np.uint8(sat5)
        sat6 = randint(255)
        sat6= np.uint8(sat6)
        sat7 = randint(255)
        sat7= np.uint8(sat7)
        sat8 = randint(255)
        sat8= np.uint8(sat8)
        sat9 = randint(255)
        sat9= np.uint8(sat9)
        
        #top left lego
        for current_row in range(0,50):
            for current_col in range(0,50):
                xx(current_row,current_col, c) = sat
        
        #top middle lego
        for current_row in range(0:50):
            for current_col in range(50:100):
                xx(current_row,current_col, c) = sat2
        
        #top right lego
        for current_row in range(0,50):
            for current_col in range(100,150):
                xx(current_row,current_col, cc) = sat3
               
        
        #middle left lego
        for current_row in range(50,100):
            for current_col in range(0,50):
                xx(current_row,current_col, c) = sat4
            
        
        #center lego
        for current_row in range(50,100):
            for current_col in range(50,100):
                xx(current_row,current_col, c) = sat5
              
        
        #middle right
        for current_row in range(50,100):
            for current_col in range(100,150):
                xx(current_row,current_col, cc) = sat6
              
        
        #bottom left
        for current_row in range(100,150):
            for current_col in range(1,50):
                xx(current_row,current_col, cc) = sat7
               
        
        #bottom middle lego
        for current_row in range(100,150):
            for current_col in range(50,100):
                xx(current_row,current_col, c) = sat8
              
        
        #bottom right lego
        for current_row in range(100,150):
            for current_col in range(100,150):
                xx(current_row,current_col, cc) = sat9
        
        
        
        imshow(np.uint8(xx)) %showing disharmonious grid
        pause(3)
        
        blankMat = np.zeros(150)
        imshow(np.uint8(blankMat))
        pause(3)
        
        #Blank screen
        Rr = randint([5,6], 1)
        if Rr == 5: #if we want to keep the same disharmonious grid
            imshow(np.uint8(xx)) % showing same disharmonious grid
        else #disharmonious funky lego code
            
            DG = xx
            
            rand_row = randint(3)
            rand_col = randint(3)
            
            if rand_row == 1 and rand_col == 1:
                for current_row in range(0,50):
                    for current_col in range(0,50):
                        DG(current_row,current_col, cc) = sat
                        
            elif rand_row == 1 and rand_col == 2:
                for current_row in range(0,50):
                    for current_col in range(50,100):
                        DG(current_row,current_col, cc) = sat
                       
            elif rand_row == 1 and rand_col == 3:
                for current_row in range(0,50):
                    for current_col in range(100,150):
                        DG(current_row,current_col, cc) = sat
                       
            elif rand_row == 2 and rand_col == 1:
                for current_row in range(50,100):
                    for current_col in range(0,50):
                        DG(current_row,current_col, cc) = sat
                      
            elif rand_row == 2 and rand_col == 2:
                for current_row in range(50,100):
                    for current_col in range(50,100):
                        DG(current_row,current_col, cc) = sat
                    
            elif rand_row == 2 and rand_col == 3:
                for current_row in range(50,100):
                    for current_col in range(100,150)
                        DG(current_row,current_col, cc) = sat
                        
            elif rand_row == 3 and rand_col == 1:
                for current_row in range(100,150):
                    for current_col in range(0,50):
                        DG(current_row,current_col, cc) = sat
                        
            elif rand_row == 3 and rand_col == 2:
                for current_row in range(100,150):
                    for current_col in range(50,100):
                        DG(current_row,current_col, cc) = sat
                       
            elif rand_row == 3 and rand_col == 3:
                for current_row in range(100,150)
                    for current_col in range(100,150):
                        DG(current_row,current_col, cc) = sat
                        
            imshow(np.uint8(DG)) #showing disharmonious funky lego
            pause(3)
            
            blankMat = np.zeros(150)
            imshow(np.uint8(blankMat))
            pause(3)
            

    clc
    prompt = ('End of Round. \n Type ‘s’ if the two grids were the same. \n Type ‘d’ if the grids were different. \n Enter response here: ');
    x =  input(prompt,'s')
    answer_vector = [answer_vector, x]
    counter = counter+1

print('answer_vector: ')
print(answer_vector)
print('sub01_ans', 'answer_vector')
save('sub01_groundtruth', 'groundtruth')
save('sub01_samedifferent', 'samedifferent')

