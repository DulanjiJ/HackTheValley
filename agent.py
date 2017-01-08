<<<<<<< HEAD
import random
import math
import gym
import universe

#GLOBAL VARIABLES
testing = False #If True, learning is disabled and Q-table is used
Q = dict()          # Create a Q-table which will be a dictionary of tuples
valid_actions = [[('KeyEvent', 'ArrowUp', True)],[('KeyEvent', 'ArrowDown',False)],[('KeyEvent', 'ArrowLeft', False)],[('KeyEvent', 'ArrowRight', False)]]

env = gym.make('flashgames.FormulaRacer-v0')
env.configure(remotes=1)  # automatically creates a local docker container
observation_n = env.reset()

real_action = valid_actions[0]
reward_n = [0]
prev_reward = [-1]

def AIdecision(reward_new,reward_old,action_old):
    global valid_actions
    if reward_new[0] >= reward_old[0]:
        next_action = action_old
    else:
        next_number = random.randint(0,3)
        next_action = [(valid_actions[next_number][0][0],valid_actions[next_number][0][1],True)]

        #Set all inputs to False
        valid_action = [[('KeyEvent', 'ArrowUp', False)],[('KeyEvent', 'ArrowDown',False)],[('KeyEvent', 'ArrowLeft', False)],[('KeyEvent', 'ArrowRight', False)]]
        #Set selected input to true
        valid_action[next_number] = next_action
        valid_actions = valid_action

    return next_action

while True:
    real_action = AIdecision(reward_n,prev_reward,real_action)
    action_n = [real_action for ob in observation_n]  # your agent here
    prev_reward = reward_n
    (observation_n, reward_n, done_n, info) = env.step(action_n)
    env.render()
=======
import random
import math
import gym
import universe

#GLOBAL VARIABLES
testing = False #If True, learning is disabled and Q-table is used
Q = dict()          # Create a Q-table which will be a dictionary of tuples
valid_actions = [[('KeyEvent', 'ArrowUp', True)],[('KeyEvent', 'ArrowDown', True)],[('KeyEvent', 'ArrowLeft', True)],[('KeyEvent', 'ArrowRight', True)]]

env = gym.make('flashgames.FormulaRacers-v0')
env.configure(remotes=1)  # automatically creates a local docker container
observation_n = env.reset()

real_action = valid_actions[0]
reward_n = 0
prev_reward = -1

def AIdecision(reward_new,reward_old,action_old):
    if reward_new >= reward_old:
        next_action = action_old
    else:
        next_action = random.randint(0,3)
    return next_action

while True:
    real_action = AIdecision(reward_n,prev_reward,real_action)
    action_n = [real_action for ob in observation_n]  # your agent here
    prev_reward = reward_n
    observation_n, reward_n, done_n, info = env.step(action_n)
    env.render()
>>>>>>> d5221101005c73faf7a951c6d7f4edaf9c2f7661
