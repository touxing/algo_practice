#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层次遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
      queue = collections.deque()
      queue.append(root)
      res = []
      while queue:
        size = len(queue)
        level = []
        for _ in range(size):
          cur = queue.popleft()
          if not cur: # 没有子节点？
            continue
          level.append(cur.val)
          queue.append(cur.left)
          queue.append(cur.right)
        if level:
          res.append(level)

      return res
# @lc code=end
