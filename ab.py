

db= {'name':'123','name2':'1234','name3':'456'}
username=str(input("Please enter your preferred username: "))
password=str(input("Thank you, now enter a password as well.\n"))
if username in db:
    if db[username]==password:
        print('Logged in')
    else:
        print('Invalid password')
else:
    print('Invalid user')
