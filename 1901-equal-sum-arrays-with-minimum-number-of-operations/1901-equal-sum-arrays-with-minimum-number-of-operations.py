class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        
        if len(nums1) > len(nums2)*6:
            return -1

        if len(nums2) > len(nums1)*6:
            return -1

        c1 = Counter(nums1)
        c2 = Counter(nums2)

        diff = sum(nums1) - sum(nums2) #this is the gap we have to cover
        ans = 0
        if diff > 0:
            currCut = 5
            while diff >=0:
                nums1find = 1+currCut
                nums2find = 6-currCut
                totalCutCount = c1[nums1find] + c2[nums2find]
                totalRed = totalCutCount*currCut
                if totalRed >= diff:
                    ans += ceil(diff/currCut)
                    return ans
                else:
                    diff -= totalRed
                    ans += totalCutCount
                currCut -= 1
        else:
            currCut = 5
            diff = abs(diff)
            while diff >0:
                nums2find = 1+currCut
                nums1find = 6-currCut
                totalCutCount = c1[nums1find] + c2[nums2find]
                totalRed = totalCutCount*currCut
                if totalRed >= diff:
                    ans += ceil(diff/currCut)
                    return ans
                else:
                    diff -= totalRed
                    ans += totalCutCount
                currCut -= 1
        return ans


