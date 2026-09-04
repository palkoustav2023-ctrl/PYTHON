#Program to find whether a given username contains less than 10 characters or not.
username = input('Enter your username: ')
length = len(username)

if length<10:
    print('your username contains less than 10 characters.')
else:
    print('Your username contains more than 10 characters.')