class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        meetings.sort()

        count = [0] * n
        timer = [0] * n

        itr = 0

        while itr < len(meetings):
            start, end = meetings[itr]
            dur = end - start

            room = -1
            earliest = 10**18
            earliestRoom = -1

            for i in range(n):
                if timer[i] < earliest:
                    earliest = timer[i]
                    earliestRoom = i
                if timer[i] <= start:
                    room = i
                    break

            if room != -1:
                timer[room] = end
                count[room] += 1
            else:
                timer[earliestRoom] += dur
                count[earliestRoom] += 1

            itr += 1

        maxv = 0
        idx = 0
        for i in range(n):
            if count[i] > maxv:
                maxv = count[i]
                idx = i

        return idx