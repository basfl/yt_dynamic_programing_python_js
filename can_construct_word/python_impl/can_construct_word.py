from functools import lru_cache


def can_construct_word(target, word_bank):
    if target == "":
        return True
    for word in word_bank:
        if word in target:
            # print(word)
            if(target.index(word) == 0):
                #suffix = target.split(word)[1]
                suffix = target[len(word):]
                # print("suffix"+suffix)
                if can_construct_word(suffix, word_bank) == True:
                    return True
    return False


@lru_cache(maxsize=10000)
def memo_can_construct_word(target, word_bank):
    if target == "":
        return True
    for word in word_bank:
        if word in target:
            # print(word)
            if(target.index(word) == 0):
                #suffix = target.split(word)[1]
                suffix = target[len(word):]
                # print("suffix"+suffix)
                if memo_can_construct_word(suffix, word_bank) == True:
                    return True
    return False

# print(can_construct_word("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
# print(can_construct_word("skateboard", [
#       "bo", "rd", "ate", "t", "ska", "sk", "boar"]))
# print(can_construct_word("enterapotentpot", [
#       "a", "p", "en", "enter", "ot", "o", "t"]))
# print(can_construct_word("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
#                          ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]))


print(memo_can_construct_word("abcdef", tuple(
    ["ab", "abc", "cd", "def", "abcd"])))
print(memo_can_construct_word("skateboard", tuple([
      "bo", "rd", "ate", "t", "ska", "sk", "boar"])))
print(memo_can_construct_word("enterapotentpot", tuple([
      "a", "p", "en", "enter", "ot", "o", "t"])))
print(memo_can_construct_word("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
                              tuple(["e", "ee", "eee", "eeee", "eeeee", "eeeeee"])))
