from GridWorld import GridWorld
from RL import DirectUtilityEstimation
from math import inf

g = GridWorld()
rl = DirectUtilityEstimation(g)
rl.train(100_000)

g.display_utility(rl)

input()

g.new()
g.display()
while g.reward() == 0:
    print('\n\n')
    best_s = None
    best_u = -inf
    for s in g.next_states():
        next_u = rl.u(s)
        if next_u > best_u:
            best_u = next_u
            best_s = s

    g.state = best_s
    g.display()
    print(best_s, best_u)
