class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        isVowel=1+(1<<(ord('e')-ord('a')))+(1<<(ord('i')-ord('a')))+(1<<(ord('o')-ord('a')))+(1<<(ord('u')-ord('a')))
        n, qz=len(words), len(queries)
        cnt=[0]*(n+1)
        for i, w in enumerate(words):
            cnt[i+1]=cnt[i]+(((1<<(ord(w[0])-ord('a')))& isVowel)!=0 and ((1<<(ord(w[-1])-ord('a')))& isVowel)!=0)
        ans=[0]*qz
        for i, (q0, q1) in enumerate(queries):
            ans[i]=cnt[q1+1]-cnt[q0]
        return ans
        
        