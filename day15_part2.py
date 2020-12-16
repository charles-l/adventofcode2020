# really not very happy with this one since the perf
# is total garbage but it got the answer in a reasonable
# amount of time so i'm not bothering to improve it right now...
nums = [int(x) for x in '1,0,16,5,17,4'.split(',')]

i = 0
recently_spoken = {}

for i, x in enumerate(nums):
    recently_spoken[x] = i
    last_spoken = x

# NOTE: i falls through

while i < 30000000-1:
    if last_spoken in recently_spoken:
        n = i - recently_spoken[last_spoken]
    else:
        n = 0

    recently_spoken[last_spoken] = i
    last_spoken = n

    i += 1

print(last_spoken)
