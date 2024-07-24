class Solution:
    def countAnagrams(self, s: str) -> int:
        def display(word):
            fact=math.factorial(len(word))
            hashmap={}
            for w in word:
                hashmap[w]=hashmap.get(w,0)+1
            
            for val in hashmap.values():
                fact//=math.factorial(val)
            
            return fact
        ways=1
        for word in s.split():
            ways*=display(word)
        return ways%((10**9)+ 7)