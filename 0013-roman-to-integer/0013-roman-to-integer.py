class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sList = list(s)
        sLen = len(s)
        nums = []
        for i in range(sLen):
            if sList[i] == 'I':
                nums.append(1)
            elif sList[i] == 'V':
                nums.append(5)
            elif sList[i] == 'X':
                nums.append(10)
            elif sList[i] == 'L':
                nums.append(50)
            elif sList[i] == 'C':
                nums.append(100)
            elif sList[i] == 'D':
                nums.append(500)
            elif sList[i] == 'M':
                nums.append(1000)
        sums = 0
        for i in range(sLen-1):
            if nums[i] >= nums[i+1]:
                sums += nums[i]
            else:
                sums -= nums[i]
        sums += nums[-1]
        return sums