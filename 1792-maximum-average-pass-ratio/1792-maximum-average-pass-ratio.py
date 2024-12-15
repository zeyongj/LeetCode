class Solution:
     def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
            Queue = []
            for i in range(len(classes)):
                ratio = classes[i][0]/classes[i][1]
                newratio = (classes[i][0]+1)/(classes[i][1]+1)
                Queue.append((ratio - newratio, classes[i]))

            heapify(Queue)
            while extraStudents > 0:
                best = heappop(Queue)            
                ratio = (best[1][0]+1)/(best[1][1]+1)
                newratio = (best[1][0]+2) / (best[1][1]+2)
                best[1][0] += 1
                best[1][1] += 1
                heappush(Queue, (ratio - newratio, best[1]))
                extraStudents-=1

            out = 0
            for i in range(len(Queue)):
                out+= Queue[i][1][0]/Queue[i][1][1]

            return out/len(Queue)