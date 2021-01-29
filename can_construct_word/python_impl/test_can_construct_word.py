import pytest
import can_construct_word


@pytest.mark.parametrize("word, word_bank,expect", [("abcdef", ["ab", "abc", "cd", "def", "abcd"], True),
                                                    ("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", [
                                                     "e", "ee", "eee", "eeee", "eeeee", "eeeeee"], False)
                                                    ])
def test_can_construct_word(word, word_bank, expect):
    assert can_construct_word.memo_can_construct_word(
        word, tuple(word_bank)) == expect, "failed"
