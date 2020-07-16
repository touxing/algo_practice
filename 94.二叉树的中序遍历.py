#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
          return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

        # res = []
        # stack = []
        # cur = root
        # while stack or cur:
        #     while cur:
        #         stack.append(cur)
        #         cur = cur.left
        #     top = stack.pop()  # 此时左子树遍历完成
        #     res.append(top.val)  # 将父节点加入列表
        #     cur = top.right  # 遍历右子树
        # return res

        # traversal = lambda x: traversal(x.left) + [x.val] + traversal(x.right) if x else []
        # return traversal(root)
# @lc code=end
