with open('input_day10', 'r') as f:
    nums = [int(x.strip()) for x in f.readlines()]

nums = sorted(nums)
n1 = 0
n3 = 0
j = 0
for x in nums:
    if x - j == 1:
        n1 += 1
        j = x
    elif x - j == 3:
        n3 += 1
        j = x
    else:
        print('early break')
        break

# final increase
j += 3
n3 += 1

print(f'{j=} {n1=} {n3=}')
print('answer:', n1 * n3)
