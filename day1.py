nums = set()
while True:
    try:
        nums.add(int(input()))
    except EOFError:
        break

for n in nums:
    if (2020 - n) in nums:
        print(n * (2020 - n))
        break
