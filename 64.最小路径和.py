#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
      '''
      最值问题首先考虑动态规划算法
      遍历一个决策树
      [m][n] m行 n列
      1.路径 当前路径总数最短
      2.选择列表 在前面路径总数最短的路径中，选择最小路径
      3.结束条件 到达右下角 [m][n]
      '''
      if not grid or not grid[0]:
        return 0

      rows, columns = len(grid), len(grid[0])
      dp = [[0] * columns for _ in range(rows)]
      dp[0][0] = grid[0][0]

      for i in range(1, rows):
        dp[i][0] = dp[i - 1][0] + grid[i][0]
      for j in range(1, columns):
        dp[0][j] = dp[0][j - 1] + grid[0][j]

      for i in range(1, rows):
        for j in range(1, columns):
          dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

      return dp[rows-1][columns-1]

# @lc code=end
