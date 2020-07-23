#
# @lc app=leetcode.cn id=450 lang=python3
#
# [450] 删除二叉搜索树中的节点
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
      def getMinNode(node: TreeNode) -> TreeNode:
        # BST 最左边的就是最小的
        while node.left:
          node = node.left
        return node

      def getMaxNode(node: TreeNode) -> TreeNode:
        while node.right:
          node = node.right
        return node

      if root is None:
        return None
      if root.val == key:  # 找到，删除
        # 没有子节点
        if root.left is None and root.right is None:
          return None
        # 有一个右子节点
        if root.left is None:
          return root.right
        # 有一个左子节点
        if root.right is None:
          return root.left
        # 左右子节点都有的情况，找左子树中最大值替换，或找右子树中最小值替换
        if root.left is not None and root.right is not None:
          # minNode = getMinNode(root.right)
          # root.val = minNode.val
          # root.right = self.deleteNode(root.right, minNode.val) # 删除 minNode 上位的节点
          maxNode = getMaxNode(root.left)
          root.val = maxNode.val
          root.left = self.deleteNode(root.left, maxNode.val) # 删除上位的节点
      elif root.val > key:
        root.left = self.deleteNode(root.left, key)
      elif root.val < key:
         root.right = self.deleteNode(root.right, key)
      return root

# @lc code=end
