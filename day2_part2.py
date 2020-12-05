from collections import Counter

num_valid = 0
while True:
    try:
        positions, letter, password = input().split(' ')

        first, second = tuple(map(lambda x: int(x) - 1, positions.split('-')))
        letter = letter[0]

        if (password[first] == letter) ^ (password[second] == letter):
            num_valid += 1
    except EOFError:
        break

print(num_valid)
