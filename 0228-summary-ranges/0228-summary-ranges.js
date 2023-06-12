/**
 * @param {number[]} nums
 * @return {string[]}
 */
var summaryRanges = function(nums) {
    const rangeAry = [];    
    for(var indexI=0; indexI<nums.length; indexI++){
   		 let startRange = nums[indexI];
         let endRange = null;
         while(Math.abs(nums[indexI+1] - nums[indexI]) === 1){
           endRange = nums[indexI+1];
           indexI++;
         }        
        rangeAry.push(endRange ? `${startRange}->${endRange}` : `${startRange}`);
      
    }
    
    return rangeAry;
};