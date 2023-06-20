/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {    
    return s.trimEnd().split(" ").pop().length
};