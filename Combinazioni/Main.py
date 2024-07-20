from collections import Counter
from itertools import combinations
from typing import Iterable, Dict
from math import log2, ceil


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
            return None
        
    return tree


def forest_maker(words: Iterable[str]) -> Dict[str, list]:

    len_index = ceil(log2(len(words)))

    letters = {char for char, count in Counter(
        "".join(["".join(set(word.lower())) for word in words])).items() if 2**(len_index - 1) <= count < 2**len_index}

    if len(letters) < len_index:
        return None

    indexes = {''.join(perm) for perm in combinations(
        letters, len_index)}

    range_index = range(len_index)

    combinations_list = {}

    for index in indexes:
        tree = tree_maker(words, index, len_index, range_index)
        if tree:
            combinations_list[index] = tree

    return combinations_list


def test():
    print("Test bare_tree_maker()")
    print("bare_tree_maker(1) == [[], []]:", bare_tree_maker(1) == [[], []])
    print("bare_tree_maker(1) == [[], []]:",
          bare_tree_maker(2) == [[[], []], [[], []]])

    print("\nTest tree_maker()")
    print("tree_maker(['Ann', 'Bob'], 'b', 1, range(1)) == [['Ann'], ['Bob']]:", [
          "Ann", "Bob"], tree_maker(['Ann', 'Bob'], "b", 1, range(1)) == [['Ann'], ['Bob']])

    print("\nTest forest_maker()")
    print("forest_maker(['Ann', 'Bob']) == {'o': [['Ann'], ['Bob']], 'n': [['Bob'], ['Ann']], 'b': [['Ann'], ['Bob']], 'a': [['Bob'], ['Ann']]}:", forest_maker(
        ['Ann', 'Bob']) == {'o': [['Ann'], ['Bob']], 'n': [['Bob'], ['Ann']], 'b': [['Ann'], ['Bob']], 'a': [['Bob'], ['Ann']]})


if __name__ == "__main__":

    # test()

    words = ["apple", "banana", "cherry", "blueberry"]

    print(forest_maker(words))
