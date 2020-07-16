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
