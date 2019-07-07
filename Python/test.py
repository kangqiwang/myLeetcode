nums=[1,5,3,4]
target=7
for i in range(len(nums)):
    a = target - nums.pop(0)
    if a in nums:
        print([i, nums.index(a)+i+1])

