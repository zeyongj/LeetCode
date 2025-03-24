class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        
        meeting_days_count = 0
        current_start = current_end = -1
        
        for start, end in meetings:
            if start > current_end:
                if current_end != -1:
                    meeting_days_count += current_end - current_start + 1
                current_start, current_end = start, end
            else:
                current_end = max(current_end, end)
        
        if current_end != -1:
            meeting_days_count += current_end - current_start + 1
        
        return days - meeting_days_count