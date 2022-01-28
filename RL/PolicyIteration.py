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
        GAMMA = 0.9
        ITER = 2
        for i in trange(0, max_iterations, ITER):
            # simplified policy evaluation
            for _ in range(ITER):
                new_u = self.utility.copy()
                for s in self.S:
                    W = 1.0 / float(len(self.P[s]))
                    new_u[s] = self.R[s] + GAMMA * sum([W * self.P[s][next_s] * self.utility[next_s] for next_s in self.P[s]])

                self.utility = new_u

            # policy improvement
            unchanged = True
            for s in self.S:
                old = self.pi[s]

                best_s = None
                best_u = -inf
                for s_p in self.P[s]:
                    u = self.R[s] + GAMMA*max(self.P[s_p][s_p_p]*self.utility[s_p_p] for s_p_p in self.P[s_p])
                    if u > best_u:
                        best_s = s_p
                        best_u = u

                if old != best_s:
                    self.pi[s] = best_s
                    unchanged = False

            if unchanged:
                break

        print(f'Stopped after {i} iterations')