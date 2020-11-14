#!/usr/bin/env python3

import random
import sys

"""
Stanford CS106A Mimic Project.
"""


# --- Define your functions here ---

def bigrams_create(filename):
    """
    Reads a file and creates a bigrams data structure
    Should not remove punctuation
    Should not change upper/lower case
    Duplicate values not allowed
    >>> bigrams_create('test-tiny.txt')
    {'': ['a'], 'a': ['b', 'c.'], 'b': ['a']}
    >>> bigrams_create('test-small.txt')
    {'': ['a'], 'a': ['b', 'c', 'd.'], 'b': ['a'], 'c': ['a']}
    >>> bigrams_create('test-roses.txt')
    {'': ['Roses'], 'Roses': ['are'], 'are': ['red', 'blue.'], 'red': ['violets'], 'violets': ['are']}
    """
    with open(filename, 'r') as f:
        text = f.read()
        words = text.split()
        words.append(' ')
        bigrams = {}
        previous = ''

        for next in words:
            if previous not in bigrams:
                bigrams[previous] = []
            following = bigrams[previous]
            if next not in following:
                following.append(next)
            previous = next

        return bigrams


def random_gen(bigrams, minimum):
    """
    No Doctests since cannot predict randomness.
    Starts with empty string '' as the Choice.
    Select at random a word that follows the Choice.
    Print the Choice + ' ' (no \n)
    If no Choice available, use ''
    Prints a minimum parameter.
    After minimum, a word ending with ';' or '.' triggers break
    """
    result = ''
    choice = ''
    count = 0
    while count <= minimum or not (choice.endswith('.') or choice.endswith(';')):
        values_list = bigrams[choice]
        follow = random.choice(values_list)
        result += follow + ' '
        choice = follow
        count += 1
    return result


def main():
    """
    Takes in a filename.
    Opens the file and converts it all to string.
    Sends string straight to bigrams_create
    bigrams_create sends back the dict.
    Send the dict and result string to random_print for minimum times
    """
    args = sys.argv[1:]
    # Two possible command-line forms:
    # filename
    # filename limit_num
    minimum = 25  # default minimum value

    # assume no limit_num is given
    filename = args[0]

    if len(args) == 2:
        minimum = int(args[1])

    if len(args) > 0:
        bigrams = bigrams_create(filename)
        result = random_gen(bigrams, minimum)
        print(result)

if __name__ == '__main__':
    main()
