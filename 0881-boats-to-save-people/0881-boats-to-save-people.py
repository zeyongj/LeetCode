class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        counter = 0
        size = len(people)
        
        if size == 0:
            return counter
        
        people.sort()
        
        left = 0
        right = size - 1
        
        while (left <= right):
            if (people[left] + people[right] > limit):
                counter += 1
                right -= 1
            else:
                counter += 1
                right -= 1
                left += 1
            # if (people[left] + people[right] <= limit):
            #     left += 1
            # counter += 1
            # right -= 1
            
        
        return counter