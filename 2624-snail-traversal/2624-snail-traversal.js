/**
 * @param {number} rowsCount
 * @param {number} colsCount
 * @return {Array<Array<number>>}
 */
Array.prototype.snail = function(numRows, numCols) {
  if (numRows * numCols !== this.length) return [];
  let result = Array(numRows).fill().map(() => []);
  for (let row = 0; row < numCols; row++) {
    for (let col = 0; col < numRows; col++) {
      result[(row & 1) ? numRows - col - 1 : col].push(this[row * numRows + col]);
    }
  }
  return result;
}

/**
 * const arr = [1,2,3,4];
 * arr.snail(1,4); // [[1,2,3,4]]
 */