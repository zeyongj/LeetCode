class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        return (Freq:=Counter(nums)) and (maxF:=max(Freq.values())) and sum(f==maxF for f in Freq.values())*maxF
        