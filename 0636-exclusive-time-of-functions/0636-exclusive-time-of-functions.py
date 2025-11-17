class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n
        stack = []
        prev_time = 0

        for log in logs:
            fid, typ, ts = log.split(":")
            fid = int(fid)
            ts = int(ts)

            if typ == "start":
                if stack:
                    # Add running time to the function currently on stack
                    res[stack[-1]] += ts - prev_time
                stack.append(fid)
                prev_time = ts
            else:  # "end"
                # Pop the function and add its exclusive time
                res[stack.pop()] += ts - prev_time + 1
                prev_time = ts + 1

        return res