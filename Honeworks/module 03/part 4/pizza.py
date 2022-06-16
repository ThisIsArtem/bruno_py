import os.path
import json


def is_file_exist():
    if not os.path.isfile('users_data.json'):
        users_data_dict = {'admin': 'adminpass01'}
        with open('users_data.json', 'w') as f:
            json.dump(users_data_dict, f)


def is_correct_password(test_password):
    is_wrong_pass = True
    while is_wrong_pass:
        if len(test_password) > 8 and test_password.lower() != test_password and test_password.upper() != test_password:
            print("Password saved successfully!")
            return True
        print("You entered a bad password. Try again.")
        return False


def create_account(test_login, test_password):
    with open('users_data.json', 'r') as f:
        users_data = json.load(f)
    if test_login in users_data:
        print('The username you entered is not unique. Try again.')
    elif is_correct_password(test_password):
        users_data[test_login] = test_password
        with open('users_data.json', 'w') as f:
            json.dump(users_data, f)
        print('Account has been successfully created!')


def log_in_account(test_login, test_password):
    with open('users_data.json', 'r') as f:
        users_data = json.load(f)
    if test_login in users_data and users_data[test_login] == test_password:
        print('The login was completed successfully')
    else:
        print('Login or password entered incorrectly. Try again')


is_file_exist()
while True:
    way = input('Do you want to log in or create an account?')
    if way == 'log in':
        login = input('Enter your username:')
        password = input('Enter your password:')
        log_in_account(login, password)
    elif way == 'create':
        login = input('Come up with a username. Remember that the login must be unique:')
        password = input(
            'Come up with a password. It must consist of more than 8 characters and contain uppercase and lowercase '
            'letters:')
        create_account(login, password)
    else:
        print("I didn't understand you, try again")
