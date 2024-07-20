from collections import Counter
from itertools import combinations
from typing import Iterable, Dict
from math import log2, ceil
import unittest


def bare_tree_maker(choise: int) -> list:
    """
    Create an empty tre form a number like:
    1. [[], []]
    2. [[[], []], [[], []]]
    3. ...

    There are 2**dim empty list
    """
    return [bare_tree_maker(choise - 1), bare_tree_maker(choise - 1)] if choise > 0 else []


def tree_maker(words: Iterable[str], index: str, len_index: int, range_index: range) -> list:
    """
    It uses a bare tree to order words,
    the criteria is if there is a letter in the word
    and use a sequence of letters
    """

    tree = bare_tree_maker(len_index)

    for word in words:

        sublist = tree
        for i in range_index:
            sublist = sublist[index[i] in word.lower()]

        if len(sublist) == 0:
            sublist.append(word)
        else:
            # sublist.append(word)
            return None

    return tree


def forest_maker(words: Iterable[str]) -> Dict[str, list]:
    """
    T
    """

    len_index = ceil(log2(len(words)))
    range_index = range(len_index)

    letters = {char for char, count in Counter(char for word in words for char in {
                                               *word.lower()}).items() if 2**len_index/4 <= count <= 2**len_index/2}

    if len(letters) < len_index:
        return {}

    combinations_list = {}

    for index in combinations(letters, len_index):

        tree = tree_maker(words, index, len_index, range_index)
        if tree:
            combinations_list[index] = tree

    return combinations_list


class Test(unittest.TestCase):

    def test_bare_tree_maker(self):
        self.assertEqual(bare_tree_maker(1), [[], []])
        self.assertEqual(bare_tree_maker(2), [[[], []], [[], []]])

    def test_tree_maker(self):
        self.assertEqual(tree_maker(['Ann', 'Bob'], "b", 1, range(1)), [
                         ['Ann'], ['Bob']])

    def test_forest_maker(self):
        self.assertEqual(forest_maker(['Ann', 'Bob']), {('b',): [['Ann'], ['Bob']], ('n',): [
                         ['Bob'], ['Ann']], ('o',): [['Ann'], ['Bob']], ('a',): [['Bob'], ['Ann']]})


if __name__ == "__main__":

    # unittest.main()

    words = ["apple", "banana", "cherry"]

    print(forest_maker(words))
