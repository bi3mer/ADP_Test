from tkinter.tix import MAX
from Problems import GridWorld, Keys
import ActiveRL
import PassiveRL


MAX_X = 25
MAX_Y = 5
start, G = GridWorld.build_grid_world(MAX_X, MAX_Y)

# GridWorld.display(G, start, 5,5)

# rl = PassiveRL.DirectUtilityEstimation(GridWorld.S, GridWorld.P, GridWorld.R, GridWorld.E, GridWorld.START)
rl = PassiveRL.PolicyIteration(G, 20, 0.5)
rl.update(None)
# rl = PassiveRL.ValueIteration(GridWorld.S, GridWorld.P, GridWorld.R, GridWorld.E, GridWorld.START, 1e-10)
# rl = PassiveRL.TemporalDifference(GridWorld.S, GridWorld.P, GridWorld.R, GridWorld.E, GridWorld.START)

# rl = ActiveRL.QLearning(GridWorld.S, GridWorld.P, GridWorld.R, GridWorld.E, GridWorld.START)
# rl = ActiveRL.SARSA(GridWorld.S, GridWorld.P, GridWorld.R, GridWorld.E, GridWorld.START)

# start = time()
# rl.train(600)
# end = time()

# print('\n')
# GridWorld.display_policy(rl)
# print('\n')
# GridWorld.display_utility(rl)


for __ in range(100):
    GridWorld.display(G, start, MAX_X, MAX_Y)
    print()
    if rl.get_md(start, Keys.E):
        break
    
    start = rl.get(start, 1)[0]

# success, states, r = rl.play_through(eps=0.0, max_steps=GridWorld.MAX_X*GridWorld.MAX_Y)
# if success:
#     input('show playthrough')
#     for s in states:
#         GridWorld.display(s)
#         print()

#     print(f'r={sum(r)}')
# else:
#     print('Policy was not able to solve gridworld.')
    
# print(f'Time elapsed: {end - start}')
