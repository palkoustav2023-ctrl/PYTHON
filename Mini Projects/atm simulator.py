#Program of a working atm.
username = 'palkoustav2023'
pin = 251200
balance = 3000000
user_name = input('Enter your username: ')
user_pin = int(input('Enter your pin: '))
if user_name == username and user_pin == pin:
    print('Access granted! Welcome')
    status = input('''What do you want to do?
    (Withdraw, Deposit, Balance): ''').lower()
    if status == 'withdraw':
        withdraw = int(input('Enter amount: '))
        balance -= withdraw
        print('Amount successfully withdrawn')
    elif status == 'deposit':
        deposit = int(input('Enter amount: '))
        balance += deposit
        print('Amount successfully deposited')
    elif status == 'balance':
        print(balance,'is your current account balance in rupees')
    else:
        print('Error occured')
else:
    print('Access denied!')