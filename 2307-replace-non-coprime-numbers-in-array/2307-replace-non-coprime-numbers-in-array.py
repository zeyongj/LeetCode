class Solution:
    def replaceNonCoprimes(self, nums):
        # This will store the result array.
        stack = []
        
        # Iterate through each number in the input list
        for num in nums:
            while stack and math.gcd(stack[-1], num) > 1:
                # If the top of the stack and current number are non-coprime, 
                # replace them with their LCM
                top = stack.pop()
                num = (top * num) // math.gcd(top, num)
            
            # Add the current number (or merged LCM) to the stack
            stack.append(num)
        
        # Return the final array after processing all numbers
        return stack