nums = set()

while True:
    try:
        nums.add(int(input()))
    except EOFError:
        break

for i in nums:
    for j in nums:
        if 2020 - (i + j) in nums:
            print((2020 - (i + j)) * i * j)
