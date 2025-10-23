#biography = {'name':'Mikaela','hometown': 'Abu Dhabi' ,'age':22}
#for value in biography.values():
#    print(value)



#Advanced Requirements

name = input('what is your name?: ')
hometown = input('what is your hometown?: ')
while True:
    try:
        age = int(input('what is your age?: '))
        break
    except ValueError:
        print('Age must be an integer.')

user_dict = {'name': name, 'hometown': hometown, 'age': age}
print(user_dict)
