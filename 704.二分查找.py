#
# @lc app=leetcode.cn id=704 lang=python3
#
# [704] 二分查找
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
          mid = left + ((right - left) >> 1)
          if target == nums[mid]:
            return mid
          elif target < nums[mid]:
            right = mid - 1
          elif target > nums[mid]:
            left = mid + 1
        return -1
# @lc code=end
