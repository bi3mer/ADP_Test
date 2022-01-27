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
        for i in trange(max_iterations):
            # simplified policy evaluation
            for __ in range(max_iterations - i):
                delta = 0
                new_u = self.utility.copy()
                for s in self.S:
                    s_p = self.pi[s]
                    new_u[s] = self.R[s] + GAMMA * self.P[s][s_p] * self.utility[s_p] 
                    delta = max(delta, abs(self.utility[s] - new_u[s]))

                self.utility = new_u
                if delta < self.theta:
                    break
            
            # policy improvement
            unchanged = True
            for s in self.S:
                old = self.pi[s]

                best_s = None
                best_u = -inf
                for s_p in self.P[s]:
                    u = self.R[s] + GAMMA*sum(self.P[s_p][s_p_p]*self.utility[s_p_p] for s_p_p in self.P[s_p])
                    if u > best_u:
                        best_s = s_p
                        best_u = u

                if old != best_s:
                    self.pi[s] = best_s
                    unchanged = False

            self.utility = new_u
            if unchanged:
                break