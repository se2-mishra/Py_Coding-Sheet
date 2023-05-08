import random
import pdb
number=random.randint(10,50)
ctr=0
while ctr<5:
    pdb.set_trace()
    guess=int(input("Guess a Number Between 10 and 50:"))
    if guess==number:
        print('Congratulations,You Have won 5 Crore$!!!')
        break
    else:
        ctr+=1
        print("THIS was not the number. Take an another TRY")
        if not ctr<5:
            print('You Lose!,')
            print('The number was',number)