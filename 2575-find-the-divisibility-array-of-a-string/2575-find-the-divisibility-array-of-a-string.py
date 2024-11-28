class Solution:
	def divisibilityArray(self, word: str, m: int) -> List[int]:
		result = [0 for _ in range(len(word))]

		current_num = 0

		for index in range(len(word)):
			current_num = (current_num * 10 + (int(word[index]))) % m

			if current_num == 0:
				result[index] = 1

		return result