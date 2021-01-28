const bestSum = (target, nums) => {
    if (target === 0) return [];

    if (target < 0) return null;
    let shortestCombination = null;
    for (let element of nums) {
        const reminder = target - element;
        const reminderResult = bestSum(reminder, nums)
        if (reminderResult != null) {
            const combination = [...reminderResult, element];
            if (shortestCombination === null || combination.length < shortestCombination.length) {
                shortestCombination = combination

            }
        }
    }

    return shortestCombination;
}


console.log(bestSum(7, [5, 3, 4, 7]))