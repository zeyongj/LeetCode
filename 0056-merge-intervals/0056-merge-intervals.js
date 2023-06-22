/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
var merge = function(intervals) {
    intervals.sort((a,b) => a[0] - b[0]);
    const results = [];
    for(let interval of intervals) {
        const prev = results.at(-1);
        if (!results.length || prev[1] < interval[0]) {
            results.push(interval);
        } else {
            prev[1] = Math.max(prev[1], interval[1])
        }
    }
    return results;
};