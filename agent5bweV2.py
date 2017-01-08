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
g_time = 0
r_timer = 0

#openai API to open flash game and congigure enviroment
env = gym.make('flashgames.FormulaRacer-v0')
env.configure(remotes=1)
observation_n = env.reset()#observation variable
action_n = [forward for ob in observation_n] #default action press up

#While loop to decide to go left or right
while True:
  g_time += 1
  if observation_n[0] != None:
    if reward_n[0] >= 0 or reward_n[0] < -0.03:
      action_n = [forward for ob in observation_n]
    else:
      timer += 1
      print(timer)
      if timer < 50:
        action_n = [left for ob in observation_n]
        r_timer += 1
      elif timer >= 85:
        if r_timer > 20:
          for u in range(r_timer):
            r_timer -= 1
            action_n = [right for ob in observation_n]
            observation_n, reward_n, done_n, info = env.step(action_n)
            env.render()
          timer = 0
    print(g_time)
    print(reward_n)

  observation_n, reward_n, done_n, info = env.step(action_n)
  env.render()
