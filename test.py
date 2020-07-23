nums = [2, 3, 4, 2, 4]
size = len(nums)
tmp = {}
for i in range(0, size):
    if nums[i] not in tmp:
        tmp[nums[i]] = 0
    for j in range(i, size):
        if nums[i] == nums[j]:
            tmp[nums[i]] += 1
for k, v in tmp.items():
    if v == 1:
        print(k, v)


print(tmp)

class Solution:
  def minWindow(self, s:str, t:str) ->str:
    need = collections.defaultdict(int)
    for c in t:
      need[c] += 1

    needCount = len(t)
    left = 0 #窗口左边
    res = (0, float('inf'))
    for right, c in enumerate(s):
      if need[c]>0:
        needCount[c] -= 1

      need[c] -= 1
      if needCount[c] == 0:
        while True:
          c = s[left]
          if need[c] == 0:
            break
          need[c] += 1
          left += 1
        if right -left < res[1]-res[0]:
          res = (left, right)
        need[s[left]] += 1
        needCount += 1
        left += 1

    return '' if res[1]>len(s) else s[res[0]:res[1]+1]
