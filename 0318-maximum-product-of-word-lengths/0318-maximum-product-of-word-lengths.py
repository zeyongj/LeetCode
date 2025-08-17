class Solution(object):
    def maxProduct(self, words):
        bitmasks = [sum(1 << (ord(c) - ord('a')) for c in set(w)) for w in words]
        products = [len(words[i]) * len(words[j]) 
                    for i in range(len(words)) 
                    for j in range(i + 1, len(words)) 
                    if not bitmasks[i] & bitmasks[j]]
        return max(products) if products else 0