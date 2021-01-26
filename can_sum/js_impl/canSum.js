const checkSum = (target, nums) => {

    if (target === 0) {
        return true;
    }
    if (target < 0) {
        return false;
    }
    for (element of nums) {
        const reminder = target - element;
        if (checkSum(reminder, nums) === true) {
            return true;
        }
    }

    return false;
}

const memoCheckSum = (target, nums,memo={}) => {
    if (target in memo){
        return memo[target];
    }
    if (target === 0) {
        return true;
    }
    if (target < 0) {
        return false;
    }
    for (element of nums) {
        const reminder = target - element;
        if (memoCheckSum(reminder, nums,memo) === true) {
            memo[target]=true;
            return true;
        }
    }
    memo[target]=false;
    return false;
}


// console.log(checkSum(7, [2, 3])) //true
// console.log(checkSum(7, [5, 3, 4, 5])) //true
// console.log(checkSum(7, [2, 4])) //false
// console.log(checkSum(8, [2, 3, 5])) //true
//console.log(checkSum(300, [7, 14])) //false
//////////////////////////////////////

console.log(memoCheckSum(7, [2, 3])) //true
console.log(memoCheckSum(7, [5, 3, 4, 5])) //true
console.log(memoCheckSum(7, [2, 4])) //false
console.log(memoCheckSum(8, [2, 3, 5])) //true
console.log(memoCheckSum(300, [7, 14])) //false