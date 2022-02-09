from random import random, choice
from math import inf

class QTable:
    def __init__(self, S, P, R, E, START, use_avg):
        self.S = S
        self.R = R
        self.E = E
        self.START = START
        self.s = START
        self.Q = {}
        self.use_avg = use_avg

        for s in S:
            self.Q[s] = {}
            for s_p in P[s]:
                self.Q[s][s_p] = 0

    def max_next(self, s):
        valid_choices = [new_s for new_s in self.Q[s]]
        best_s = None
        best_u = -inf

        for new_s in valid_choices:
            next_u = self.Q[s][new_s]
            if next_u > best_u:
                best_u = next_u
                best_s = new_s

        return best_s, best_u

    def u(self, s):
        return self.max_next(s)[1]
        
    def get_next(self, s, eps=0.05):
        if random() < eps:
            best_s = choice([new_s for new_s in self.Q[s]])
            best_q = self.Q[s][best_s]
        else:
            best_s, best_q = self.max_next(s)

        return best_s, best_q

    def play_through(self, eps=0.1, max_steps=1000):
        states = [self.START]
        r = [0]

        s = self.START
        steps = 0

        while s not in self.E:
            best_s, _ = self.get_next(s, eps=eps)

            states.append(best_s)
            r.append(self.R[s])
            s = best_s

            steps += 1
            if steps > max_steps:
                return False, states, r

        states.append(s)
        r.append(self.R[s])

        return True, states, r

    def reset(self):
        self.s = self.START

    def next(self, new_state):
        self.s = new_state
        return self.R[new_state]

    
