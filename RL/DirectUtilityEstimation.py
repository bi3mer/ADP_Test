from .MDP import MDP
from Utility import Average

from tqdm import trange

class DirectUtilityEstimation(MDP):
    def __init__(self, S, A, P, R, E, START):
        super().__init__(S, A, P, R, E, START)

    def train(self, max_iterations):
        for _ in trange(max_iterations):
            states, reward = self.play_through()
            for s in states:
                val = self.utility[s]
                self.utility[s] = Average(val.num + reward, val.div + 1)
                