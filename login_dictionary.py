

db= {'name':'123','name2':'1234','name3':'456'}
username=str(input("Enter username: "))
password=str(input("Enter password"))
if username in db:
    if db[username]==password:
        print('Logged in')
    else:
        print('Invalid password')
else:
    print('Invalid user')
