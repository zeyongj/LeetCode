class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        x, y = min(x, y), max(x, y)
        A = [0] * n
        for i in range(1, n + 1):
            A[0] += 2 									# go left and right
            A[min(i - 1, abs(i - y) + x)] -= 1 			# reach 1 then stop
            A[min(n - i, abs(i - x) + 1 + n - y)] -= 1 	# reach n then stop
            A[min(abs(i - x), abs(y - i) + 1)] += 1 	# reach x then split
            A[min(abs(i - x) + 1, abs(y - i))] += 1 	# reach y then split
            r = max(x - i, 0) + max(i - y, 0)
            A[r + (y - x + 0) // 2] -= 1 				# i -> x -> y <- x
            A[r + (y - x + 1) // 2] -= 1 				# i -> y -> x <- y
        return list(accumulate(A))