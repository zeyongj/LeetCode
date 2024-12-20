class Solution:
    def clumsy(self, n: int) -> int:
        res = "" + str(n)
        curr_op = 1

        for i in range(n - 1, 0, -1):
            i = str(i)
            if curr_op == 1:
                res += "*" + i
                curr_op += 1
            elif curr_op == 2:
                res += "//" + i
                curr_op += 1
            elif curr_op == 3:
                res += "+" + i
                curr_op += 1
            else:
                res += "-" + i
                curr_op = 1

        res = eval(res)
        return res