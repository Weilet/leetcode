class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * 366
        for day in range(days[-1]+1):
            if day in days:
                dp[day] = min(dp[max(day-1, 0)]+costs[0], dp[max(day-7, 0)]+costs[1], dp[max(day-30, 0)]+costs[2])
            else:
                dp[day] = dp[day-1]
        ans = max(dp)
        return ans