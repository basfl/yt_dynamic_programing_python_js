const canConstruct = (target, wordBank) => {
    if (target === "") {
        return true
    }

    for (let word of wordBank) {
        if (target.indexOf(word) === 0) {
            const suffix = target.slice(word.length);
            if (canConstruct(suffix, wordBank) == true) {
                return true
            }
        }
    }
    return false
}


const memoCanConstruct = (target, wordBank, memo = {}) => {
    if (target in memo) return memo[target];
    if (target === "") {
        return true;
    }

    for (let word of wordBank) {
        if (target.indexOf(word) === 0) {
            const suffix = target.slice(word.length);
            if (memoCanConstruct(suffix, wordBank, memo) == true) {
                memo[target] = true;
                return true;
            }
        }
    }
    memo[target] = false;
    return false;
}



// console.log(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]));
// console.log(canConstruct("skateboard", [
//     "bo", "rd", "ate", "t", "ska", "sk", "boar"
// ]));

// console.log(canConstruct("enterapotentpot", [
//     "a", "p", "en", "enter", "ot", "o", "t"
// ]))
// console.log(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
//     ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]))


console.log(memoCanConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]));
console.log(memoCanConstruct("skateboard", [
    "bo", "rd", "ate", "t", "ska", "sk", "boar"
]));

console.log(memoCanConstruct("enterapotentpot", [
    "a", "p", "en", "enter", "ot", "o", "t"
]))
console.log(memoCanConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
    ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]))