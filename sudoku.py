# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 14:11:09 2019

@author: victo_000

Sudoku Solver
"""

"""https://www.kristanix.com/sudokuepic/sudoku-solving-techniques.php"""

import numpy as np
import math
import random as rd
import time

from IPython.display import clear_output

from qol import notify,nl,dc

#grid = np.arange(81).reshape(9,9)

#NUMBER TO ARRAY (COL,LINE,BLOCK)
def whereami(n):
    x = n % 9
    y = math.floor(n/9)
    if y <= 2:
        if x <= 2:
            z=0
        elif x <= 5 and x >= 3:
            z=1
        elif x >= 6:
            z=2
    elif y <= 5 and y >= 3:
        if x <= 2:
            z=3
        elif x <= 5 and x >= 3:
            z=4
        elif x >= 6:
            z=5
    elif y >= 6:
        if x <= 2:
            z=6
        elif x <= 5 and x >= 3:
            z=7
        elif x >= 6:
            z=8
    return [x,y,z]

def list_x(n):
    x = whereami(n)[0]
    return grid[:, x]

def list_y(n):
    y = whereami(n)[1]
    return grid[y, :]       
    
def list_z(n):
    z = whereami(n)[2]
    if z == 0:
        return grid[:3, :3].reshape(-1)
    if z == 1:
        return grid[:3, 3:6].reshape(-1)
    if z == 2:
        return grid[:3, 6:9].reshape(-1)
    if z == 3:
        return grid[3:6, :3].reshape(-1)
    if z == 4:
        return grid[3:6, 3:6].reshape(-1)
    if z == 5:
        return grid[3:6, 6:9].reshape(-1)
    if z == 6:
        return grid[6:9, :3].reshape(-1)
    if z == 7:
        return grid[6:9, 3:6].reshape(-1)
    if z == 8:
        return grid[6:9, 6:9].reshape(-1)

def allowed(n,loc):
    if n in list_x(loc) or n in list_y(loc) or n in list_z(loc):
        return False
    else:
        return True

def allowed_list(loc):
    liste = []
    for i in range(1,9+1):
        if allowed(i,loc) == True:
            liste.append(i)
    return liste

def min_pos(grid):
    minlist = []
    for i in range(81):
        loc = whereami(i)
        if grid[loc[1]][loc[0]] == 0:
            minlist.append(len(allowed_list(i)))
    if minlist == []:
        return 42
    else:
        return min(minlist)

def show(grid):
    print(grid[0][0:3],"|",grid[0][3:6],"|",grid[0][6:9])
    print(grid[1][0:3],"|",grid[1][3:6],"|",grid[1][6:9])
    print(grid[2][0:3],"|",grid[2][3:6],"|",grid[2][6:9])
    print("---------------------------")
    print(grid[3][0:3],"|",grid[3][3:6],"|",grid[3][6:9])
    print(grid[4][0:3],"|",grid[4][3:6],"|",grid[4][6:9])
    print(grid[5][0:3],"|",grid[5][3:6],"|",grid[5][6:9])
    print("---------------------------")
    print(grid[6][0:3],"|",grid[6][3:6],"|",grid[6][6:9])
    print(grid[7][0:3],"|",grid[7][3:6],"|",grid[7][6:9])
    print(grid[8][0:3],"|",grid[8][3:6],"|",grid[8][6:9])

"""

"""

#ez
ez = np.asarray([[5,3,0,0,7,0,0,0,0],
                 [6,0,0,1,9,5,0,0,0],
                 [0,9,8,0,0,0,0,6,0],
                 [8,0,0,0,6,0,0,0,3],
                 [4,0,0,8,0,3,0,0,1],
                 [7,0,0,0,2,0,0,0,6],
                 [0,6,0,0,0,0,2,8,0],
                 [0,0,0,4,1,9,0,0,5],
                 [0,0,0,0,8,0,0,7,9]])

#Medium
med = np.asarray([[0,0,0,0,8,0,0,0,0],
                  [0,0,3,0,0,0,9,5,7],
                  [6,0,0,0,3,0,8,2,4],
                  [3,9,6,0,0,4,0,0,0],
                  [0,0,8,0,0,0,5,0,0],
                  [0,0,0,6,0,0,7,4,3],
                  [5,3,2,0,1,0,0,0,8],
                  [1,7,9,0,0,0,3,0,0],
                  [0,0,0,0,7,0,0,0,0]])

#Anti-Backtrack
AB = np.asarray([[0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,3,0,8,5],
                 [0,0,1,0,2,0,0,0,0],
                 [0,0,0,5,0,7,0,0,0],
                 [0,0,4,0,0,0,1,0,0],
                 [0,9,0,0,0,0,0,0,0],
                 [5,0,0,0,0,0,0,7,3],
                 [0,0,2,0,1,0,0,0,0],
                 [0,0,0,0,4,0,0,0,9]])

#HARDEST
hardest = np.asarray([[8,0,0,0,0,0,0,0,0],
                      [0,0,3,6,0,0,0,0,0],
                      [0,7,0,0,9,0,2,0,0],
                      [0,5,0,0,0,7,0,0,0],
                      [0,0,0,0,4,5,7,0,0],
                      [0,0,0,1,0,0,0,3,0],
                      [0,0,1,0,0,0,0,6,8],
                      [0,0,8,5,0,0,0,1,0],
                      [0,9,0,0,0,0,4,0,0]])

grid = ez

save = dc(grid)
show(save)

error = False

start = time.time()

while 0 in grid and error == False:

    while min_pos(grid) == 0:
        print("woops, restarting")
        nl(3)
        grid = dc(save)
        clear_output()
        break
    
    while min_pos(grid) == 1:
        for i in range(81):
            loc = whereami(i)
            if grid[loc[1]][loc[0]] == 0:
                
                if allowed_list(i) == []:
                    print(i,allowed_list(i),grid[loc[1]][loc[0]])
                    print("woops, restarting")
                    nl(3)
                    grid = dc(save)
                    clear_output()
                    break
                    
                elif len(allowed_list(i)) == 1:
                    grid[loc[1]][loc[0]] = rd.choice(allowed_list(i))
                    print(whereami(i)[0]+1, whereami(i)[1]+1,"input:",grid[loc[1]][loc[0]])#,allowed_list(i))
                    break
                    
    while min_pos(grid) == 2:
        for i in range(81):
            loc = whereami(i)
            if grid[loc[1]][loc[0]] == 0:
                
                if allowed_list(i) == []:
                    print(i,allowed_list(i),grid[loc[1]][loc[0]])
                    print("woops, restarting")
                    nl(3)
                    grid = dc(save)
                    clear_output()
                    break
                    
                elif len(allowed_list(i)) == 2:
                    grid[loc[1]][loc[0]] = rd.choice(allowed_list(i))
                    print(whereami(i)[0]+1, whereami(i)[1]+1,"supposition:",grid[loc[1]][loc[0]],allowed_list(i))
                    break
                
#    while min_pos(grid) == 3:
#        for i in range(81):
#            loc = whereami(i)
#            if grid[loc[1]][loc[0]] == 0:
#                
#                if allowed_list(i) == []:
#                    print(i,allowed_list(i),grid[loc[1]][loc[0]])
#                    print("woops, restarting")
#                    nl(3)
#                    grid = dc(save)
#                    break
#                    
#                elif len(allowed_list(i)) == 3:
#                    grid[loc[1]][loc[0]] = rd.choice(allowed_list(i))
#                    print(whereami(i)[0]+1, whereami(i)[1]+1,"supposition:",grid[loc[1]][loc[0]],allowed_list(i))    
#                    break

    if min_pos(grid) >= 3:
        if 0 in grid:
            print("Critical Error")
            error = True
        else:
            print("Solved!")

nl()
end = time.time()
elapsed = "Solution found in " + str(round(end-start,2)) + " seconds"

show(grid)
notify("sudoku.py", elapsed)

