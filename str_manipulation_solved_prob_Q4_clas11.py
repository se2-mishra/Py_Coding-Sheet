inp=input('Please enter a string:')
while len(inp)<=4:
    if inp[-1]=='z':
        inp=inp[0:3]+'c'
    elif 'a' in inp:
        inp=inp[0]+'bb'
    elif not int(inp[0]):
        int='1'+inp[1:]+'z'
    else:
        inp=inp+'*'
print(inp)
    