import hashlib
import json
def hash_password(password):
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    return password_hash
def register():
    username = input('Enter a username: ')
    password = input('Enter a password: ')
    password_hash = hash_password(password)
    user = {'username': username, 'password_hash': password_hash}
    with open('users.json', 'a') as file:
        json.dump(user, file)
        print('User registered successfully.')
def login():
    username = input('Enter username: ')
    password = input('Enter password: ')
    password_hash = hash_password(password)
    with open('users.json', 'r') as file:
        users = json.load(file)
        for user in users:
            if user['username'] == username and user['password_hash'] == password_hash:
                print('Access granted.')
                return
        print('Access denied.')
choice = input('Do you want to login or register? (login/register) ')
if choice == 'login':
    login()
elif choice == 'register':
    register()
else:
    print('Invalid choice.')
