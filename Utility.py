from collections import namedtuple

Position = namedtuple('Position', ['x', 'y'])
Average = namedtuple('Average', ['num', 'div'])


def add_pos(p1, p2):
    return Position(p1.x + p2.x, p1.y + p2.y)