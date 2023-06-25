# @param {Integer} n
# @return {Integer[][]}
def generate_matrix(n)
  arr = Array.new(n){ Array.new(n) }
  
  i, j, di, dj = 0, 0, 0, 1
  (0...n*n).each do |k|
    arr[i][j] = k + 1  
    
    di, dj = dj, -di if arr[(i+di)%n][(j+dj)%n]
    
    i += di
    j += dj
  end
  
  arr
end