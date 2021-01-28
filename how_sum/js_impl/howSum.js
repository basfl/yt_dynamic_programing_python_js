const howSum = (target, nums) => {
    if (target === 0) return [];

    if (target < 0) return null;

    for (let element of nums) {
        const reminder = target - element;
        const reminderResult = howSum(reminder, nums)
        if (reminderResult != null) {
            return [...reminderResult, element];
        }
    }

    return null;
}

const memoHowSum = (target, nums, memo={}) => {

    if (target in memo) return memo[target];
    if (target === 0) return [];
    if (target < 0) return null;
    for (let element of nums) {
        const reminder = target - element;
        const reminderResult = memoHowSum(reminder, nums, memo)
        if (reminderResult != null) {
            memo[target] = [...reminderResult, element];
            return memo[target];
        }
    }

    memo[target] = null;
    return null;
}

console.log(howSum(7, [2, 3]))
console.log(howSum(7, [5, 3, 4, 7]));
console.log(howSum(7, [2, 4]));
console.log(howSum(8, [2, 3, 5]));
console.log(memoHowSum(300, [7, 14]));