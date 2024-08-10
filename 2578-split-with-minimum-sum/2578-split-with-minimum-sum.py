from queue import PriorityQueue

class Solution:
    def splitNum(self, num: int) -> int:
        a = [int(x) for x in str(num)]
        pq = PriorityQueue()
        num1 = ""
        num2 = ""
        for i in a:
            pq.put(i)

        while not pq.empty():
            num1 += str(pq.get())
            if not pq.empty():
                num2 += str(pq.get())

        if num2:
            return int(num1) + int(num2)
        else:
            return int(num1)
