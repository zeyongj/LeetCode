class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
	    # Time: O(max(artifacts, dig)) which is O(N^2) as every position in the grid can be in dig
		# Space: O(dig) which is O(N^2)
        result, dig_pos = 0, set(tuple(pos) for pos in dig)
        for pos in artifacts:
            if all((x, y) in dig_pos for x in range(pos[0], pos[2] + 1) for y in range(pos[1], pos[3] + 1)):     
                result += 1
        return result