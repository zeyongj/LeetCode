class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        # Create dictionaries to store the positions for 'a', 'b', and 'c'
        positions_a = {0: len(s)}
        positions_b = {0: len(s)}
        positions_c = {0: len(s)}
        
        n = len(s)
        count_a = 0
        
        # Fill positions_a with the indices of 'a'
        for i in range(n - 1, -1, -1):
            if s[i] == 'a':
                count_a += 1
                positions_a[count_a] = i
        
        count_b = 0
        # Fill positions_b with the indices of 'b'
        for i in range(n - 1, -1, -1):
            if s[i] == 'b':
                count_b += 1
                positions_b[count_b] = i
        
        count_c = 0
        # Fill positions_c with the indices of 'c'
        for i in range(n - 1, -1, -1):
            if s[i] == 'c':
                count_c += 1
                positions_c[count_c] = i
        
        # If k is 0, return 0 (no characters are needed)
        if k == 0:
            return 0
        
        # If there are not enough 'a', 'b', or 'c' characters to reach k, return -1
        if count_a < k or count_b < k or count_c < k:
            return -1
        
        # Initialize counters for the number of 'a', 'b', and 'c' in the current window
        a_count = 0
        b_count = 0
        c_count = 0
        result = -1
        
        # Calculate the initial result by checking the minimum length of the valid window
        result = n - min(positions_a.get(max(0, k - a_count)), 
                         min(positions_b.get(max(0, k - b_count)), 
                             positions_c.get(max(0, k - c_count))))
        
        # Iterate over the string to find the optimal result
        for i in range(n - 1):
            if s[i] == 'a':
                a_count += 1
            elif s[i] == 'b':
                b_count += 1
            else:
                c_count += 1
            
            result = min(result, i + 1 + n - min(positions_a.get(max(0, k - a_count)), 
                                                 min(positions_b.get(max(0, k - b_count)), 
                                                     positions_c.get(max(0, k - c_count)))))
        
        return result
