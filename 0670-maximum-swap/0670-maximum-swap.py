class Solution:
    def maximumSwap(self, num: int) -> int:
        num_list = list(str(num))
        
        last = {int(d): i for i, d in enumerate(num_list)}
        
        for i, digit in enumerate(num_list):
            for d in range(9, int(digit), -1):
                if last.get(d, -1) > i:
                    # Swap and return the new number
                    num_list[i], num_list[last[d]] = num_list[last[d]], num_list[i]
                    return int(''.join(num_list))
        
        return num
