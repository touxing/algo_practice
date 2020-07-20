#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
      '''
      暴力破解，穷举法
      '''
      # 当前滑动窗口中需要的各元素的数量
      need=collections.defaultdict(int)
      for c in t:
          need[c]+=1
      needCnt=len(t) # 所需元素的总数量
      left=0 # 窗口左边界
      res=(0,float('inf'))
      for right,c in enumerate(s):
          # right 窗口有边界
          # 包含待查找的子串，窗口左边缩小
          if need[c]>0:
              needCnt-=1

          need[c]-=1 #
          if needCnt==0:       #步骤一：滑动窗口包含了所有T元素
              while True:      #步骤二：左边窗口缩小，排除多余元素
                  c=s[left]
                  if need[c]==0:
                      break
                  need[c]+=1
                  left+=1
              if right-left<res[1]-res[0]:   #记录结果
                  res=(left,right)
              need[s[left]]+=1  #步骤三：left增加一个位置，窗口右边放大，寻找新的满足条件滑动窗口
              needCnt+=1
              left+=1
      return '' if res[1]>len(s) else s[res[0]:res[1]+1]    #如果res始终没被更新过，代表无满足条件的结果
