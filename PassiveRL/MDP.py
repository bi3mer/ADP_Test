from math import inf
from random import choices, random, choice
from math import exp

from .Base import Base
from Problems.Keys import *

class MDP(Base):
    def __init__(self, graph, name):
        super().__init__(graph, name)
        self._reset_utility()

    def _reset_utility(self):
        for n in self.G.nodes:
            self.G.nodes[n][U] = 0

    def _best_neighbor(self, node):
        best_n = None
        best_u = -inf

        for neighbor in self.G.neighbors(node):
            new_u = self.get_md(neighbor, U)

            if new_u > best_u:
                best_u = new_u
                best_n = neighbor

        return best_n

    def _weighted_neighbor(self, node):
        n = []
        w = []

        for neighbor in self.G.neighbors(node):
            n.append(neighbor)
            w.append(self.get_md(neighbor, U))

        offset = min(w) 
        if offset < 0:
            w = [a-offset+0.1 for a in w]

        return choices(n, weights=w, k=1)[0]

    def _softmax_neighbor(self, node):
        n = []
        w = []

        for neighbor in self.G.neighbors(node):
            n.append(neighbor)
            w.append(exp(self.get_md(neighbor, U)))

        return choices(n, weights=w, k=1)[0]

    def _epsilon_greedy_neighbor(self, node):
        if random() < 0.1:
            return choice(list(self.G.neighbors(node)))

        return self._epsilon_greedy_neighbor(node)
        # return self._best_neighbor(node)

        

        




# from Utility import Average
# from random import random, choice
# from math import inf

# class MDP:
#     def __init__(self, S, P, R, E, START, use_avg):
#         self.S = S
#         self.P = P
#         self.R = R
#         self.E = E
#         self.START = START
#         self.pos = START
#         self.U = {}
#         self.use_avg = use_avg

#         for s in S:
#             if use_avg:
#                 self.U[s] = Average(0,0)
#             else:
#                 self.U[s] = 0

#     def u(self, state):
#         if self.use_avg:
#             val = self.U[state]
#             if val.div == 0:
#                 return 0
                
#             return val.num / val.div
#         else:
#             return self.U[state]

#     def play_through(self, eps=0.1, max_steps=1000):
#         states = [self.START]
#         r = [0]

#         s = self.START
#         steps = 0

#         while s not in self.E:
#             best_s = None
#             best_u = -inf

#             valid_choices = [new_s for new_s in self.P[s]]

#             if random() < eps:
#                 best_s = choice(valid_choices)
#                 best_u = self.u(best_s)
#             else:
#                 for new_s in valid_choices:
#                     next_u = self.u(new_s)
#                     if next_u > best_u:
#                         best_u = next_u
#                         best_s = new_s

#             states.append(best_s)
#             r.append(self.R[s])
#             s = best_s

#             steps += 1
#             if steps > max_steps:
#                 return False, None, [-1000]

#         states.append(s)
#         r.append(self.R[s])

#         return True, states, r

#     def reset(self):
#         self.pos = self.START

#     def next(self, new_state):
#         self.pos = new_state
#         return self.R[new_state]

#     def get_next(self, eps=0.05):
#         valid_choices = [new_s for new_s in self.P[self.pos]]
#         best_s = None
#         best_q = -inf
#         if random() < eps:
#             best_s = choice(valid_choices)
#             best_q = self.U[best_s]
#         else:
#             for new_s in valid_choices:
#                 next_q = self.U[new_s]
#                 if next_q > best_q:
#                     best_q = next_q
#                     best_s = new_s

#         return best_s
