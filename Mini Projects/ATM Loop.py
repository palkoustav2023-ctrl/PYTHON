#Program of a working atm.
username = 'palkoustav2023'
pin = 251200
balance = 251200

while True:
    user_name = input('Enter your username: ')
    user_pin = int(input('Enter your pin: '))
    if user_name == username and user_pin == pin:
        print('Access granted! Welcome!')
        user = input('What do you want to do? (Withdraw, Deposit, Balance, Exit)').lower()
        if user == 'withdraw':
            withdraw = int(input('Enter amount: '))
            balance -= withdraw
            print('Amount withdrawn successfully!')
            print('Your current balance is', balance)
        elif user == 'deposit':
            deposit = int(input('Enter amount:'))
            balance += deposit
            print('Amount deposited successfully!')
            print('Your current balance is', balance)
        elif user == 'balance':
            print('Your current account balance is', balance)
        elif user == 'exit':
            print('Thank you for using our atm!')
            break
        else:
            print('Error occured')
    else:
        print('Access denied!')
