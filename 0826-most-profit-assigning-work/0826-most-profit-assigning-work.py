class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        job_profile = [(0, 0)]
        for i in range(len(difficulty)):
            job_profile.append((difficulty[i], profit[i]))
        # Sort by difficulty values in increasing order.

        job_profile.sort()
        for i in range(len(job_profile) - 1):
            job_profile[i + 1] = (
                job_profile[i + 1][0],
                max(job_profile[i][1], job_profile[i + 1][1]),
            )
        net_profit = 0
        for i in range(len(worker)):
            ability = worker[i]

            # Find the job with just smaller or equal difficulty than ability.

            l, r = 0, len(job_profile) - 1
            job_profit = 0
            while l <= r:
                mid = (l + r) // 2
                if job_profile[mid][0] <= ability:
                    job_profit = max(job_profit, job_profile[mid][1])
                    l = mid + 1
                else:
                    r = mid - 1
            # Increment profit of current worker to total profit.

            net_profit += job_profit
        return net_profit