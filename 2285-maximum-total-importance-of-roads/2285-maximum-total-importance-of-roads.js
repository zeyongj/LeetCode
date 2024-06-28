/**
 * @param {number} n
 * @param {number[][]} roads
 * @return {number}
 */
var maximumImportance = function(n, roads) {
    let res = 0, cost = 1;
    let conn = new Array(n).fill(0);

    for (const road of roads) {
        conn[road[0]]++;
        conn[road[1]]++;
    }

    conn.sort((a, b) => a - b);

    for (const con of conn) {
        res += con * cost++;
    }
    return res;
};