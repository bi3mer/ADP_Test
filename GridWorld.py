from Utility import Position

class GridWorld:
    def __init__(self):
        self.state = Position(0,0)
        self.LOSE_STATE = Position(3,1)
        self.WIN_STATE = Position(3,2)
        self.EMPTY = Position(1,1)
        self.MAX_Y = 3
        self.MAX_X = 4

    def next_states(self):
        states = []

        # up
        new_y = self.state.y + 1
        if new_y < self.MAX_Y:
            if not (self.state.x == self.EMPTY.x and new_y == self.EMPTY.y):
                states.append(Position(self.state.x, new_y))

        # down
        new_y = self.state.y - 1
        if new_y - 1 >= 0:
            if not (self.state.x == self.EMPTY.x and new_y == self.EMPTY.y):
                states.append(Position(self.state.x, new_y))

        # right
        new_x = self.state.x + 1
        if new_x + 1 < self.MAX_X:
            if not (new_x == self.EMPTY.x and self.state.x == self.EMPTY.y):
                states.append(Position(new_x, self.state.y))

        # left
        new_x = self.state.x - 1
        if new_x - 1 >= 0:
            if not (new_x == self.EMPTY.x and self.state.x == self.EMPTY.y):
                states.append(Position(new_x, self.state.y))

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
            
