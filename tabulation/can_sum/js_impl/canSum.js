const canSum = (target, numbers) => {
    const table = Array(target + 1).fill(false);
    table[0] = true;
    for (let i = 0; i < table.length; i++) {
        if (table[i] === true) {
            for (let element of numbers) {
                if ((i + element) <= target) {
                    table[i + element] = true;
                }

            }
        }
    }
    return table[target];
}



console.log(canSum(7, [2, 3])) // t
console.log(canSum(7, [5, 3, 4, 7])) // t
console.log(canSum(7, [2, 4])) // f
console.log(canSum(8, [2, 3, 5])) // t
console.log(canSum(300, [7, 14])) // f