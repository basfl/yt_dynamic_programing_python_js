const canConstruct = (target, wordBank) => {
    const table = Array(target.length + 1).fill(false);
    table[0] = true;
    for (let i = 0; i <= target.length; i++) {
        if (table[i] === true) {
            for (let word of wordBank) {
                if (target.slice(i, i + word.length) === word) {
                    table[i + word.length] = true;
                } //end of if for slice

            } //end of for loop for wordbank

        } //end of if

    }// end of for 
    return table[target.length];
}


console.log(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]));
console.log(canConstruct("skateboard", [
    "bo", "rd", "ate", "t", "ska", "sk", "boar"
]));

console.log(canConstruct("enterapotentpot", [
    "a", "p", "en", "enter", "ot", "o", "t"
]))
console.log(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
    ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]))
