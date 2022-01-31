from .MDP import MDP
from tqdm import trange

class ValueIteration(MDP):
    def __init__(self, S, P, R, E, START, theta):
        super().__init__(S, P, R, E, START, False)
        self.theta = theta

    def train(self, max_iterations):
        GAMMA = 0.75
        for i in trange(max_iterations):
            new_u = self.U.copy()
            delta = 0

            for s in self.S:
                new_u[s] = self.R[s] + GAMMA * max([self.P[s][next_s] * self.U[next_s] for next_s in self.P[s]])
                delta = max(delta, abs(self.U[s] - new_u[s]))

            self.U = new_u
            if delta < self.theta:
                print(f'Stopped after {i} iterations')
                break
        