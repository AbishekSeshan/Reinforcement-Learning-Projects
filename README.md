# Reinforcement Learning Projects
This repository contains many classical applications of Reinforcement Learning (model based and model free) which have been implemented during my learning phase:
<br>
<h2>1. Deterministic Maze Problem </h2> 

This is a nxn grid where each cell can have boundaries on all of it sides. The agent will find an optimal way to a terminal/goal state provided by the user. This is an application of deterministic model based RL. 

<h2>2. Stochastic Maze Problem (WIP) </h2> 

This is a nxn grid where each cell can have boundaries on all of it sides. Stochasticity comes into play in the form of stochastic policies for each state such that, for an action in a particular state, the agent has 80% probability of taking that particular action, 0% probability of taking the opposite action, and 10% probability for each of the remaining directional actions.  
For eg: if the chosen action is 'N':
P(N) = 0.8, P(S) = P(no action) = 0, P(E) = P(W) = 0.1
	 
The agent will find an optimal way to a terminal/goal state provided by the user. 

<h2>3. Frozen Lake Problem (WIP) </h2>
This is quite similar to the maze problem with the difference that here, some cells have to be skipped since they have holes. An agent will have to find its way through the Frozen Lake. This is also an application of deterministic model based RL. 
