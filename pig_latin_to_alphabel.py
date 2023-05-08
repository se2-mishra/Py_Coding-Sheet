statement=input("Pleae enter a word: ")
vowels=('a','e','i','o','u','A','E','I','O','U')
words=statement.split()
for word in words:
    for i in word:
        if word[0] in vowels:
            print(word+"ay")
        else:
            print(word[1:]+word[0]+"ay")
