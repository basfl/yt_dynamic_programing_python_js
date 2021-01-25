const slowFib = (n) => {
    if (n <= 2) return 1;
    return slowFib(n - 1) + slowFib(n - 2);

}

const memoFib = (n, memo = {}) => {
    if (n in memo) {
        return memo[n];
    }
    if (n <= 2) {
        return 1;
    } else {
        memo[n] = memoFib(n - 1,memo) + memoFib(n - 2,memo);
        return memo[n];
    }
}


console.log(slowFib(7));
console.log(memoFib(50));