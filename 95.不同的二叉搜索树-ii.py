#
# @lc app=leetcode.cn id=95 lang=python3
#
# [95] 不同的二叉搜索树 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # root  leftChild < root  rightChild > root
    def generateTrees(self, n: int) -> List[TreeNode]:
      # 动态规划
      # 分阶段
      # 找状态
      # 做决策
      # 状态转移方程
      # 目标方程
      # 终止条件
      def generateTrees(start, end):
        if start > end:
          return [None,]

        allTrees = []
        for i in range(start, end+1):
          # 获得所有可行的左子树集合
          leftTree = generateTrees(start, i-1)
          # 获得所有可行的右子树集合
          rightTree = generateTrees(i+1, end)

          # 从左子树集合中选出一棵左子树，从右子树集合中选出一棵右子树，拼接到根节点上
          for l in leftTree:
            for r in rightTree:
              currTree = TreeNode(i)
              currTree.left = l
              currTree.right = r
              allTrees.append(currTree)
        return allTrees

      return generateTrees(1, n) if n else []











# @lc code=end
