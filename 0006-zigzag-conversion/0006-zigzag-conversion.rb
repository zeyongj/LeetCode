# @param {String} s
# @param {Integer} num_rows
# @return {String}
def convert(s, numRows)
    return s if numRows == 1
    n = s.length
    zigzag = Array.new(numRows) { [] }
    row, direction = 0, -1
    s.chars.each do |c|
        zigzag[row] << c
        if row == 0 || row == numRows - 1
            direction = -direction
        end
        row += direction
    end
    zigzag.flatten.join
end

