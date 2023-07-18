function climbStairs(n: number): number {
    const arr: number[] = [1,1]
    if(n<2){
        return 1
    }
    for(let i=2; i<=n; i++){
        const len  = arr.length
        arr.push(arr[len-1]+arr[len-2])
    }
    return arr[arr.length-1]
};