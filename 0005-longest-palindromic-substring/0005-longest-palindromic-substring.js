/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function(s) {
    let n = s.length;
    if (n <= 1) return s;
    let start = 0, len = 1;
    for (let i = 0; i < n; ) {
        let j = i, k = i;
        while (k < n - 1 && s[k + 1] === s[k]) ++k; // skip duplicate characters
        i = k + 1;
        while (j > 0 && k < n - 1 && s[j - 1] === s[k + 1]) { // expand from center
            --j;
            ++k;
        }
        let newLen = k - j + 1;
        if (newLen > len) {
            start = j;
            len = newLen;
        }
    }
    return s.substring(start, start + len);
};
