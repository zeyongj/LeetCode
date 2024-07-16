class Solution:
    def mostFrequentPrime(self, mat: List[List[int]]) -> int:
        ROWS, COLS = len(mat), len(mat[0])

        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]
        count = {}
        
        def check_is_prime(number):
            for i in range(2, int(number**0.5) + 1):
                if number % i == 0:
                    return False
            return True
        
        def is_valid(r, c):
            return 0 <= r < ROWS and 0 <= c < COLS
        
        for r in range(ROWS):
            for c in range(COLS):
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    num = mat[r][c]
                    while is_valid(nr, nc):
                        if num > 10 and (num in count or check_is_prime(num)):
                            count[num] = count.get(num, 0) + 1
                        num = int(str(num) + str(mat[nr][nc]))
                        nr, nc = nr + dr, nc + dc
                    if num > 10 and (num in count or check_is_prime(num)):
                            count[num] = count.get(num, 0) + 1
        
        max_cnt = 0
        res = -1
        for k, v in count.items():
            if v > max_cnt or (v == max_cnt and k > res):
                max_cnt = v
                res = k
        
        return res
