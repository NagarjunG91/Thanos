import mymodule
mymodule.say_hi()
print('version',mymodule._version_)

def print_maximum(a,b):
    if a > b:
        print('max is', a)
    elif a == b:
        print('both {} and {} are equal'.format(a, b))
    else:
        print('max is', b)


guess1 = int(input('enter number 1:'))
guess2 = int(input('enter number 2:'))

print_maximum(guess1, guess2)

if __name__ == '__main__':
                  print('this is main')
else:
     print('not main')


