import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_map = {}
        min_heap = []
        output = []
        
        for word in words:
            if word not in word_map.keys():
                word_map[word] = 1
            else:
                word_map[word] += 1
        
        for word,freq in word_map.items():
            heapq.heappush(min_heap, (-1*freq, word))
            
        while (len(min_heap) > 0 and k > 0):
            output.append(heapq.heappop(min_heap)[1])
            k -= 1
        
        # output.reverse()
        
        return output