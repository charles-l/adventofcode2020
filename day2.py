from collections import Counter

num_valid = 0
while True:
    try:
        counts, letter, password = input().split(' ')

        upper, lower = tuple(map(int, counts.split('-')))
        letter = letter[0]

        count = sum(1 for x in password if x == letter)
        if upper <= count <= lower:
            num_valid += 1
    except EOFError:
        break

print(num_valid)
