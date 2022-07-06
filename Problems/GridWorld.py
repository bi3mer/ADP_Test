import networkx as nx
from .Keys import *


def build_grid_world(MAX_X, MAX_Y):
    g = nx.DiGraph() 

    for y in range(MAX_Y):
        for x in range(MAX_X):
            # ignore the blank position
            if y == 1 and x == 1:
                continue

            # create node and its reward
            src = f'{y}_{x}'
            g.add_node(src)
            if x == MAX_X - 1 and y == MAX_Y - 1:
                g.nodes[src][R] = 1
                g.nodes[src][E] = True
            elif x == MAX_X - 1 and y == MAX_Y - 2:
                g.nodes[src][R] = -1
                g.nodes[src][E] = True
            else:
                g.nodes[src][R] = -0.05
                g.nodes[src][E] = False

            # create left connection
            if x - 1 >= 0 and not (x - 1 == 1 and y == 1):
                g.add_edge(src, f'{y}_{x-1}')

            # create right connection
            if x + 1 < MAX_X and not (x + 1 == 1 and y == 1):
                g.add_edge(src, f'{y}_{x+1}')

            # create up connection
            if y - 1 >= 0  and not (x == 1 and y - 1 == 1):
                g.add_edge(src, f'{y-1}_{x}')

            # create down connection
            if y + 1 < MAX_Y and not (x == 1 and y + 1 == 1):
                g.add_edge(src, f'{y+1}_{x}')

    return f'0_0', g


def display(G, position, MAX_X, MAX_Y):
    for y in reversed(range(MAX_Y)):
        out = ''
        for x in range(MAX_X):
            cur_state = f'{y}_{x}'
            
            if not G.has_node(cur_state):
                # check if blank state
                out += 'X'
            else:            
                # otherwise, get node and set value
                r = G.nodes[cur_state][R]
                if position == cur_state:
                    out += '@'
                elif r == -1:
                    out += 'L'
                elif r == 1:
                    out += 'W'
                else:
                    out += '-'

        print(out)

# def display_utility(rl):
#     print('--------' * MAX_X + '-')
#     for y in reversed(range(MAX_Y)):
#         out = '| '
#         for x in range(MAX_X):
#             cur_state = Position(x, y)
#             out +=  '{:.2f} | '.format(rl.u(cur_state))
        
#         print(out)
#         print('--------' * MAX_X + '-')


# def display_policy(rl):
#     try:
#         pi = rl.pi
#     except:
#         print(f'{rl} does not have a policy associated with it.')
#         return

#     print('-----' * MAX_X + '-')
#     for y in reversed(range(MAX_Y)):
#         out = '| '
#         for x in range(MAX_X):
#             cur_state = Position(x, y)
#             pi_state = pi[cur_state]

#             if cur_state.x < pi_state.x:
#                 a = 'R'
#             elif cur_state.x > pi_state.x:
#                 a = 'L'
#             elif cur_state.y < pi_state.y:
#                 a = 'U'
#             elif cur_state.y > pi_state.y:
#                 a = 'D'
#             else:
#                 print(f'{cur_state} -> {pi_state} is not possible')
#                 a = '?'

#             out = f'{out} {a} | '
        
#         print(out)
#         print('-----' * MAX_X + '-')