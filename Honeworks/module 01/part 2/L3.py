is_wrong_pass = True
while is_wrong_pass:
    password = input("Come up with a password. It must consist of more than 8 characters and contain uppercase and lowercase letters:")
    if len(password) > 8 and password.lower() != password and password.upper() != password:
        is_wrong_pass = False
        print("Password saved successfully!")
    else:
        print("You entered a bad password. Try again.")
        