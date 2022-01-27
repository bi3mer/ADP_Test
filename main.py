from email.policy import Policy
import GridWorld
from RL import *

# rl = DirectUtilityEstimation(GridWorld.S, GridWorld.P, GridWorld.R, GridWorld.E, GridWorld.START)
rl = PolicyIteration(GridWorld.S, GridWorld.P, GridWorld.R, GridWorld.E, GridWorld.START, 1e-6)
# rl = ValueIteration(GridWorld.S, GridWorld.P, GridWorld.R, GridWorld.E, GridWorld.START, 0.03)
rl.train(100_000)

print('\n')
GridWorld.display_utility(rl)
input()

states, r = rl.play_through(eps=0.0)
for s in states:
    GridWorld.display(s)
    print()

print(f'r={r}, reward={GridWorld.R[s]}')
