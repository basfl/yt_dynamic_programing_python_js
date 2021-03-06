const howSum = (target, numbers) => {
    const table = Array(target + 1).fill(null);
    table[0] = [];
    for (let i = 0; i < table.length; i++) {
        if (table[i] !== null) {
            for (let element of numbers) {
                if ((i + element) <= target) {
                    table[i + element] = [...table[i], element];
                }

            }
        }
    }
    return table[target];
}


console.log(howSum(7, [2, 3])) //[3,2,2]
console.log(howSum(7, [5, 3, 4, 7])) //[4,3]
console.log(howSum(7, [2, 4])) //null
console.log(howSum(8, [2, 3, 5])) //[2,2,2,2]
console.log(howSum(300, [7, 14])) //null