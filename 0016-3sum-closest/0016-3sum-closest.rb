# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer}
def three_sum_closest(nums, target)
    n = nums.length
    nums.sort!
    closest_sum = nums[0] + nums[1] + nums[2]
    min_diff = (target - closest_sum).abs

    (0...n - 2).each do |i|
        left = i + 1
        right = n - 1

        while left < right
            sum = nums[i] + nums[left] + nums[right]
            diff = (target - sum).abs

            if diff < min_diff
                min_diff = diff
                closest_sum = sum
            end

            if sum < target
                left += 1
            elsif sum > target
                right -= 1
            else
                return target # The sum is equal to the target, so it's the closest.
            end
        end
    end

    closest_sum
end
