def transform_step(subject_number, value):
    return (value * subject_number) % 20201227

def find_loop_size(subject_number, transformed_value):
    value = 1
    loop_size = 0
    while value != transformed_value:
        value = transform_step(subject_number, value)
        loop_size += 1
    return loop_size

def transform(subject_number, loop_size):
    value = 1
    for i in range(loop_size):
        value = transform_step(subject_number, value)
    return value

card_public_key = 11404017
door_public_key = 13768789
card_loop_size = find_loop_size(7, card_public_key)
door_loop_size = find_loop_size(7, door_public_key)
encryption_key = transform(card_public_key, door_loop_size)
print(encryption_key)
