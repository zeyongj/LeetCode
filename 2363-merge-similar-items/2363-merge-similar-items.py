class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        res = []
        helper = [0] * 1001
        for arr in items1:
            helper[arr[0]] = arr[1]
        for arr in items2:
            if helper[arr[0]]:
                helper[arr[0]] += arr[1]
            else:
                helper[arr[0]] = arr[1]
        for i in range(1001):
            if helper[i]:
                res.append([i, helper[i]])

        return res