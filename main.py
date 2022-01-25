from email.policy import Policy
from tkinter import Grid
import GridWorld
from RL import *

rl = DirectUtilityEstimation(GridWorld.S, GridWorld.A, GridWorld.P, GridWorld.R, GridWorld.E, GridWorld.START)
rl.train(100_000)

GridWorld.display_utility(rl)

input()

states, r = rl.play_through(eps=0.0)
for s in states:
    GridWorld.display(s)
    print()

print(f'r={r}, reward={GridWorld.R[s]}')
