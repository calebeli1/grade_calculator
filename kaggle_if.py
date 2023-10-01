def sign(num_arg):
    if num_arg <= -1:
        value = -1
    elif num_arg == 0:
        value = 0
    else:
        value = 1
    return value

print(sign(-10))

def sign(x):
    if x > 0:
        return 1
    if x == 0:
        return 0
    if x < 0:
        return -1

print(sign(-10))