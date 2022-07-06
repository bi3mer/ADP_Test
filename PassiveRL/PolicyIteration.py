from random import choice, choices
from math import inf, exp
from .MDP import MDP
from Problems.Keys import *

class PolicyIteration(MDP):
    def __init__(self, graph, policy_iter, gamma):
        super().__init__(graph, 'Policy')

        self.GAMMA = gamma
        self.POLICY_ITER = policy_iter

    def __get_u(self, n):
        return self.get_md(n, U)
        # if self.get_md(n, C) >= 2:
        #     return self.get_md(n, U)

        # return (1 + self.get_md(n, U))**2
        # return 2 + self.get_md(n, U)

    def update(self, _):
        # create a random policy
        self.pi = {} 
        for n in self.G:
            self.pi[n] = choice(list(self.G.neighbors(n)))

        # all utility values are reset to 0. Note, in time-sensitive computations
        # this could be only done every once in a while, but this hasn't been an
        # issue in our use case since the graphs we use are not large enough. It 
        # takes less than half a second to converge, and this isn't an optimized
        # implementation and, after all, this is Python.
        self._reset_utility()

        # run policy iteration
        i = 0
        while True:
            # policy evaluation
            for __ in range(self.POLICY_ITER):
                for n in self.G:
                    r = self.get_md(n, R) 
                    # u = self.__get_u(self.pi[n])
                    u = max(self.__get_u(n_p) for n_p in self.G.neighbors(n)) 
                    self.set_md(n, U, r + self.GAMMA*u)
            
            # policy improvement
            changed = False
            for n in self.G:
                old = self.pi[n]

                best_s = None
                best_u = -inf
                for n_p in self.G.neighbors(n):
                    u_p = self.__get_u(n_p)
                    if u_p > best_u:
                        best_s = n_p
                        best_u = u_p

                if old != best_s:
                    self.pi[n] = best_s
                    changed = True
            
            i+=1
            if not changed:
                break
            
        print(f'{i} iterations to converge')
        
    def get(self, node, k):
        # def __p(k):
        #     print(k)
        #     print(f'\tC: {self.get_md(k, C)}')
        #     print(f'\tU: {self.get_md(k, U)}')
        #     print(f'\tR: {self.get_md(k, R)}')

        #     for n in self.G.neighbors(k):
        #         print(f'\t\t{n} :: {self.pi[k] == n}\t:: R={self.get_md(n, R):.5f} :: U={self.get_md(n, U):.5f}')

        # print(f'{node} -> {self.pi[node]}')
        # __p(node)
        # print()

        nodes = []
        size = 0
        while size < k:
            node = self.pi[node]
            nodes.append(node)
            size += 1 * '__' not in node # small optimization to remove branching

        return nodes

    def get_starting_node(self):
        nodes = list(self.visited_iter())
        weights = [exp(self.__get_u(n)) for n in nodes]
        return choices(nodes, weights=weights, k=1)[0]



# from random import choice
# from tqdm import trange
# from math import inf
# from .MDP import MDP

# class PolicyIteration(MDP):
#     def __init__(self, S, P, R, E, START, theta):
#         super().__init__(S, P, R, E, START, False)
#         self.theta = theta

#         # create a random policy
#         self.pi = {} 
#         for s in S:
#             self.pi[s] = choice(list(self.P[s].keys()))
            
#     def train(self, max_iterations):
#         GAMMA = 0.75
#         ITER = 2

#         for i in trange(0, max_iterations, ITER):
#             # simplified policy evaluation
#             for _ in range(ITER):
#                 for s in self.S:
#                     self.U[s] = self.R[s] + GAMMA * self.P[s][self.pi[s]] * self.U[self.pi[s]]

#             # policy improvement
#             unchanged = True
#             for s in self.S:
#                 old = self.pi[s]

#                 best_s = None
#                 best_u = -inf
#                 for s_p in self.P[s]:
#                     if self.U[s_p] > best_u:
#                         best_s = s_p
#                         best_u = self.U[s_p]

#                 if old != best_s:
#                     self.pi[s] = best_s
#                     unchanged = False

#             if unchanged:
#                 break

#         print(f'{i}/{max_iterations} iterations to converge')