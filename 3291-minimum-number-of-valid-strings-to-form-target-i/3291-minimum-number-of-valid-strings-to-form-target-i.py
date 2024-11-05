from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}

def build_trie(words):
    root = TrieNode()
    for word in words:
        node = root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
    return root

class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        root = build_trie(words)
        n = len(target)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0  
        for i in range(n):
            if dp[i] == float('inf'):
                continue
            node = root
            j = i
            while j < n and target[j] in node.children:
                node = node.children[target[j]]
                j += 1
                dp[j] = min(dp[j], dp[i] + 1)
        return dp[n] if dp[n] != float('inf') else -1    