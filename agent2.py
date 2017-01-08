import random
import math
import gym
import universe

#GLOBAL VARIABLES
testing = False #If True, learning is disabled and Q-table is used
Q = dict()          # Create a Q-table which will be a dictionary of tuples
valid_actions = [[('KeyEvent', 'ArrowUp', True)],[('KeyEvent', 'ArrowDown',False)],[('KeyEvent', 'ArrowLeft', False)],[('KeyEvent', 'ArrowRight', False)]]
left = False

env = gym.make('flashgames.FormulaRacer-v0')
env.configure(remotes=1)  # automatically creates a local docker container
observation_n = env.reset()

real_action = valid_actions[0]
reward_n = [0]
prev_reward = [-1]

def AIdecision(reward_new,reward_old,action_old):
    global valid_actions
    global left
    
    next_action = action_old
    
    if reward_new[0] < reward_old[0]:
        
        #Set all inputs to False
        valid_action = [[('KeyEvent', 'ArrowUp', False)],[('KeyEvent', 'ArrowDown',True)],[('KeyEvent', 'ArrowLeft', False)],[('KeyEvent', 'ArrowRight', False)]]
        
        if left:
            next_action = [(valid_actions[3][0][0],valid_actions[3][0][1],True)]
            valid_action[3] = next_action
            left = False
        else:
            next_action = [(valid_actions[2][0][0],valid_actions[2][0][1],True)]
            valid_action[2] = next_action
            left = True
       
        valid_actions = valid_action
        
    else:
        valid_action = [[('KeyEvent', 'ArrowUp', True)],[('KeyEvent', 'ArrowDown',False)],[('KeyEvent', 'ArrowLeft', False)],[('KeyEvent', 'ArrowRight', False)]]
        valid_actions = valid_action
        next_action = [('KeyEvent', 'ArrowUp', True)]
        
    return next_action

while True:
    real_action = AIdecision(reward_n,prev_reward,real_action)
    action_n = [real_action for ob in observation_n]  # your agent here
    prev_reward = reward_n
    (observation_n, reward_n, done_n, info) = env.step(action_n)
    env.render()