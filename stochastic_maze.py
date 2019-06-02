#Stochastic Maze with uncertain policies for each state. Each action that the agent takes
#will have 80% probability of going in that direction and 0% of going on the opposite direction. 
#For eg: 'N' action will have 80% probability of the agent going north, 10% probability each of going east 
#and west and 0% probability of going south.

import random
import numpy as np 

class state:
    def __init__(self,wall,index):
        self.left = wall[0] 
        self.right = wall[1]
        self.up = wall[2] 
        self.down = wall[3] 
        self.index = index
        self.x = int(index / n) 
        self.y = index % n
        #self.count = [0,0,0,0,0] #[noaction, N, E, W, S]
        self.value = 0 #Value function for that state
        self.best_action = '' #Stores the optimal policy

    def wallinfo(self):
        return "Wall info at index {}: left {}, right {}, up {}, down {}".format(self.index, self.left, self.right, self.up, self.down)

n = int(input("Rows: ")) 

def computeAction(current_state, action, random_no): #Random number is between 0 and 1
    if action == 'N':
        if random_no >0.2:
            computed_action = action 
        
        elif random_no >0.1:
            computed_action = 'E' 
        
        else:
            computed_action = 'W'
    
    elif action == 'E':
        if random_no >0.2:
            computed_action = action 
        
        elif random_no >0.1:
            computed_action = 'N' 
        
        else:
            computed_action = 'S'   
    
    elif action == 'W':
        if random_no >0.2:
            computed_action = action 
        
        elif random_no >0.1:
            computed_action = 'N' 
        
        else:
            computed_action = 'S'
    
    elif action == 'S':
        if random_no >0.2:
            computed_action = action 
        
        elif random_no >0.1:
            computed_action = 'E' 
        
        else:
            computed_action = 'W'

    elif action == "no action":
        computed_action = action 

    return computed_action


def getNextState(current_state, computed_action): #Returns the index of the next state
    
    if computed_action == 'N':
        if current_state.y == n-1:
            return current_state.index
        else:
            if current_state.up == '0':
                return current_state.index + 1 
            else:
                return current_state.index
            
    elif computed_action == 'E':
        if current_state.x == n-1:
            return current_state.index
        else:
            if current_state.right == '0':
                return current_state.index + n 
            else:
                return current_state.index
    
    elif computed_action == 'W':
        if current_state.x == 0:
            return current_state.index
        else:
            if current_state.left == '0':
                return current_state.index - n 
            else:
                return current_state.index

    elif computed_action == 'S':
        if current_state.y == 0:
            return current_state.index
        else:
            if current_state.down == '0':
                return current_state.index - 1 
            else:
                return current_state.index

    elif computed_action == 'No action' or computed_action == 'no action':
            return current_state.index
    
    else:
        print("Please enter a valid action ") 
        


def getReward(current_state, action, w): #Returns the reward for a transition #w is terminal state index
    
    next_state_index = getNextState(current_state, action)
    
    if current_state.index == next_state_index:
        if current_state.index != w:  #if it is not terminal state
            reward = -100 
            return reward
        else:
            reward = 100
            return reward

    else:
        if next_state_index == terminal_state.index:
            reward = 100
            return reward
        else:
            reward = 1
            return reward

action_count = np.zeros((n*n, 5))
transition_matrix = np.zeros((n*n,5,n*n))

def transition_model(gamma, w):
    
    no_iterations = 1000
    count = 0

    while(count<=no_iterations):
        for i in maze:
            for a in actions:
                x = actions.index(a)
                action_count[i.index,x] += 1                            #C(s,a) += 1
                number = random.random() 
                action = computeAction(i,a,number)
                next_state_index = getNextState(i,action)   
                transition_matrix[i.index,x,next_state_index] += 1      #C(s,a,s') += 1
        
        count+=1

    for s in range(0,n*n):
        for a in range(5):
            for s_ in range(0,n*n):
                transition_matrix[s,a,s_] = transition_matrix[s,a,s_]/action_count[s,a] 
    
    return transition_matrix 

def valueIteration(gamma, w):

    probability = transition_model(gamma,w)
    #sigma = 0.005 
    count = 0
    while(count<=10000):
        for i in maze:
            reward_list = []

            for a in actions:
                temp = 0
                x = actions.index(a)
                r = getReward(i,a,w)

                for j in maze:
                    state_next_index = j.index
                    v = j.value
                    temp +=  probability[i.index,x,state_next_index]*(gamma*float(v))
                
                Q = r + temp
                reward_list.append(Q)  
            Qmax = max(reward_list)
            max_index = reward_list.index(Qmax)

            i.value = Qmax
            i.best_action = actions[max_index]
        
        count+=1 

def start():
    valueIteration(gamma,w) 



if __name__=="__main__":

    actions = ['no action', 'N', 'E', 'W', 'S' ]

    maze = []

    for i in range(n*n):
        x = input("walls at left, right, up, down for index {}: ".format(i)) #1 for wall, 0 for no wall. For eg: x=1001 means walls at left and down.
        maze.append(state(x,i))
        

    print("")

    w = int(input("Enter the terminal/destination state:"))
    print("")

    terminal_state = maze[w]

    print("Learning in progress.....")
    print("")

    gamma = float(input("Enter the value of the discount factor: "))
    print("")

    start() 

    for i in maze:
        print("State: {} , Optimal action: {}".format(i.index,i.best_action))

