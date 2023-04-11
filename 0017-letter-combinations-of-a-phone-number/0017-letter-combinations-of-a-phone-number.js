/**
 * @param {string} digits
 * @return {string[]}
 */
function letterCombinations(digits) {
    if (digits.length === 0) {
        return [];
    }

    const phone = [
        '0', '1', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz'
    ];

    const result = [];

    function backtrack(combination, index) {
        if (index === digits.length) {
            result.push(combination);
            return;
        }

        const letters = phone[digits[index]];
        for (let i = 0; i < letters.length; i++) {
            backtrack(combination + letters[i], index + 1);
        }
    }

    backtrack('', 0);
    return result;
}
