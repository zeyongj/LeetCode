/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function(n) {
    const result = [];
    generateParenthesisHelper(result, "", 0, 0, n);
    return result;
};

function generateParenthesisHelper(result, current, open, close, n) {
    if (current.length === n * 2) {
        result.push(current);
        return;
    }

    if (open < n) {
        generateParenthesisHelper(result, current + "(", open + 1, close, n);
    }

    if (close < open) {
        generateParenthesisHelper(result, current + ")", open, close + 1, n);
    }
}
