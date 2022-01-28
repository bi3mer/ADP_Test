import GridWorld
from RL import *
from time import time

# rl = DirectUtilityEstimation(GridWorld.S, GridWorld.P, GridWorld.R, GridWorld.E, GridWorld.START)
rl = PolicyIteration(GridWorld.S, GridWorld.P, GridWorld.R, GridWorld.E, GridWorld.START, 1e-13)
# rl = ValueIteration(GridWorld.S, GridWorld.P, GridWorld.R, GridWorld.E, GridWorld.START, 1e-13)
start = time()
rl.train(100_000)
end = time()

# print('\n')
# GridWorld.display_policy(rl)
# print('\n')
# GridWorld.display_utility(rl)
# input()

states, r = rl.play_through(eps=0.0, max_steps=GridWorld.MAX_X*GridWorld.MAX_Y)
# for s in states:
#     GridWorld.display(s)
#     print()

# print(f'r={r}, reward={GridWorld.R[s]}')
print(f'r={r}')
print(f'Time elapsed: {end - start}')
