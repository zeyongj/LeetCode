class Solution(object):
    def equalFrequency(self, word):
        unique_vals = set(word)
        counts = []
        
        for i in unique_vals:
            counts.append(word.count(i))

        is_unique_max = len([i for i in counts if i == max(counts)])==1
        max_count =  len([i for i in counts if i == max(counts)])
        is_unique_min = len([i for i in counts if i == min(counts)])==1
        min_count =  len([i for i in counts if i == min(counts)])

        return ((max(counts) - min(counts) == 1 and (is_unique_max or (min(counts) == 1 and is_unique_min))) or max(counts) == 1) or len(unique_vals) == 1 or (max_count + 1 == len(unique_vals) and min(counts) == 1)