class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        a = [[sum([int(x) for x in str(nums[i])]), nums[i]] for i in range(len(nums))]
        mx = 0
        b = [a[i][0] for i in range(len(a))]
        if len(b) == len(set(b)): return -1

        d = defaultdict(list)
        for i in range(len(a)):
            d[a[i][0]].append(a[i][1])

        c = list(d.values())
        for ar in c:
            if len(ar) >= 2:
                mx = max(sorted(ar)[-1]+sorted(ar)[-2], mx)
        return mx