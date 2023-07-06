# @param {Integer} target
# @param {Integer[]} nums
# @return {Integer}
def min_sub_array_len(s, nums)
    return 0 if nums.empty?
    min = nil
    i,j = 0, 0
    sum = nums[i]
    while j < nums.size
        if(sum < s)
            j += 1
            sum += nums[j] if j < nums.size
            next
        end
        if(i==j)
            return 1
        end
        length = j-i + 1
        min = length if min.nil?
        min = length if min > length
        i += 1
        sum -= nums[i-1]
    end
    min ? min : 0
end