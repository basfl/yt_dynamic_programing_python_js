const countConstruct = (target, wordBank) => {
    if (target === "") {
        return 1
    }
    let total = 0;
    for (let word of wordBank) {
        if (target.indexOf(word) === 0) {
            const suffix = target.slice(word.length);
            const numWays = countConstruct(suffix, wordBank);
            total += numWays;

        }
    }
    return total;
}


const memoCountConstruct = (target, wordBank, memo = {}) => {
    if (target in memo) return memo[target];
    if (target === "") {
        return 1
    }
    let total = 0;
    for (let word of wordBank) {
        if (target.indexOf(word) === 0) {
            const suffix = target.slice(word.length);
            const numWays = memoCountConstruct(suffix, wordBank, memo);
            total += numWays;

        }
    }
    memo[target] = total;
    return total;
}




console.log(countConstruct("purple", ["purp", "p", "ur", "le", "purpl"]));
console.log(countConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]));
console.log(countConstruct("skateboard", [
    "bo", "rd", "ate", "t", "ska", "sk", "boar"
]));

console.log(countConstruct("enterapotentpot", [
    "a", "p", "en", "enter", "ot", "o", "t"
]))
// console.log(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
//     ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]))

console.log("-------------------memoization-----------")

console.log(memoCountConstruct("purple", ["purp", "p", "ur", "le", "purpl"]));
console.log(memoCountConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]));
console.log(memoCountConstruct("skateboard", [
    "bo", "rd", "ate", "t", "ska", "sk", "boar"
]));

console.log(memoCountConstruct("enterapotentpot", [
    "a", "p", "en", "enter", "ot", "o", "t"
]));
console.log(memoCountConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
    ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]));