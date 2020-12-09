with open('input_day9') as f:
    nums = [int(x.strip()) for x in f.readlines()]

target = 556543474
for i in range(len(nums)):
    for j in range(i+2, len(nums)):
        r = nums[i:j]
        if sum(r) == target:
            print(min(r) + max(r))
