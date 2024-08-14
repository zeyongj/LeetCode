class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count the frequency of each task
        frequencies = Counter(tasks)

        # Sort the frequencies in descending order
        frequencies = sorted(frequencies.values(), reverse=True)

        # The maximum frequency
        max_freq = frequencies[0]

        # Calculate the maximum possible idle time
        idle_time = (max_freq - 1) * n

        # Reduce idle time based on the remaining tasks
        for freq in frequencies[1:]:
            idle_time -= min(max_freq - 1, freq)

        # Idle time can't be negative
        idle_time = max(0, idle_time)

        # Total time is the sum of tasks and the remaining idle time
        return len(tasks) + idle_time