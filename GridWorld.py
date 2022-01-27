from Utility import Position, add_pos
from enum import Enum

class Action(Enum):
    LEFT = 0
    RIGHT = 1
    UP = 2
    DOWN = 3

def action_to_tuple(action):
    if action == Action.LEFT:
        return Position(-1, 0)
    elif action == Action.RIGHT:
        return Position(1,0)
    elif action == Action.UP:
        return Position(0,1)
    elif action == Action.DOWN:
        return Position(0,-1)
    
    raise ValueError(f'Unregistered action type: {action}')

MAX_X = 4
MAX_Y = 3
BLANK_STATE = Position(1,1)
START = Position(0,0)   

S = [Position(x, y) for y in range(3) for x in range(4)]
A = [Action.LEFT, Action.RIGHT, Action.UP, Action.DOWN]
P = {}
R = {}

for s in S:
    # slight movement penalty
    R[s] = -0.05

    # probability for actions
    P[s] = {}
    for a in A:
        new_s = add_pos(s, action_to_tuple(a))  

        if new_s != BLANK_STATE and new_s.x >= 0 and new_s.x < MAX_X and new_s.y >= 0 and new_s.y < MAX_Y:
            P[s][new_s] = 1

WIN_STATE = Position(3,2)
LOSE_STATE = Position(3,1)
R[Position(3,1)] = -1
R[Position(3,2)] = 1

E = [Position(3,1), Position(3,2)] # End states

def display(s):
    print('-----------------')
    for y in reversed(range(MAX_Y)):
        out = '| '
        for x in range(MAX_X):
            cur_state = Position(x, y)
            if s == cur_state:
                out += '@'
            elif cur_state == LOSE_STATE:
                out += 'L'
            elif cur_state == WIN_STATE:
                out += 'W'
            elif cur_state == BLANK_STATE:
                out += 'X'
            else:
                out += ' '

            out += ' | '
        
        print(out)
        print('-----------------')

def display_utility(rl):
    print('-----------------------------')
    for y in reversed(range(MAX_Y)):
        out = '| '
        for x in range(MAX_X):
            cur_state = Position(x, y)
            out +=  '{:.2f} | '.format(rl.u(cur_state))
        
        print(out)
        print('-----------------------------')
            
