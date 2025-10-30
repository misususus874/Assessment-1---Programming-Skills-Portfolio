name_list = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

user = input("Enter a name: ")
if user.capitalize() in name_list:
    print(f"{user} is here!")
else:
    print("Person not found!")
