from fractions import Fraction

class Solution(object):
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        result = Fraction(0, 1)
        i = 0
        n = len(expression)
        
        while i < n:
            # Determine the sign of the current fraction
            sign = 1
            if expression[i] == '-':
                sign = -1
                i += 1
            elif expression[i] == '+':
                i += 1
            
            # Extract the numerator
            j = i
            while j < n and expression[j].isdigit():
                j += 1
            numerator = sign * int(expression[i:j])
            
            # Move past the '/' character
            i = j + 1
            
            # Extract the denominator
            j = i
            while j < n and expression[j].isdigit():
                j += 1
            denominator = int(expression[i:j])
            
            # Update the result using the current fraction
            result += Fraction(numerator, denominator)
            
            # Move to the next part of the expression
            i = j
        
        # Return the result as a string in the form of "numerator/denominator"
        return str(result.numerator) + "/" + str(result.denominator)
