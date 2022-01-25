from Utility import Average
from random import random, choice
from math import inf

class MDP:
    def __init__(self, S, A, P, R, E, START):
        self.A = A
        self.P = P
        self.R = R
        self.E = E
        self.START = START
        self.utility = {}
        for s in S:
            self.utility[s] = Average(0,0)

    def u(self, state):
        val = self.utility[state]
        if val.div == 0:
            return 0
            
        return val.num / val.div

    def play_through(self, eps=0.1):
        states = [self.START]
        s = self.START
        r = 0

        while s not in self.E:
            best_s = None
            best_u = -inf

            valid_choices = [new_s for new_s in self.P[s] if self.P[s][new_s] > 0]

            if random() < eps:
                best_s = choice(valid_choices)
                best_u = self.u(best_s)
            else:
                for new_s in valid_choices:
                    next_u = self.u(new_s)
                    if next_u > best_u:
                        best_u = next_u
                        best_s = new_s

            states.append(best_s)
            s = best_s
            r += self.R[s]

        return states, r