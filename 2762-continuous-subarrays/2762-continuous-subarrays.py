from sortedcontainers import SortedList

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        sl = SortedList([])
        # Add an element to the end of the array that will trigger the removal of all the elements from the sortedlist
        nums.append(-5)
        start = 0
        sl.add(nums[start])
        count = 0
        for i in range(1, len(nums)):
            added = nums[i]
            sl.add(added)
            while abs(added - sl[0]) > 2 or abs(added - sl[-1]) > 2:
                subArrays = len(sl) - 1
                # The number of subarrays without the recently-added element that start with the left-most element in the sliding window is equal to the length of the sliding window witohut the recently-added element
                count += subArrays
                # Remove the leftmost element from the window
                sl.remove(nums[start])
                # Move the sliding window start position
                start += 1
        return count