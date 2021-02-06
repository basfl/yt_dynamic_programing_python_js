def can_construct_word(target, word_bank):
    table = [False]*(len(target)+1)
    table[0] = True
    for i, _ in enumerate(target):
        if table[i] == True:
            for word in word_bank:
                if target[i:i+len(word)] == word:
                    table[i+len(word)] = True
    return table[len(target)]


print(can_construct_word("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(can_construct_word("skateboard", [
      "bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(can_construct_word("enterapotentpot", [
      "a", "p", "en", "enter", "ot", "o", "t"]))
print(can_construct_word("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
                         ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]))
