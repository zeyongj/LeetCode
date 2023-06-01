/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    let map = {};
    for (let str of strs) {
        let sorted = [...str].sort().join('');
        if (!map[sorted]) {
            map[sorted] = [str];
        } else {
            map[sorted].push(str);
        }
    }
    return Object.values(map);
};
