#Deterministic Maze 

import random 

class state:
    def __init__(self,wall,index):
        self.left = wall[0] 
        self.right = wall[1]
        self.up = wall[2] 
        self.down = wall[3] 
        self.index = index
        self.x = int(index / n) 
        self.y = index % n
        self.value = 0 #Value function for that state
        self.best_action = '' #Stores the best action for the particular state

    def wallinfo(self):
        return "Wall info at index {}: left {}, right {}, up {}, down {}".format(self.index, self.left, self.right, self.up, self.down)

n = int(input("Rows: ")) 

def getNextState(current_state, action): #Returns the index of the next state
    
    if action == 'N':
        if current_state.y == n-1:
            return current_state.index
        else:
            if current_state.up == '0':
                return current_state.index + 1 
            else:
                return current_state.index
            
    elif action == 'E':
        if current_state.x == n-1:
            return current_state.index
        else:
            if current_state.right == '0':
                return current_state.index + n 
            else:
                return current_state.index
    
    elif action == 'W':
        if current_state.x == 0:
            return current_state.index
        else:
            if current_state.left == '0':
                return current_state.index - n 
            else:
                return current_state.index

    elif action == 'S':
        if current_state.y == 0:
            return current_state.index
        else:
            if current_state.down == '0':
                return current_state.index - 1 
            else:
                return current_state.index

    elif action == 'No action' or action == 'no action':
            return current_state.index
    
    else:
        print("Please enter a valid action ") 
        


def getReward(current_state, action): #Returns the reward for a transition
    
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

#main starts here

maze = []

for i in range(n*n):
    x = input("walls at left, right, up, down for index {}: ".format(i)) #1 for wall, 0 for no wall. For eg: x=1001 means walls at left and down.
    maze.append(state(x,i))
    #print(maze[i].wallinfo())

print("")

w = int(input("Enter the terminal/destination state:"))
print("")

terminal_state = maze[w]


print("Learning in progress.....")
print("")

#Learning process (deterministic)

no_iterations = 100

actions = ['no action','N','E','W','S'] 


'''def valueFromIndex(index_of_state): #returns the value function of the state who's index has been passed as an argument
    for i in maze:
        if index_of_state == i.index:
            return i.value''' 

def valueIteration():
    
    #sigma = 0.003 
    gamma = 0.5 
    count = 0
    while(count<=10000):
        for i in maze:
            reward_list = []
            for j in actions:
                r = getReward(i,j)
                state_next_index = getNextState(i,j)
                v = maze[state_next_index].value
                '''v = valueFromIndex(state_next_index) 
                print(v)'''
                Q = float(r) + (gamma*float(v))
                reward_list.append(Q)  
            Qmax = max(reward_list)
            max_index = reward_list.index(Qmax)

            i.value = Qmax
            i.best_action = actions[max_index]
        
        count+=1 



valueIteration()

for i in maze:
    print("State: {} , Optimal action: {}".format(i.index,i.best_action))
     
    