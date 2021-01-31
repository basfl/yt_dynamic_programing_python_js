import pytest
from count_construct_word import count_construct_word


@pytest.mark.parametrize("word, word_bank,expect", [("abcdef", ["ab", "abc", "cd", "def", "abcd"], 1),
("enterapotentpot", [
 "a", "p", "en", "enter", "ot", "o", "t"
],4),
                                                    ("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", [
                                                     "e", "ee", "eee", "eeee", "eeeee", "eeeeee"], 0)
                                                    ])
def test_can_construct_word(word, word_bank, expect):
    assert count_construct_word(
        word, tuple(word_bank)) == expect, "failed"
