/**
 * @param {number} total
 * @param {number} cost1
 * @param {number} cost2
 * @return {number}
 */
var waysToBuyPensPencils = function(total, cost1, cost2) {
    var res = 0;
    while(total >= 0){
        res += Math.trunc((total/cost2)+1);
        total -= cost1;
    }
    return (res);
};