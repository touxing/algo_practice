#
# @lc app=leetcode.cn id=567 lang=python3
#
# [567] 字符串的排列
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
      need = collections.defaultdict(int)
      window = collections.defaultdict(int)
      for c in s1:
        need[c] += 1
      left = 0
      right = 0
      valid = 0
      while right < len(s2):
        c = s2[right]
        right += 1
        if need[c] > 0:
          window[c] += 1
          if window[c] == need[c]:
            valid += 1
        while right-left >= len(s1):
          if valid == len(need):
            return True
          d = s2[left]
          left += 1
          if need[d] > 0:
            if window[d] == need[d]:
              valid -= 1
            window[d] -= 1

      return False

# @lc code=end
