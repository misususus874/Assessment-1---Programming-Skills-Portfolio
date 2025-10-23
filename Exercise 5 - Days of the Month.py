days_in_months = {
'1': 31, '2': 28, '3': 31, '4': 30, '5': 31, '6': 30,
    '7': 31, '8': 31, '9': 30, '10': 31, '11': 30,
    '12': 31}

user = input('Enter a month number: ')
if user == '2':
    answer = input('Is this a leap year?: ')
    if answer.lower() == 'yes':
        print('29')
    else:
        print(days_in_months.get(user))
elif user in days_in_months.keys():
    print(days_in_months.get(user))
else:
    print('Invalid Month!')