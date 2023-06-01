from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            sorted_s = "".join(sorted(s))
            anagrams[sorted_s].append(s)
        return list(anagrams.values())
