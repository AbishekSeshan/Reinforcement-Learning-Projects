import random 

class state:
    def __init__(self,wall,index):
        self.left = wall[0] 
        self.right = wall[1]
        self.up = wall[2] 
        self.down = wall[3] 
        self.index = index
        self.x = index / n 
        self.y = index % n

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
        if current_state.index != (n*n)-1:  #if it is not terminal state
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

start_state = maze[0] 
terminal_state = maze[(n*n)-1]


'''for i in maze:
    direction = input("Enter the action for the agent in state {}: ".format(i.index))
    print("The destination state for the current state with index {} is: {}".format(i.index,getNextState(i,direction)))
    print("The reward for this transition is: {}".format(getReward(i,direction)))
    print("")'''

print("Learning in progress.....")
print("")

#Learning process

no_iterations = 100

actions = ['N','E','W','S','no action'] 

#                               S0                ,               S1            ................  
training_set = [] #[[[A, S', R]........(100 times)],[[A, S', R].......(100 times)],................]

for i in range(n*n):
    
    temp1 = []
    
    for j in range(no_iterations):
        temp2 = []
        random_action = random.choice(actions)
        temp2.append(random_action) #temp2[0] = action

        next_state = getNextState(maze[i],random_action)
        temp2.append(next_state) #temp2[1] = index of next state 

        reward = getReward(maze[i],random_action)
        temp2.append(reward) #temp2[2] = reward for this transition 

        temp1.append(temp2)

    training_set.append(temp1)  


for i in range(len(training_set)):
    print("Set for state {}".format(i))
    print(training_set[i])
    print("")


        
    