const gridTravel = (m, n) => {
    if (m === 1 && n === 1) {
        return 1;
    }
    if (m === 0 || n === 0) {
        return 0;
    }
    return gridTravel(m - 1, n) + gridTravel(m, n - 1);
}

const memoGridTravel = (m, n, memo = {}) => {
    const key = m + "," + n
    if (key in memo) {
        return memo[key]
    }

    if (m === 1 && n === 1) {
        return 1;
    }
    if (m === 0 || n === 0) {
        return 0;
    }
    memo[key] = memoGridTravel(m - 1, n, memo) + memoGridTravel(m, n - 1, memo);
    return memo[key];


}
// console.log(gridTravel(1, 1)) / 1
// console.log(gridTravel(2, 3)) // 3
// console.log(gridTravel(3, 2)) // 3
// console.log(gridTravel(3, 3)) // 6
// console.log(grid_travel(18,18)) //2333606220

console.log(memoGridTravel(1, 1)) / 1
console.log(memoGridTravel(2, 3)) // 3
console.log(memoGridTravel(3, 2)) // 3
console.log(memoGridTravel(3, 3)) // 6
console.log(memoGridTravel(18,18)) //2333606220