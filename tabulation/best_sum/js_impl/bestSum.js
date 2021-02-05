const bestSum = (target, numbers) => {
    const table = Array(target + 1).fill(null);
    table[0] = [];
    for (let i = 0; i < table.length; i++) {
        if (table[i] !== null) {
            for (let element of numbers) {
                if ((i + element) <= target) {
                    const combination = [...table[i], element];
                    if (!table[i + element] || table[i + element].length > combination.length) {
                        table[i + element] = combination;
                    }
                }

            }
        }
    }
    return table[target];
}


console.log(bestSum(7, [5, 3, 4, 7]))
console.log(bestSum(8, [2, 3, 5]))
console.log(bestSum(8, [1, 4, 5]))
console.log(bestSum(100, [1, 2, 5, 25]))