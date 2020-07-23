#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
      if not root:
        return 0
      children = [root.left, root.right]
      if not any(children):
        return 1
      min_depth = float('inf')
      for c in children:
        if c:
          min_depth = min(self.minDepth(c), min_depth)
      return min_depth + 1
# @lc code=end
