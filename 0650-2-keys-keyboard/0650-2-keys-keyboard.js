/**
 * @param {number} n
 * @return {number}
 */
var minSteps = function(n) {
    const memo = {}
    function dfs(clipboard, aString) {
        if (aString === n) return 0
        if (clipboard > n || aString > n) return Infinity

        const memostr = `${clipboard}, ${aString}`
        if (memostr in memo) return memo[memostr]

        const copy = aString > clipboard ? dfs(aString, aString) : Infinity
        const paste = clipboard > 0 ? dfs(clipboard, aString + clipboard) : Infinity

        return memo[memostr] = 1 + Math.min(copy, paste)
    }

    return dfs(0, 1)
}