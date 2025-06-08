class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        output = []
        curr = 1

        for _ in range(n):
            output.append(curr)
            if curr*10 <= n:
                curr *= 10
            else:
                while curr%10 == 9 or curr+1 > n:
                    curr //= 10
                curr += 1
        
        return output
        