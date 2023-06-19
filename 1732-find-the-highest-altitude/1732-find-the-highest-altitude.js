/**
 * @param {number[]} gain
 * @return {number}
 */
var largestAltitude = function(gain) {
    var altitude = 0;
    var maxAltitude = 0;
    var len = gain.length;
        
    for (var i = 0; i < len; i++) {
        altitude += gain[i];
        maxAltitude = Math.max(maxAltitude, altitude);
    }
        
    return maxAltitude;    
};