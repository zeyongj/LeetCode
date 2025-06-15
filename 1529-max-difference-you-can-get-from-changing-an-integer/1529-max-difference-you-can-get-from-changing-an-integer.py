class Solution:
    def maxDiff(self, num: int) -> int:
        numStr = str(num)
        uniqueDigits = set(numStr)
        maxVal = num
        minVal = num

        for digit in uniqueDigits:
            for newDigit in '0123456789':
                if numStr[0] == digit and newDigit == '0':
                    continue
                newNumStr = numStr.replace(digit, newDigit)
                newNum = int(newNumStr)
                maxVal = max(maxVal, newNum)
                minVal = min(minVal, newNum)

        return maxVal - minVal