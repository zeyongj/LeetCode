/**
 * @param {string} s
 * @return {boolean}
 */
var isNumber = function(s) {
    return (! isNaN(s) ) && ( s.trim() !== "" ) && (! s.includes("Infinity") )
};