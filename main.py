import GridWorld
import ActiveRL
import PassiveRL
from time import time

# rl = PassiveRL.DirectUtilityEstimation(GridWorld.S, GridWorld.P, GridWorld.R, GridWorld.E, GridWorld.START)
# rl = PassiveRL.PolicyIteration(GridWorld.S, GridWorld.P, GridWorld.R, GridWorld.E, GridWorld.START, 1e-13)
# rl = PassiveRL.ValueIteration(GridWorld.S, GridWorld.P, GridWorld.R, GridWorld.E, GridWorld.START, 1e-10)
# rl = PassiveRL.TemporalDifference(GridWorld.S, GridWorld.P, GridWorld.R, GridWorld.E, GridWorld.START)

# rl = ActiveRL.QLearning(GridWorld.S, GridWorld.P, GridWorld.R, GridWorld.E, GridWorld.START)
rl = ActiveRL.SARSA(GridWorld.S, GridWorld.P, GridWorld.R, GridWorld.E, GridWorld.START)

start = time()
rl.train(50)
end = time()

print('\n')
GridWorld.display_policy(rl)
print('\n')
GridWorld.display_utility(rl)
input()

success, states, r = rl.play_through(eps=0.0, max_steps=GridWorld.MAX_X*GridWorld.MAX_Y)
if success:
    for s in states:
        GridWorld.display(s)
        print()

    print(f'r={sum(r)}')
else:
    print('Policy was not able to solve gridworld.')
    
print(f'Time elapsed: {end - start}')
