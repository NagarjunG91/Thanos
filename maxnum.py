def print_maximum(a, b):
    if a > b:
        return a
    elif a == b:
        print('both {} and {} are equal'.format(a, b))
        return a,b
    else:
        return b


guess1 = int(input('enter number 1:'))
guess2 = int(input('enter number 2:'))

print(print_maximum(guess1, guess2))

