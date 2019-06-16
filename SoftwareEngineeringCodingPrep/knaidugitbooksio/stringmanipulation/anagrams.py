"""
    Write a function that will accept a
        jumble of letters as well as a dictionary,
        and output a list of words that the match
        in the dictionary.
Example
    input: grabscrab("ortsp", ["sport", "parrot", "ports", "matey"])
    output: ["sport", "ports"]
"""

# grabscrab("oolp", ["donkey", "pool", "horse", "loop"]) == ["pool", "loop"]


from itertools import permutations
import unittest


def get_possible_combination_of_word(arg):
    possible_permutation_list = [''.join(p) for p in permutations(arg)]
    unique_possible_pmtn_lst = list(set(possible_permutation_list))
    return unique_possible_pmtn_lst


# O(n^2)
def grabscrab(anagram_check_word, check_anagaram_list):
    poss_cmbn_list = get_possible_combination_of_word(anagram_check_word)
    result = []

    for x in poss_cmbn_list:
        for y in check_anagaram_list:
            # print("{} == {}".format(x, y))
            if x == y:
                result.append(x)
        # print()

    # print(list(set(result)))
    return list(set(result))


# print(grabscrab("oolp", ["donkey", "pool", "horse", "loop"]))
# print(grabscrab("ourf", ["one", "two", "three"]))


class TestAnagrams(unittest.TestCase):
    def setUp(self):
        pass

    def test_grabscrab(self):
        assert (grabscrab("trisf", ["first"]) == ["first"])
        assert (grabscrab("oob", ["bob", "baobab"]) == [])
        assert (grabscrab("ainstuomn", ["mountains", "hills", "mesa"]) == ["mountains"])
        assert (grabscrab("oolp", ["donkey", "pool", "horse", "loop"]) == ["pool", "loop"])
        assert (grabscrab("ortsp", ["sport", "parrot", "ports", "matey"]) == ["sport", "ports"])
        assert (grabscrab("ourf", ["one", "two", "three"]) == [])


if __name__ == "__main__":
    unittest.main()

"""
Test cases:
    Test.expect(grabscrab("trisf", ["first"]) == ["first"])
    Test.expect(grabscrab("oob", ["bob", "baobab"]) == [])
    Test.expect(grabscrab("ainstuomn", ["mountains", "hills", "mesa"]) == ["mountains"])
    Test.expect(grabscrab("oolp", ["donkey", "pool", "horse", "loop"]) == ["pool", "loop"])
    Test.expect(grabscrab("ortsp", ["sport", "parrot", "ports", "matey"]) == ["sport", "ports"])
    Test.expect(grabscrab("ourf", ["one","two","three"]) == [])
"""