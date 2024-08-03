/**
 * @param {number[]} targetArray
 * @param {number[]} currentArray
 * @return {boolean}
 */
var canBeEqual = function(targetArray, currentArray) {
    const elementCounts = new Array(1001).fill(0);
    let uniqueCount = 0;
    
    for (let i = 0; i < targetArray.length; i++) {
        if (elementCounts[targetArray[i]]++ === 0) uniqueCount++;
        if (elementCounts[currentArray[i]]-- === 1) uniqueCount--;
    }
    
    return uniqueCount === 0;
};