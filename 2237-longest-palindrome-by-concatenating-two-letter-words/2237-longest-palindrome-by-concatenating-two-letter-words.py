class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        freq=Counter(words)
        pal=0
        hasDouble=False
        for key, val in freq.items():
            if key[0]==key[1]:
                pal+=val//2*4
                if val&1: hasDouble=True
            elif key[0]<key[1]:
                rev=key[1]+key[0]
                pal+=min(val, freq[rev] )*4
        return pal+hasDouble*2