class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        hm1 = Counter(secret)
        hm2 = Counter(guess)
        count = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                count += 1
        cows = 0
        for key, val in hm1.items():
            if key in hm2:
                if hm2[key] >= val:
                    cows += val
                else:
                    cows += hm2[key]
        cows -= count
        result = ""
        result += str(count) + 'A' + str(cows) + 'B'
        return result