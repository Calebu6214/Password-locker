#!/usr/bin/env python3.8
# import pyperclip
from user import User

def create_user(userlogin_name,password):
    '''
    Function to create a new user
    '''
    new_user =User(userlogin_name,password)
    return new_user

        # save User
def save_users(user):
    '''
    Function to user
    '''
    user.save_user()



def main():
        print("Hello Welcome to your user list. What is your name?")
        user_name = input()

        print(f"Hello {user_name}. what would you like to do?")
        print('\n')

        while True:
                print("Use these short codes : ca - create a new account, dc - display credentials, fc -find a credential, ex -exit the user list, dl -delete the credentials,ce -copy credentials ")

                short_code = input().lower()

                if short_code == 'ca':
                        print("New User")
                        print("-"*10)

                        print ("Username ....")
                        userlogin_name = input()

                        print("Password ...")
                        password = input()


                        save_users(create_user(userlogin_name,password)) # create and save new user.
                        print ('\n')
                        print(f"New User {userlogin_name} {password} created")
                        print ('\n')

if __name__ == '__main__':

    main() 

