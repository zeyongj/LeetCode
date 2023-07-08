# @param {Integer} n
# @param {Integer} k
# @return {String}
def get_permutation(n, k)
    numbers = (1..n).to_a
    k -= 1
    permutation = ''
    
    while n > 0 do
        n -= 1
        factorial = Math.gamma(n+1).to_i  # gamma(n) = (n-1)!
        index, k = k.divmod(factorial)
        permutation += numbers.delete_at(index).to_s
    end
    
    return permutation
end