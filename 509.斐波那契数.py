#
# @lc app=leetcode.cn id=509 lang=python3
#
# [509] 斐波那契数
#

# @lc code=start
class Solution:
    memo = {}
    def fib(self, N: int) -> int:
      if N == 0:
        return 0
      if N == 1:
        return 1
      if bool(self.memo.get(N)):
        return self.memo.get(N)
      result = self.fib(N - 1) + self.fib(N - 2)
      self.memo.update({N: result})
      return result
    # def fib(self, N: int) -> int:
    #   if N == 0:
    #     return 0
    #   if N == 2 or N == 1:
    #     return 1;
    #   prev = curr = 1
    #   for i in range(3, N+1):
    #     total = prev + curr
    #     prev = curr
    #     curr = total
    #   return curr


# @lc code=end
