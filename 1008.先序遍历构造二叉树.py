#
# @lc app=leetcode.cn id=1008 lang=python3
#
# [1008] 先序遍历构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        # 递归递归递归
        if preorder:
          p, root = [[], []], TreeNode(preorder.pop(0)) # 二维数组保存左右子节点，root取当前根节点
          [p[val > root.val].append(val) for val in preorder]
          root.left = self.bstFromPreorder(p[0]) # 当前节点<父节点 False=0 左节点
          root.right = self.bstFromPreorder(p[1]) # 当前节点>父节点 True=1 右节点
          return root
# @lc code=end
