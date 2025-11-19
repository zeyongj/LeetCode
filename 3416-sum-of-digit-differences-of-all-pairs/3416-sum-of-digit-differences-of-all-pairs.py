class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        num_strs = [str(num) for num in nums]
        digit_count = len(num_strs[0])
        n = len(nums)
        res = 0

        for digit_index in range(digit_count):
            freq = defaultdict(int)
            for num in num_strs:
                freq[num[digit_index]] += 1

            pairs = n * (n-1) //2
            same = 0
            for count in freq.values():
                if count > 1:
                    same += count * (count-1)//2

            diff_pairs = pairs - same
            res += diff_pairs

        return res
        