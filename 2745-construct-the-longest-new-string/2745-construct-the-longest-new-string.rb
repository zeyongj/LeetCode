# @param {Integer} x
# @param {Integer} y
# @param {Integer} z
# @return {Integer}
def longest_string(x, y, z)
  ans = 0
  if x == y
    ans = 2 * [x, y].min
  else
    ans = 2 * [x, y].min + 1
  end

  ans += z

  return ans * 2
end
