from .Playthrough import play_through
from Utility import Average

from tqdm import trange

class DirectUtilityEstimation:
    def __init__(self, game):
        self.game = game
        self.utility = {}
        for s in game.STATES:
            self.utility[s] = Average(0, 0)

    def u(self, state):
        val = self.utility[state]
        if val.div == 0:
            return 0
            
        return val.num / val.div

    def train(self, max_iterations):
        for _ in trange(max_iterations):
            states, reward = play_through(self, self.game)
            for s in states:
                val = self.utility[s]
                self.utility[s] = Average(val.num + reward, val.div + 1)
                