/**
 * @param {number} n
 * @return {number}
 */
var minSteps = function(n) {
    const memo = {}

    function dfs(clipboard, aString) { 
        /*  base cases  */
            // if we are at length n, we are now at the desired length
            // so return 0 because we don't need to take anymore steps 

            // if clipboard or the current display of A's are
            // greater than n, copying and/or pasting is futile
            // because we can only return a string larger than length n
            // thus return Infinity
        if (aString.length === n) return 0 // base case 1
        if (clipboard.length > n || aString.length > n) return inf // base case 2

        /*  memoization/cache  */
        const memostr = `${clipboard}, ${aString}`
        if (memostr in memo) return memo[memostr]

        // if the string of  A's and what's copied on the clipboard 
        // are the same length, then we must have already copied
        // the current string of A's to the clipboard, so to avoid
        // an endless loop, set copy to infinity. otherwise we can copy
        const copy = aString.length > clipboard.length ? dfs(aString, aString) : inf

        // for paste, we must simply check if we have actually 
        // have something to paste. if we don't, then we will be
        // adding nothing to our current string of A's, putting us in
        // an infinite loop once again. therefore use infinity if clipboard
        // is empty
        const paste = clipboard.length > 0 ? dfs(clipboard, aString + clipboard) : inf

        // add 1 here to represent one step that is taken
        return memo[memostr] = 1 + Math.min(copy, paste)
    }

    return dfs('', 'A')
};

const inf = Infinity // help to shorten code lines