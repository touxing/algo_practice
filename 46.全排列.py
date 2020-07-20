#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums: List[int], track: List[int]):
            '''
            路径：记录在 track中
            选择列表 nums中不存在于track中的那些元素
            结束条件 nums中的元素全部再track中出现
            '''
            # 触发结束条件
            if len(track) == len(nums):
                # 列表是引用传递，导致返回的结构是 [[],[],[]]
                # 传递拷贝值
                res.append(track[:])
                return

            for item in nums:
              # 排除不合法的选择
              if item in track:
                continue
              # 做选择
              track.append(item)
              # 进入下一层决策树
              backtrack(nums, track)
              # 取消选择
              track.pop()
        res = []
        track = [] # 记录路径
        backtrack(nums, track)
        return res



# @lc code=end
