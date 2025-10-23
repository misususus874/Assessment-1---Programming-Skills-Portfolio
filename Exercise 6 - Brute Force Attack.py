password = '12345'
attempts = 5

while True:
    user = input('Enter Password: ')
    if user == password:
        print('Password Matched!')
        break
    else:
        attempts -= 1
        print(f'Wrong Password! Attempts Remaining: {attempts}')
        if attempts == 0:
            print('The authorities have been alerted!')
            break
