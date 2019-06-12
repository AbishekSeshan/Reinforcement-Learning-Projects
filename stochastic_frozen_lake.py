import numpy as np
import random as rd

class state:
    def __init__(self,puddle,index):
        self.index = index
        self.puddle = puddle
        self.x = int(index/n)
        self.y = index % n 
        self.best_policy = ''

n = int(input("Enter the number of rows: "))

actions = ['no action', 'N', 'E', 'W', 'S']

probability = np.zeros((n*n,5,n*n)) #Transition matrix (C(s,a,s')/C(s,a))
action_count = np.zeros((n*n,5))    #State Action matrix (C(s,a))
reward_matrix = np.zeros((n*n,5))   #Reward matrix (R(s,a))
value = np.ones((n*n))              #Value function array (V(s))

def getNextState(current_state, action, chance):

    if action == "no action" or current_state.puddle == 1:
        next_state_index = current_state.index 
    
    elif action == 'N':
        if chance > 0.4:
            if current_state.y == n-1:
                next_state_index = current_state.index
            else:
                next_state_index = current_state.index + 1
        
        else:
            if current_state.y == n-1:
                next_state_index = getNextState(current_state, action, 0.5)
            else:
                next_state = lake[current_state.index + 1] 
                next_state_index = getNextState(next_state, action, 0.5) 
    
    elif action == 'E':
        if chance > 0.4:
            if current_state.x == n-1:
                next_state_index = current_state.index
            else:
                next_state_index = current_state.index + n
        
        else:
            if current_state.x == n-1:
                next_state_index = getNextState(current_state, action, 0.5)
            else:
                next_state = lake[current_state.index + n] 
                next_state_index = getNextState(next_state, action, 0.5) 
    
    elif action == 'W':
        if chance > 0.4:
            if current_state.x == 0:
                next_state_index = current_state.index
            else:
                next_state_index = current_state.index - n
        
        else:
            if current_state.x == 0:
                next_state_index = getNextState(current_state, action, 0.5)
            else:
                next_state = lake[current_state.index - n] 
                next_state_index = getNextState(next_state, action, 0.5) 
    
    elif action == 'S':
        if chance > 0.4:
            if current_state.y == 0:
                next_state_index = current_state.index
            else:
                next_state_index = current_state.index - 1
        
        else:
            if current_state.y == 0:
                next_state_index = getNextState(current_state, action, 0.5)
            else:
                next_state = lake[current_state.index - 1] 
                next_state_index = getNextState(next_state, action, 0.5) 
    
    return next_state_index
    
def getReward(current_state, action, chance, goal_state_index):
    
    nextstate = getNextState(current_state, action, chance)

    if lake[nextstate].puddle == 1:
        reward = -100
    
    elif nextstate == goal_state_index:
        reward = 100 
    
    elif nextstate == current_state.index:
        reward = -10

    else:
        reward = 0 
    
    return reward

def rewardMatrix(goal_state_index):
    for i in range(n*n):
        for a in range(5): 
            r = 0.4*getReward(lake[i],actions[a],0.3,goal_state_index) + 0.6*getReward(lake[i],actions[a],0.5,goal_state_index)
            reward_matrix[i,a] = r 
    
    

def transitionModel(goal_state_index):

    no_iterations = 1000 

    for _ in range (no_iterations):
        
        for s in lake:
            for a in actions:
                action_count[s.index, actions.index(a)] +=1
        
                chance = rd.random()

                s_ = getNextState(s,a,chance)
                probability[s.index, actions.index(a), s_] +=1

    for s in range(0,n*n):
        for a in range(5):
            for s_ in range(0,n*n):
                probability[s,a,s_] = probability[s,a,s_]/action_count[s,a]

    return probability 

def policyIteration(gamma, goal_state_index):

    T = transitionModel(goal_state_index) 
    
    count = 0

    while(count<500):

        for s in range(n*n):
            reward_list = []

            for a in range(5):
                temp = 0
                

                for s_ in range(n*n):
                    temp = T[s,a,s_]*value[s_]

                Q = reward_matrix[s,a] + (gamma*temp) #Bellman's backup
                reward_list.append(Q) 

            Qmax = max(reward_list) 
            value[s] = Qmax

            lake[s].best_policy = actions[reward_list.index(Qmax)] #actions[index of Qmax] 
            
            count +=1


def start():
    
    print("")
    print("Learning in progress...")
    print("")
    rewardMatrix(w)
    policyIteration(gamma,w) 

    for i in lake:
        print("State: {} , Optimal action: {}".format(i.index,i.best_policy))

                

    
if __name__ == "__main__":
    
    lake=[]

    for i in range(n*n):
        lake.append(state(0,i)) 

    puddle = input(("Enter the indices of the cells(separated by space) where puddles exist: ")).split() #For eg: "2 4 6 12" means puddles are at indices 2,4,6,12

    for i in puddle:
        i = int(i) 
        lake[i].puddle = 1


    w = int(input("Enter the index of the goal state: "))

    gamma = float(input("Enter the value of gamma: "))

    start()
     
