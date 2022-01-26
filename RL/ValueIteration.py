from .MDP import MDP
from tqdm import trange

class ValueIteration(MDP):
    def __init__(self, S, P, R, E, START, theta):
        super().__init__(S, P, R, E, START, False)
        self.theta = theta

    def train(self, max_iterations):
        GAMMA = 0.75
        for i in trange(max_iterations):
            new_u = self.utility.copy()
            delta = 0

            for s in self.S:
                new_u[s] = self.R[s] + GAMMA * max([self.P[s][next_s] * self.utility[next_s] for next_s in self.P[s] if self.P[s][next_s] > 0])
                delta = max(delta, abs(self.utility[s] - new_u[s]))

            self.utility = new_u
            if delta < self.theta:
                print(f'Stopped after {i} iterations')
                break
        
        print(delta)
