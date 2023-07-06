/**
 * @param {number} target
 * @param {number[]} nums
 * @return {number}
 */
var minSubArrayLen = function(s, nums) {
    let result = Number.MAX_SAFE_INTEGER
    let sum = 0, left = 0
    for(let i = 0; i < nums.length; i++){
        sum += nums[i]
        while(sum >= s){
            result = Math.min(result, i - left + 1)
            sum -= nums[left++]
        }
    }
    return result === Number.MAX_SAFE_INTEGER ? 0 : result 
};