/**
 * @param {number} radius
 * @param {number} xCenter
 * @param {number} yCenter
 * @param {number} x1
 * @param {number} y1
 * @param {number} x2
 * @param {number} y2
 * @return {boolean}
 */
var checkOverlap = function (radius, xCenter, yCenter, x1, y1, x2, y2) {
    let x = Math.max(x1, Math.min(x2, xCenter));
    let y = Math.max(y1, Math.min(y2, yCenter));
    let xD = xCenter - x;
    let yD = yCenter - y;
    return xD ** 2 + yD ** 2 <= radius ** 2;
};