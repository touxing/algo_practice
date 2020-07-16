#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dp(n: int) -> int:
          if n in memo: return memo[n]
          if n == 0: return 0
          if n < 0: return -1
          res = float('INF')
          for coin in coins:
            subproblem = dp(n - coin)
            if subproblem == -1: continue
            res = min(res, 1 + subproblem)

          memo[n] = res if res != float('INF') else -1
          return memo[n]

        return dp(amount)
# @lc code=end
