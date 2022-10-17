class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        seen = set(sentence)
        
        if len(seen) == 26:
            return True
        else:
            return False