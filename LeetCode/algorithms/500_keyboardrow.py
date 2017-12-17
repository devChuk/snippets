"""
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.

Example 1:
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
Note:
You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.
"""

def findWords(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    rows = [set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')]
    result = []

    for word in words:
        lower_word = word.lower()
        contains = set()
        for c in lower_word:
            for index, row in enumerate(rows):
                if c in row:
                    contains.add(index)

        if len(contains) <= 1:
            result.append(word)
    return result
