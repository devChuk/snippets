"""Just a small refresh in Python."""


def get_char_count(s):
    """Self explanatory."""
    char_count = {}

    for c in s:
        if s in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 0

    return char_count


def is_anagram(a, b):
    """Also self explanatory."""
    if len(a) is not len(b):
        return False

    if get_char_count(a) == get_char_count(b):
        return True
    else:
        return False


def steps_required(n):
    """Count the amount of steps needed to reach n with 2 or 3 steps."""
    if (n is 0):
        return 0
    elif (n <= 2):
        return steps_required(n - 1)

'test'[2]


def is_substring(a, b):
    """A."""
    pass


def count_substrings(s, a):
    """Amount of times a is found inside s."""
    for c in s:
        if c == a[0]:
            pass


def two_sum(self, nums, target):
    """
    :type nums: List[int].

    :type target: int
    :rtype: List[int]
    """
    lookup = {}
    for i, num in enumerate(nums):
        if target - num in lookup:
            return [lookup[target - num], i]
        lookup[num] = i
    return []

# for x in range(0, 3):

# >>> x = "Hello World!"
# >>> x[2:]
# 'llo World!'
# >>> x[:2]
# 'He'
# >>> x[:-2]
# 'Hello Worl'
# >>> x[-2:]
# 'd!'
# >>> x[2:-2]
# 'llo Worl'
