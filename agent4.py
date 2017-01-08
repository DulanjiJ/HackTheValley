import random
import math
import gym
import universe

#DIRECTIONS
left = [('KeyEvent', 'ArrowUp', True) ,('KeyEvent', 'ArrowLeft', True), ('KeyEvent', 'ArrowRight', False)]
right = [('KeyEvent', 'ArrowUp', True) ,('KeyEvent', 'ArrowLeft', False), ('KeyEvent', 'ArrowRight', True)]
forward = [('KeyEvent', 'ArrowUp', True) ,('KeyEvent', 'ArrowLeft', False), ('KeyEvent', 'ArrowRight', False)]

#GLOBALS
ticks = 0
total = 0
timer = 0
prev_reward = 0
last_reward = 0

env = gym.make('flashgames.FormulaRacer-v0')
env.configure(remotes=1)
observation_n = env.reset()
action_n = [forward for ob in observation_n]


while True:
  if observation_n[0] != None:
    current_diff = reward_n[0] - prev_reward
    last_diff = prev_reward - last_reward
    if current_diff >= last_diff:
      action_n = [forward for ob in observation_n]
      timer = 0
    else:
      timer += 1
      print(timer)
      if timer < 50:
        action_n = [left for ob in observation_n]
      else:
        action_n = [right for ob in observation_n]
    last_reward = prev_reward
    prev_reward = reward_n[0]
  observation_n, reward_n, done_n, info = env.step(action_n)
  print(reward_n)
  env.render()
