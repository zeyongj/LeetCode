class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        ll = []
        sortedNums = sorted(nums)

        for num in sortedNums[0]:
            cou = 1

            for listNums in sortedNums[1:]:
                if num not in listNums:
                    cou = 0
                    break
            
            if cou:
                ll.append(num)

        return sorted(ll)