def reverse(text):
    return text[::-1]


def palindrome(text):
    return text == reverse(text)


s = input('enter something:')

if palindrome(s):
    print('is palindrone')
else:
    print('foff mate')

poem = """\
hello hello hello {}
is there anybody in there
i cant escape this reality
""".format(s)

f = open('poem.txt', 'w')
f.write(poem)
f.close()
# rt is read text can  be only r

with open('poem.txt', 'rt') as f:
    for line in f:
        print(line, end='')

