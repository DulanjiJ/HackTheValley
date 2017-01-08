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
