class Solution:
    def frequencySort(self, s: str) -> str:
        # a string to store the final answer string
        answerString = ''
        # a dictionary that stores the frequency of each character
        hashMap = defaultdict(int)
        for i in s:
            hashMap[i] = hashMap[i] + 1
        # sorting the dictionary based on the values in descending order
        sortedHashMap = sorted(hashMap.items(), key=lambda x: x[1], reverse=True)
        # multiply the char with the frequency
        for char, frequency in sortedHashMap:
            answerString = answerString + char * frequency

        return answerString