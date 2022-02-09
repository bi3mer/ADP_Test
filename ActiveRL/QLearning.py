from .QTable import QTable
from tqdm import trange

class QLearning(QTable):
    def __init__(self, S, P, R, E, START):
        super().__init__(S, P, R, E, START, False)

    def train(self, max_iterations):
        GAMMA = 0.9

        # adaptive learning rate based on how many times a state has been 
        # visited instead of using a static alpha=0.001 or whatever.
        N = {}
        for s in self.S:
            N[s] = 1

        for _ in trange(max_iterations):
            s = self.START
            while s not in self.E:
                N[s] += 1
                new_s, _ = self.get_next(s)

                ALPHA = (60.0/(59.0 + N[s]))
                self.Q[s][new_s] += ALPHA*(self.R[s] + GAMMA*self.u(new_s) - self.Q[s][new_s])
                s = new_s

            self.Q[s][0] = self.R[s]
