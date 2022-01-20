from math import inf
from random import random, choice

def play_through(agent, game, eps=0.1):
    game.new()
    states = [game.state]

    while game.reward() == 0:
        best_s = None
        best_u = -inf

        if random() < eps:
            best_s = choice(game.next_states())
            best_u = agent.u(best_s)
        else:
            for s in game.next_states():
                next_u = agent.u(s)
                if next_u > best_u:
                    best_u = next_u
                    best_s = s

        states.append(best_s)
        game.state = best_s

    return states, game.reward()
