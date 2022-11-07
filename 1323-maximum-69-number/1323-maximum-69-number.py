class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        num_char_list = list(str(num))

        for i, cur_char in enumerate(num_char_list):
            if cur_char == '6':
                num_char_list[i] = '9'
                break

        return int("".join(num_char_list))