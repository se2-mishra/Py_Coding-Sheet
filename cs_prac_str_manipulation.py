'''WAP that performs the following task
1). After getting a word from the user, your program should use a loop to print out
    each of the letters of the word. Just remember that strings in python start
    with element o!.
2). print out each letter in reverse order
3). Make a new variable that is the original word reverse and print variable.
4). Code to count number.'''
string1=input('Enter a string:')
length=len(string1)
var=''
for i in range(length):
    print(string1[i])
print('The number in reverse')
for a in range(-1,(-length-1),-1):
    print(string1[a])
    var+=string1[a]
print('the new variable is')
print(var)
print('Length of the variable is ',length)
