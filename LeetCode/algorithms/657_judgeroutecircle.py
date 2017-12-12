"""
Initially, there is a Robot at position (0, 0).
Given a sequence of its moves, judge if this robot makes a circle, which
means it moves back to the original place.

The move sequence is represented by a string. And each move is represent
by a character. The valid robot moves are R (Right), L (Left), U (Up)
and D (down). The output should be true or false representing whether the
robot makes a circle.
"""


def judgeCircle(moves):
    """
    :type moves: str
    :rtype: bool
    """
    x = 0
    y = 0
    for char in moves:
        if char == 'U':
            y += 1
        elif char == 'D':
            y -= 1
        elif char == 'L':
            x -= 1
        elif char == 'R':
            x += 1

    return x == 0 and y == 0
