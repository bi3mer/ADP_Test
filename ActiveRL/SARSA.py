from .QTable import QTable
from tqdm import trange

class SARSA(QTable):
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
            self.reset()
            s = self.START
            s_1, _ = self.get_next(s)
            while s not in self.E:
                N[s] += 1
                s_2, _ = self.get_next(s_1)

                ALPHA = (60.0/(59.0 + N[s]))
                self.Q[s][s_1] += ALPHA*(self.R[s] + GAMMA*self.Q[s_1][s_2] - self.Q[s][s_1])

                s = s_1
                s_1 = s_2

            self.Q[s][0] = self.R[s]
            