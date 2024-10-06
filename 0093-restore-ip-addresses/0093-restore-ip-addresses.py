class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def valid(segment: str) -> bool:
            segment_length = len(segment)  # storing the length of each segment
            if (
                segment_length > 3
            ):  # each segment's length should be less than or equal to 3
                return False

            # Check if the current segment is valid
            # for either one of the following conditions:
            # 1. Check if the current segment is less than or equal to 255.
            # 2. Check if the length of the segment is 1. The first character of the segment
            #    can be `0` only if the length of the segment is 1.
            return int(segment) <= 255 if segment[0] != "0" else len(segment) == 1

        def update_segment(
            s: str, curr_dot: int, segments: List[str], result: List[str]
        ):
            segment = s[curr_dot + 1 : len(s)]
            if valid(segment):  # if the segment is acceptable
                segments.append(segment)  # add it to the list of segments
                result.append(".".join(segments))
                segments.pop()  # remove the top segment

        def backtrack(
            s: str, prev_dot: int, dots: int, segments: List[str], result: List[str]
        ):
            size = len(s)
            # The current dot curr_dot could be placed in
            # a range from prev_dot + 1 to prev_dot + 4.
            # The dot couldn't be placed after the last character in the string.
            for curr_dot in range(prev_dot + 1, min(size - 1, prev_dot + 4)):
                segment = s[prev_dot + 1 : curr_dot + 1]
                if valid(segment):
                    segments.append(segment)

                    # if all 3 dots are placed, add the solution to result
                    if dots - 1 == 0:
                        update_segment(s, curr_dot, segments, result)
                    else:
                        # continue to place dots
                        backtrack(s, curr_dot, dots - 1, segments, result)

                    segments.pop()  # remove the last placed segment

        # creating empty lists for storing valid IP addresses,
        # and each segment of IP
        result, segments = [], []
        backtrack(s, -1, 3, segments, result)
        return result