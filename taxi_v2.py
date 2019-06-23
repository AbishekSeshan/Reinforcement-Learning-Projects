# Solving deterministic Taxi-v2 problem using Value and Policy iterations.
# 5x5 grid: R - 20 ; G - 7 ; B - 9 ; Y - 24 (index numbers of pickup/drop locations)
# Actions: 0 - North, 1 - East, 2 - West, 3 - South, 4 - Pickup, 5 - Drop 
# Passenger states - 5 (0-R, 1-G, 2-B, 3-Y, 4-T(in taxi))
# Destination states - 4 (0-R, 1-G, 2-B, 3-Y)  
# State format: State[grid index, passenger state, destination state]

import numpy as np 

n = 5

colors = [20,7,9,24] #indices with colors, i.e possible pick-up and drop locations. 

class cell:
    def __init__(self,wall,index):
        self.left = wall[0] 
        self.right = wall[1]
        self.up = wall[2] 
        self.down = wall[3] 
        self.index = index
        self.x = int(index / n) 
        self.y = index % n
        self.color = 4    #color : 0R,1G,2B,3Y locations. 

grid = []
value = np.zeros((n*n,5,4))
policy = np.zeros((n*n,5,4))
reward_mat = np.zeros((n*n,5,4,6)) 


def getNextState(current_state, action): #index,passloc,desloc

    x = int(current_state[0] / n)
    y = current_state[0] % n
    
    next_state = current_state

    if action == 0:
        if y == n-1:
            next_state = next_state 
        else:
            if grid[current_state[0]].up == '0':
                next_state[0] += 1 
            else:
                next_state = next_state
            
    elif action == 1:
        if x == n-1:
            next_state = next_state
        else:
            if grid[current_state[0]].right == '0':
                next_state[0] += n 
            else:
                next_state = next_state
    
    elif action == 2:
        if x == 0:
            next_state = next_state
        else:
            if grid[current_state[0]].left == '0':
                next_state[0] -= n 
            else:
                next_state = next_state

    elif action == 3:
        if y == 0:
            next_state = next_state
        else:
            if grid[current_state[0]].down == '0':
                next_state[0] -= 1 
            else:
                next_state = next_state

    elif action == 4: #pickup 
        
        if grid[current_state[0]].color == grid[pass_loc].color and current_state[1] != 4:   #if current location is pickup location and passenger not in taxi
            next_state[1] = 4                                                                #passenger in taxi.
        
        else:
            next_state = next_state

    elif action == 5: #drop
        
        if grid[current_state[0]].color == grid[pass_loc].color and current_state[1] == 4:   #if current location is drop location and passenger is in taxi
            next_state[1] = grid[current_state[0]].color                                     #passenger dropped off.

        else:
            next_state = next_state

    return next_state

def getReward(current_state, action):
    
    '''+20 reward for legal drop off and pickup, and -10 for illegal drop off and pick up.
        -1 reward otherwise'''
    
    if action == 4: #pickup
        if grid[current_state[0]].color == grid[pass_loc].color and current_state[1] != 4:
            reward = 20
        else:
            reward = -10
    
    elif action == 5: #drop off
        if grid[current_state[0]].color == grid[pass_loc].color and current_state[1] == 4:
            reward = 20
        else:
            reward = -10

    else:
        reward = -1
    
    return reward


def fillreward():
    for index in range(n*n):
        for ploc in range(5):
            for dest in range(4):
                statez = [index,ploc,dest]
                for a in range(6):
                    r = getReward(statez,a) 
                    reward_mat[index,ploc,dest,a] = r


def valueIteration():

    gamma = 0.7
    count = 0

    while(count<100):
        for index in range(n*n):
            for ploc in range(5):
                for dest in range(4):
                    statez = [index,ploc,dest]
                    reward_list = []
                    for a in range(6):
                        next_state = getNextState(statez,a) 
                        ah = next_state[0]
                        b = next_state[1]
                        c = next_state[2]
                        q = reward_mat[index,ploc,dest] + float(gamma*value[ah,b,c]) 
                        reward_list.append(q) 

                    Qmax = max(reward_list)
                    best = reward_list.index(Qmax) 
                    
                    value[index,ploc,dest] = Qmax
                    policy[index,ploc,dest] = best
        count += 1

    

def sequence():
    pass
    
def start():

    pass


    
    


if __name__ == "__main__":

    #n = int(input("Rows: "))
    #n=5

    for i in range(n*n):
        a = '0000'
        grid.append(cell(a,i)) 

    #taxi_loc = int(input("Enter taxi location: "))
    taxi_loc = 5

    #pass_loc = int(input("Enter passenger location: "))
    pass_loc = 9 #(B)

    #destination = int(input("Enter destination index: "))
    destination = 20 #(R)


    #color initializations:
    grid[20].color = 0 #R
    grid[7].color = 1  #G
    grid[9].color = 2  #B
    grid[24].color = 3 #Y

    #wall initializations:
    grid[0].right=1
    grid[5].left=1

    grid[1].right=1
    grid[6].left=1

    grid[8].right=1
    grid[13].left=1

    grid[9].right=1
    grid[14].left=1

    grid[10].right=1
    grid[15].left=1

    grid[11].right=1
    grid[16].left=1

    valueIteration()

    print(policy)