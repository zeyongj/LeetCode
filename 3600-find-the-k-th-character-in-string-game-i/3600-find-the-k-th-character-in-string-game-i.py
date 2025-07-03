class Solution:
    def kthCharacter(self, k: int) -> str:
        sb = ['a']
        while len(sb) < k:
            size = len(sb)
            for i in range(size):
                next_char = chr(ord('a') + ((ord(sb[i]) - ord('a') + 1) % 26))
                sb.append(next_char)
        return sb[k - 1]