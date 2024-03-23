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
        # from collections import Counter
        # count = Counter(words) can do the same thing!
        
        for word,freq in word_map.items():
            heapq.heappush(min_heap, (-1*freq, word))
            
        #  The heap is primarily ordered by the first element of the tuple, which is the negative frequency -1*freq. (Given this is a minheap, the actual ranking is from the largest to the smallest)
        # Second Element (word): If two frequencies are equal (after negation), Python uses the second element of the tuple to break ties. Since strings are ordered lexicographically in Python, the word that comes first in alphabetical order, i.e. lexicographical order. om the problem, will precede others with the same frequency.
        
        while (len(min_heap) > 0 and k > 0):
            output.append(heapq.heappop(min_heap)[1])
            k -= 1
        
        # output.reverse() And therefore, reverse is not needed, as the words are appened in their lexicographical order.
        
        return output