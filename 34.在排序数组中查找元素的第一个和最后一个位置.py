#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
      low = 0
      high = len(nums) - 1
      def binarySearchFirst(nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
          mid = low + ((high - low) >> 1)
          if target > nums[mid]:
            low = mid + 1
          elif target < nums[mid]:
            high = mid - 1
          else:
            if (mid == 0 or nums[mid - 1] != target):
              return mid
            else:
              high = mid - 1
        return -1

      def binarySearchLast(nums : List[int], target : int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
          mid = low + ((high - low) >> 1)
          if target < nums[mid]:
            high = mid - 1
          elif target > nums[mid]:
            low = mid + 1
          else:
            if (mid == len(nums) -1 or nums[mid+1] != target):
              return mid
            else:
              low = mid + 1
        return -1

      return [binarySearchFirst(nums, target), binarySearchLast(nums, target)]
# @lc code=end
