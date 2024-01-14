# https://www.geeksforgeeks.org/problems/grinding-geek/1

from typing import List

class Solution:
    def max_courses(self, n: int, total: int, cost: List[int]) -> int:
        dp = [[-1] * (total + 1) for _ in range(n)]
        return self.fn(0, cost, total, dp)

    def fn(self, i: int, cost: List[int], total: int, dp: List[List[int]]) -> int:
        if i == len(cost):
            return 0
        if dp[i][total] != -1:
            return dp[i][total]
        ans = self.fn(i + 1, cost, total, dp)
        if cost[i] <= total:
            ans = max(ans, 1 + self.fn(i + 1, cost, total - cost[i] + int(cost[i] * 9 / 10), dp))
        dp[i][total] = ans
        return ans