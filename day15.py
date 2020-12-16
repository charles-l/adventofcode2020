nums = [int(x) for x in '1,0,16,5,17,4'.split(',')]

i = 0
while i < 2020:
    if nums[-1] in nums[:-1]:
        nums.append(nums[:-1][::-1].index(nums[-1]) + 1)
    else:
        nums.append(0)


    i += 1

print(nums[2020-1])
