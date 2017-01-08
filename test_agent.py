import gym
import universe

env = gym.make('flashgames.FormulaRacer-v0')
env.configure(remotes=1)
obv_n = env.reset()
handle = open('obv.txt','w')

for i in range(3000):
  act_n = [[('KeyEvent', 'ArrowUp', True)] for ob in obv_n]
  obv_n, reward_n, done_n, info = env.step(act_n)
  env.render()
  print(obv_n)
  print(info)
