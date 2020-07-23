#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
      if not nums:
        return 0

      preSum = 0
      maxAns = nums[0]
      for i in range(len(nums)):
        preSum = max(preSum+nums[i], nums[i])
        maxAns = max(preSum, maxAns)

      return maxAns
# @lc code=end
