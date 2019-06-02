import numpy as np

class state:
    def __init__(self,puddle,index):
        self.index = index
        self.puddle = puddle
        self.x = int(index/n)
        self.y = index % n 


n = int(input("No. of rows: "))

lake=[]

for i in range(n*n):
    lake.append(state(0,i)) 

puddle = input(("Enter the indices of the cells(separated by space) where puddles exist: ")).split() #For eg: "2 4 6 12" means puddles are are indices 2,4,6,12

for i in puddle:
    i = int(i) 
    lake[i].puddle = 1


goal_state_index = int(input("Enter the index of the goal state: ")) 


