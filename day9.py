with open('input_day9') as f:
    nums = [int(x.strip()) for x in f.readlines()]

window_n = 25
for i in range(window_n, len(nums)):
    s = set(nums[i-window_n:i])
    for a in s:
        if nums[i] - a in s:
            break
    else:
        print(nums[i])
        break
