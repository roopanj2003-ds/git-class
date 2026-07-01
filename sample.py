





password = input("Enter password: ")

contains_number = 0  
contains_upper = 0 #uppercase letter

for ch in password:
    digits= ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    if ch in digits:
      contains_number += 1
    

    if password == password.upper() and password != password.lower():
        contains_upper+= 1

if len(password) >= 8  and contains_number > 0 and contains_upper > 0:
    print("Strong Password")
else:
    print("Weak Password")




