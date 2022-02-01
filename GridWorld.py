from Utility import Position, add_pos
from enum import Enum

class Action(Enum):
    LEFT = 0
    RIGHT = 1
    UP = 2
    DOWN = 3

def action_to_str(action):
    if action == Action.LEFT:
        return 'L'
    elif action == Action.RIGHT:
        return 'R'
    elif action == Action.UP:
        return 'U'
    elif action == Action.DOWN:
        return 'D'
    
    raise ValueError(f'Unregistered action type: {action}')

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

MAX_X = 5
MAX_Y = 5
BLANK_STATE = Position(1,1)
START = Position(0,0)   

S = [Position(x, y) for y in range(MAX_Y) for x in range(MAX_X)]
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

WIN_STATE = Position(MAX_X-1,MAX_Y-1)
LOSE_STATE = Position(MAX_X-1,MAX_Y-2)
R[LOSE_STATE] = -1
R[WIN_STATE] = 1

E = [LOSE_STATE, WIN_STATE] # End states

def display(s):
    print('----' * MAX_X + '-')
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
        print('----' * MAX_X + '-')

def display_utility(rl):
    print('--------' * MAX_X + '-')
    for y in reversed(range(MAX_Y)):
        out = '| '
        for x in range(MAX_X):
            cur_state = Position(x, y)
            out +=  '{:.2f} | '.format(rl.u(cur_state))
        
        print(out)
        print('--------' * MAX_X + '-')


def display_policy(rl):
    try:
        pi = rl.pi
    except:
        print(f'{rl} does not have a policy associated with it.')
        return

    print('-----' * MAX_X + '-')
    for y in reversed(range(MAX_Y)):
        out = '| '
        for x in range(MAX_X):
            cur_state = Position(x, y)
            pi_state = pi[cur_state]

            if cur_state.x < pi_state.x:
                a = 'R'
            elif cur_state.x > pi_state.x:
                a = 'L'
            elif cur_state.y < pi_state.y:
                a = 'U'
            elif cur_state.y > pi_state.y:
                a = 'D'
            else:
                print(f'{cur_state} -> {pi_state} is not possible')
                a = '?'

            out = f'{out} {a} | '
        
        print(out)
        print('-----' * MAX_X + '-')