# pre calculating all prime factors for a num (2,mx)
MOD = 10 ** 9 + 7
MX = 10 ** 5 + 1
prime_factors = [0] * MX
for i in range(2, MX): 
    if prime_factors[i] == 0: 
        for j in range(i, MX, i): 
            prime_factors[j] += 1

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = [-1] * n
        right = [n] * n
        st = []

        #setting left, right boundaries for current index where it can be max prime score, Using Monotonic Stack
        for i, v in enumerate(nums): 
            while st and prime_factors[nums[st[-1]]] < prime_factors[v]: 
                right[st.pop()] = i
            if st: 
                left[i] = st[-1]
            st.append(i)

        #Greedy Selection of Elements
        ans = 1
        for i,v,l,r in sorted(zip(range(n),nums,left,right), key=lambda x: -x[1]): 
            total = (i-l)*(r-i)
            if total >= k: 
                ans = ans * pow(v,k,MOD) % MOD
                break
            ans = ans * pow(v,total,MOD) % MOD
            k -= total
        
        return ans