class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fib_list = [1,1]
        while(fib_list[-1] + fib_list[-2] <= k):
            fib_list.append(fib_list[-1] + fib_list[-2])
        n = len(fib_list)
        count = 0
        for i in range(n-1,-1,-1):
            if(fib_list[i]<=k and k > 0):
                count += 1
                k -= fib_list[i]
        return(count)