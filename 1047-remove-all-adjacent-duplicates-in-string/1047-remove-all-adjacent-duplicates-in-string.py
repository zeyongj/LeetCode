class Solution:
    def removeDuplicates(self, s: str) -> str:
        # Create an empty stack.
        stack = []
        # Iterate over the string
        for char in s:
            # If stack has at least one character and
            # stack's top character is same as the string's character
            if stack and stack[-1] == char:
                # Pop a character from the stack.
                stack.pop()
            else:
                # Otherwise, push that character onto the stack.
                stack.append(char)

        # Form a string from stack's elements and return that.
        return "".join(stack)
