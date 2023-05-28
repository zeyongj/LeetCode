/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permuteUnique = function(nums) {
    let list = [];
    nums.sort((a, b) => a - b);
    backtrack(list, [], nums, []);
    return list;
};

function backtrack(list, tempList, nums, used){
    if(tempList.length == nums.length){
        list.push(Array.from(tempList));
        return;
    }
    for(let i = 0; i < nums.length; i++){
        if(used[i] || (i > 0 && nums[i] == nums[i-1] && !used[i - 1])) continue;
        used[i] = true;
        tempList.push(nums[i]);
        backtrack(list, tempList, nums, used);
        used[i] = false;
        tempList.pop();
    }
}
