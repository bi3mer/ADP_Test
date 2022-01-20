from Utility import Position

class GridWorld:
    def __init__(self):
        self.state = Position(0,0)
        self.LOSE_STATE = Position(3,1)
        self.WIN_STATE = Position(3,2)
        self.EMPTY = Position(1,1)
        self.MAX_Y = 3
        self.MAX_X = 4

        self.STATES = [Position(x, y) for y in range(self.MAX_Y) for x in range(self.MAX_X)]

    def new(self):
        self.state = Position(0,0)

    def next_states(self):
        states = []

        # up
        new_y = self.state.y + 1
        if new_y < self.MAX_Y:
            new_pos = Position(self.state.x, new_y)
            if new_pos != self.EMPTY:
                states.append(new_pos)

        # down
        new_y = self.state.y - 1
        if new_y >= 0:
            new_pos = Position(self.state.x, new_y)
            if new_pos != self.EMPTY:
                states.append(new_pos)

        # right
        new_x = self.state.x + 1
        if new_x < self.MAX_X:
            new_pos = Position(new_x, self.state.y)
            if new_pos != self.EMPTY:
                states.append(new_pos)

        # left
        new_x = self.state.x - 1
        if new_x  >= 0:
            new_pos = Position(new_x, self.state.y)
            if new_pos != self.EMPTY:
                states.append(new_pos)

        return states

    def reward(self):
        if self.state == self.LOSE_STATE:
            return -1
        elif self.state == self.WIN_STATE:
            return 1
        else:
            return 0

    def display(self):
        print('-----------------')
        for y in reversed(range(self.MAX_Y)):
            out = '| '
            for x in range(self.MAX_X):
                cur_state = Position(x, y)
                if self.state == cur_state:
                    out += '@'
                elif cur_state == self.LOSE_STATE:
                    out += 'L'
                elif cur_state == self.WIN_STATE:
                    out += 'W'
                elif cur_state == self.EMPTY:
                    out += 'X'
                else:
                    out += ' '

                out += ' | '
            
            print(out)
            print('-----------------')

    def display_utility(self, rl):
        print('-----------------------------')
        for y in reversed(range(self.MAX_Y)):
            out = '| '
            for x in range(self.MAX_X):
                cur_state = Position(x, y)
                out +=  '{:.2f} | '.format(rl.u(cur_state))
            
            print(out)
            print('-----------------------------')
            
