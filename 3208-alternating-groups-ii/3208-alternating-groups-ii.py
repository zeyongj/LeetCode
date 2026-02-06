class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n=len(colors)
        sz=n+k-1
        ans, alt, prev=0, 1, colors[0]
        for i in range(1, sz):
            i0=i%n
            alt=1 if prev==colors[i0] else alt+1
            ans+=(alt>=k)
            prev=colors[i0]
        return ans
        