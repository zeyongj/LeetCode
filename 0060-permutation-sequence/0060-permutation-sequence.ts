function getPermutation(n: number, k: number): string {
    let factorial = [1];
    for(let i = 1; i <= n ; i++) {
        factorial[i] = factorial[i-1]*i
    }
    let nums = Array.from({length: n},(v,i) => i+1);
    let res = ''
    for(let i = n; i > 0; i--) {
        let index = Math.ceil(k/factorial[i-1]);
        res += nums[index-1];
        nums.splice(index-1,1);
        k -= (factorial[i-1]*(index-1));
    }
    return res;
};