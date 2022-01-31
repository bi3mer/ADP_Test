from .MDP import MDP
from tqdm import trange

class TemporalDifference(MDP):
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
            states, reward = self.play_through()
            if states == None:
                continue

            for i in range(len(states) - 1):
                s = states[i]
                s_p = states[i + 1]
                r_p = reward[i + 1]
    
                N[s] += 1
                self.U[s] += (60.0/(59 + N[s]))*(r_p + GAMMA*self.U[s_p] - self.U[s])