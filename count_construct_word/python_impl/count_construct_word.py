from functools import lru_cache


@lru_cache(maxsize=10000)
def count_construct_word(target, word_bank):
    if target == "":
        return 1
    total_count = 0
    for word in word_bank:
        if word in target:
            # print(word)
            if(target.index(word) == 0):
                # suffix = target.split(word)[1]
                suffix = target[len(word):]
                # print("suffix"+suffix)
                number_of_ways = count_construct_word(suffix, word_bank)
                total_count += number_of_ways

    return total_count


print(count_construct_word("purple", tuple(
    ["purp", "p", "ur", "le", "purpl"])))
print(count_construct_word("abcdef", tuple(
    ["ab", "abc", "cd", "def", "abcd"])))
print(count_construct_word("skateboard", tuple([
      "bo", "rd", "ate", "t", "ska", "sk", "boar"])))
print(count_construct_word("enterapotentpot", tuple([
    "a", "p", "en", "enter", "ot", "o", "t"])))
print(count_construct_word("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
                           tuple(["e", "ee", "eee", "eeee", "eeeee", "eeeeee"])))
