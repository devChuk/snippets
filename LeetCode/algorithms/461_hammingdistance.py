"""
The Hamming distance between two integers is the number of positions
at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.
"""

def hammingDistance(x, y):
    """
    :type x: int
    :type y: int
    :rtype: int
    """
    binary_x = '{0:032b}'.format(x)
    binary_y = '{0:032b}'.format(y)

    count = 0
    for index, char in enumerate(binary_x):
        if (char != binary_y[index]):
            count += 1

    return count
