from random import choice
from tqdm import trange
from math import inf
from .MDP import MDP

class PolicyIteration(MDP):
    def __init__(self, S, P, R, E, START, theta):
        super().__init__(S, P, R, E, START, False)
        self.theta = theta

        # create a random policy
        self.pi = {} 
        for s in S:
            self.pi[s] = choice(list(self.P[s].keys()))
            
    def train(self, max_iterations):
        GAMMA = 0.75
        ITER = 20
        delta = 0

        for i in trange(0, max_iterations, ITER):
            # simplified policy evaluation
            for _ in range(ITER):
                for s in self.S:
                    self.utility[s] = self.R[s] + self.P[s][self.pi[s]] * self.utility[self.pi[s]]

            # policy improvement
            unchanged = True
            for s in self.S:
                old = self.pi[s]

                best_s = None
                best_u = -inf
                for s_p in self.P[s]:
                    if self.utility[s_p] > best_u:
                        best_s = s_p
                        best_u = self.utility[s_p]

                if old != best_s:
                    self.pi[s] = best_s
                    unchanged = False

            if unchanged:
                break

        print(f'Stopped after {i} iteration, {delta}')