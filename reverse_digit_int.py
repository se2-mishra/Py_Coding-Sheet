# Python Program to Reverse a Number using While loop.
Number = int(input("Please Enter any Number: "))
Reverse = 0
while(Number>0):
    Reminder=Number%10.
    Reverse=(Reverse *10)+Reminder
    Number=Number//10.
str(print('Reverse of the numbers is',Reverse))