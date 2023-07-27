/**
 * @param {string[]} words
 * @param {number} maxWidth
 * @return {string[]}
 */
var fullJustify = (words, maxWidth) => {
  const n = words.length;
  const res = [];

  for (var i = 0; i < n; i = j) {
    // Step 1. Use j to find out where to cut the row (i ... j-1)
    let len = -1;
    for (var j = i; j < n && len + 1 + words[j].length <= maxWidth; j++) {
      len += 1 + words[j].length;
    }

    // Step 2. Calculate how many spaces to add for each word
    let spaces = 1; // avg. spaces reserved for each word
    let extra = 0; // extra left spaces

    if (j !== i + 1 && j !== n) {
      spaces = (maxWidth - len) / (j - 1 - i) + 1;
      extra = (maxWidth - len) % (j - 1 - i);
    }

    // Step 3. Build the row with spaces + extra space + word
    let row = words[i];
    for (let k = i + 1; k < j; k++, extra--) {
      row += ' '.repeat(spaces + (extra > 0 ? 1 : 0)) + words[k];
    }
    row += ' '.repeat(maxWidth - row.length);

    // Step 4. Push the row to final result
    res.push(row);
  }

  return res;
};