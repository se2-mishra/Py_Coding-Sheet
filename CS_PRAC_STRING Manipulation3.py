#WAP that inputs a word and prints 'Yes it starts!' if the given word starts with 0,1,2,...,9
text=input('Enter text:')
word=input('Enter word:')
length=len(word)
a=text.find(word,0)
b=text.find(word,1)
c=text.find(word,2)
d=text.find(word,3)
e=text.find(word,4)
f=text.find(word,5)
g=text.find(word,6)
h=text.find(word,7)
i=text.find(word,8)
j=text.find(word,9)
if length>=a and length<=j:
    print('YES')
