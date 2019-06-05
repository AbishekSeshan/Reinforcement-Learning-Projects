import numpy as np

class state:
    def __init__(self,puddle,index):
        self.index = index
        self.puddle = puddle
        self.x = int(index/n)
        self.y = index % n 
        self.value = 0
        self.best_policy = ''


actions = ['no action', 'N', 'E', 'W', 'S']


def getNextState(current_state, action):
    
    if action == 'no action':
        nextstate = current_state.index
    
    elif current_state.puddle == 1:
        nextstate = current_state.index 
    
    elif action == 'N':
        if current_state.y == n-1:
            nextstate = current_state.index
        else:
            nextstate = current_state.index + 1
    
    elif action == 'E':
        if current_state.x == n-1:
            nextstate = current_state.index
        else:
            nextstate = current_state.index + n
    
    elif action == 'W':
        if current_state.x == 0:
            nextstate = current_state.index
        else:
            nextstate = current_state.index - n
    
    elif action == 'S':
        if current_state.y == 0:
            nextstate = current_state.index
        else:
            nextstate = current_state.index - 1

    return nextstate


def getReward(current_state, action, terminal_state_index):

    nextstate = getNextState(current_state, action)

    if current_state.index == terminal_state_index:
        if nextstate != current_state.index:
            reward = 0 
        else:
            reward = 100

    else:
        if nextstate == terminal_state_index:
            reward = 100
        elif lake[nextstate].puddle == 1:
            reward = -100 
        elif lake[nextstate].puddle == 0:
            reward = 0 
    
    return reward


def valueIteration(gamma, no_iterations, terminal_state_index):
    
    count = 0

    while(count < no_iterations):
        for i in range(n*n):
            
            reward_list = []
            
            for j in range(5):
                next_state_index = getNextState(lake[i], actions[j]) 
                reward = getReward(lake[i],actions[j],goal_state_index)
                value = lake[next_state_index].value 
                Q = float(reward) + (gamma*float(value))  #Bellman's packup
                reward_list.append(Q) 
            
            Qmax = max(reward_list) 
            lake[i].value = Qmax 
            lake[i].best_policy = actions[reward_list.index(Qmax)] 
        
        count +=1


def start():
    valueIteration(gamma, no_iterations, goal_state_index)
            
if __name__ == "__main__":

    n = int(input("No. of rows: "))

    lake=[]

    for i in range(n*n):
        lake.append(state(0,i)) 

    puddle = input(("Enter the indices of the cells(separated by space) where puddles exist: ")).split() #For eg: "2 4 6 12" means puddles are are indices 2,4,6,12

    for i in puddle:
        i = int(i) 
        lake[i].puddle = 1


    goal_state_index = int(input("Enter the index of the goal state: "))

    gamma = float(input("Enter the value of gamma: "))

    no_iterations = int(input("Enter the no. of iterations for convergence:"))

    start() 

    for i in lake:
        print("State: {} , Optimal action: {}".format(i.index,i.best_policy))
