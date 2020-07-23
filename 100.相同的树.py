#
# @lc app=leetcode.cn id=100 lang=python3
#
# [100] 相同的树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
      if not p and not q:
        return True
      if type(p) != type(q):
        return False
      if p.val != q.val:
        return False
      return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
# @lc code=end
