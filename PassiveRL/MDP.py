from Utility import Average
from random import random, choice
from math import inf

class MDP:
    def __init__(self, S, P, R, E, START, use_avg):
        self.S = S
        self.P = P
        self.R = R
        self.E = E
        self.START = START
        self.U = {}
        self.use_avg = use_avg

        for s in S:
            if use_avg:
                self.U[s] = Average(0,0)
            else:
                self.U[s] = 0

    def u(self, state):
        if self.use_avg:
            val = self.U[state]
            if val.div == 0:
                return 0
                
            return val.num / val.div
        else:
            return self.U[state]

    def play_through(self, eps=0.1, max_steps=1000):
        print('=====================')
        states = [self.START]
        r = [0]

        s = self.START
        steps = 0

        while s not in self.E:
            print(s, len(self.P))
            best_s = None
            best_u = -inf

            valid_choices = [new_s for new_s in self.P[s]]

            if random() < eps:
                print(1)
                best_s = choice(valid_choices)
                best_u = self.u(best_s)
            else:
                print(2, best_u, [self.u(sss) for sss in valid_choices])
                for new_s in valid_choices:
                    next_u = self.u(new_s)
                    if next_u > best_u:
                        best_u = next_u
                        best_s = new_s

            states.append(best_s)
            r.append(self.R[s])
            s = best_s

            steps += 1
            if steps > max_steps:
                return None, [-1000]

        states.append(s)
        r.append(self.R[s])

        print('------------')

        return states, r